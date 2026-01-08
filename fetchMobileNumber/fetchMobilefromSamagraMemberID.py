# Fetch Mobile number into excel file by searching member ID in a browser window
import pandas as pd
import pyperclip
import pyautogui
import time
import re
import sys
import os


# Step 1: Load the Excel file into a DataFrame
def load_excel(file_path):
    return pd.read_excel(file_path)


# Step 2: Identify all 8-digit numbers in the DataFrame
def find_eight_digit_cells(df):
    eight_digit_cells = []
    for index, row in df.iterrows():
        for col in df.columns:
            value = str(row[col])  # Convert to string for checking
            value = value.split(".")[0]
            if len(value) == 9 and value.isdigit():
                eight_digit_cells.append((index, col, value))
    return eight_digit_cells


# Step 3: Process each 8-digit number and perform required actions
def process_eight_digit_numbers(df, cells, output_file_name):
    total_count = len(df)
    print("Total : ", total_count)
    count = 0
    start_time = time.perf_counter()
    print("Script starting in 2 seconds switch to browser")
    time.sleep(1)
    global estimate
    try:
        for index, col, value in cells:
            # 1) Copy the 8-digit number to clipboard
            count += 1
            print(f"S.No {count}/{total_count}", end=" ")
            pattern = r"\b\d{10}\b"
            if "Mobile_Number" in df.columns:
                dataCheck = df.at[index, "Mobile_Number"]
                if re.search(pattern, str(dataCheck)) or "id not found" in str(
                    dataCheck
                ):
                    print("Value already exists")
                    if count == 1:
                        estimate = 1
                    continue
            pyperclip.copy(value)
            # 2) Open a website (URL needs to be specified)
            # if df.at[index]:
            # df = df.drop(index)
            time.sleep(0.2)
            web_url = "https://csmsmpscsc.mp.gov.in/rationmitra/EBS/RCMS/AddMember.aspx"  # Change to the desired URL
            pyautogui.hotkey("ctrl", "l")  # Focus address bar
            time.sleep(0.2)  # Wait for a second
            pyautogui.write(web_url)
            pyautogui.press("enter")

            # Wait for the page to load (you may need to adjust this)
            time.sleep(1.5)
            pyautogui.click(x=1065, y=512)  # Replace with actual coordinates
            time.sleep(0.1)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.hotkey("tab")
            time.sleep(1.2)
            pyautogui.hotkey("tab")
            time.sleep(0.2)
            pyautogui.hotkey("enter")
            time.sleep(1.5)
            pyautogui.click(x=566, y=857)
            time.sleep(0.1)
            pyautogui.click(x=566, y=857)
            # 3) Paste value in a search field using pyautogui
            # pyautogui.hotkey("ctrl", "a")
            # time.sleep(0.1)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(0.1)
            copied_text = pyperclip.paste()
            pyautogui.click(x=972, y=716)  # Replace with actual coordinates

            # 9) Find a 10-digit number in that copied text
            match = re.search(r"\b\d{10}\b", copied_text)
            if match:
                found_number = match.group(0)
                # Add the found digit number into a new column in the DataFrame
                df.loc[index, "Mobile_Number"] = int(found_number)
                print(f"{count}/{total_count} - {value},  - {found_number}")
            elif "Member details not found for above" in copied_text:
                df.loc[index, "Mobile_Number"] = "id not found"
                print(f"RC Number {value} is not valid")
            else:
                df.loc[index, "Mobile_Number"] = None
                print(f"{count}/{total_count} - {value},  - NA")

            one_time = time.perf_counter()
            if count == 1:
                estimate = (one_time - start_time) * total_count
                print(f"Estimated time : {estimate / 60:.1f},minutes")
            elif estimate == 1:
                estimate = (one_time - start_time) * (total_count - count)
                print(f"Estimated time : {estimate / 60:.1f},minutes")
            elif count % 10 == 0:
                remaining_time = estimate - (one_time - start_time)
                print(f"Remaining time : {remaining_time / 60:.1f},minutes")
        return df
    except pyautogui.PyAutoGUIException:
        print("Failsafe triggered, writing results to excel files")
        df.to_excel(output_file_name, index=False)
    except KeyboardInterrupt:
        print("Closing")
        df.to_excel(output_file_name, index=False)


# Main function to execute the script
def main():
    file_path = sys.argv[1]  # Provide your Excel file path
    df = load_excel(file_path)
    output_file_name = os.path.basename(file_path)
    # backup_file
    df.to_excel(f"backup{output_file_name}")
    print("backup file created")
    print(output_file_name)
    eight_digit_cells = find_eight_digit_cells(df)
    if eight_digit_cells:
        df = process_eight_digit_numbers(df, eight_digit_cells, output_file_name)
        # df.to_excel(output_file_name, index=False)  # Output file name
        if df is not None and not df.empty:
            df.to_excel(output_file_name, index=False)
        else:
            print("DataFrame is empty or invalid, skipping export.")
        print(f"Saved to {output_file_name}")
    else:
        print("no 8 digit found")


if __name__ == "__main__":
    main()

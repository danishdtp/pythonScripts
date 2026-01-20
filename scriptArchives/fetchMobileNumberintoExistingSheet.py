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
            if len(value) == 8 and value.isdigit():
                eight_digit_cells.append((index, col, value))
    return eight_digit_cells


# Step 3: Process each 8-digit number and perform required actions
def process_eight_digit_numbers(df, cells, output_file_name):
    total_count = len(df)
    print("Total : ", total_count)
    count = 0
    start_time = time.perf_counter()
    global estimate
    try:
        for index, col, value in cells:
            # 1) Copy the 8-digit number to clipboard
            count += 1
            print(f"S.No {count}/{total_count}", end=" ")

            pattern = r"\b\d{10}\b"
            if "Mobile_Number" in df.columns:
                dataCheck = df.at[index, "Mobile_Number"]
                if re.search(
                    pattern, str(dataCheck)
                ) or f"RC Number {value} is not valid" in str(dataCheck):
                    print("Value already exists")
                    if count == 1:
                        estimate = 1
                    continue
            pyperclip.copy(value)

            #     "https://epos.mp.gov.in/RC_Mobile_Int.jsp"  # Change to the desired URL
            # )
            # pyautogui.hotkey("ctrl", "l")  # Focus address bar
            # time.sleep(0.2)  # Wait for a second
            # pyautogui.write(web_url)
            # pyautogui.press("enter")
            #
            # Wait for the page to load (you may need to adjust this)
            time.sleep(0.2)
            pyautogui.click(x=698, y=319)  # Replace with actual coordinates
            time.sleep(0.2)
            pyautogui.click(x=698, y=319)  # Replace with actual coordinates
            # 3) Paste value in a search field using pyautogui
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)
            # pyautogui.write(value)

            # 4) Click on the submit button (coordinates need to be adjusted)
            pyautogui.click(x=843, y=321)  # Replace with actual coordinates

            # 5) Wait for 2 seconds
            time.sleep(2)
            pyautogui.click(x=864, y=456)
            # 6) Drag to select the text
            pyautogui.hotkey("ctrl", "a")
            time.sleep(0.5)
            # 7) Copy that text
            pyautogui.hotkey("ctrl", "c")

            # 8) Wait a moment for the clipboard to update
            time.sleep(0.3)
            copied_text = pyperclip.paste()

            # 9) Find a 10-digit number in that copied text
            match = re.search(r"\b\d{10}\b", copied_text)
            if match:
                found_number = match.group(0)
                # Add the found digit number into a new column in the DataFrame
                df.loc[index, "Mobile_Number"] = found_number
                print(f"{count}/{total_count} - {value},  - {found_number}")
            elif "Details not found for RC" in copied_text:
                print(f"RC Number {value} is not valid")
            else:
                df.loc[index, "Mobile_Number"] = None
                print(f"{count}/{total_count} - {value},  - NA")

            one_time = time.perf_counter()
            if count == 1:
                estimate = (one_time - start_time) * total_count
                print(f"Estimated time : {estimate / 60:.1f},minutes")
            elif estimate == 0:
                estimate = (one_time - start_time) * total_count
                print(f"Estimated time : {estimate / 60:.1f},minutes")
            else:
                remaining_time = estimate - (one_time - start_time)
                print(f"Remaining time : {remaining_time / 60:.1f},minutes")
        return df
    except pyautogui.FailSafeException:
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
    df.to_excel(f"backup{output_file_name}")
    print("backup file created")
    # drops all columns with Unnamed or Null name
    # df.columns = [
    #     col if col is not None and "Unnamed" not in str(col) else "drop_column"
    #     for col in df.columns
    # ]
    # df = df.drop(columns=["drop_column"])
    print("output in file", output_file_name)
    eight_digit_cells = find_eight_digit_cells(df)
    if eight_digit_cells:
        df = process_eight_digit_numbers(df, eight_digit_cells, output_file_name)
        if df is not None and not df.empty:
            df.to_excel(output_file_name, index=False)
        else:
            print("DataFrame is empty or invalid, skipping export.")
        # Saving the modified DataFrame to a new Excel file
        # df.to_excel(output_file_name, index=False)  # Output file name
        print(f"Saved to {output_file_name}")
    else:
        print("no 8 digit found")


if __name__ == "__main__":
    main()

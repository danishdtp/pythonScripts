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
def find_12_digit_adhar_cells(df):
    twelve_digit_cells = []
    for index, row in df.iterrows():
        for col in df.columns:
            value = str(row[col])  # Convert to string for checking
            value = value.split(".")[0]
            if len(value) == 12 and value.isdigit():
                twelve_digit_cells.append((index, col, value))
    return twelve_digit_cells


# Step 3: Process each 8-digit number and perform required actions
def process_12digit_number(df, cells, output_file_name):
    total_count = len(df)
    print("Total : ", total_count)
    count = 0
    start_time = time.perf_counter()
    for index, col, value in cells:
        # 1) Copy the 8-digit number to clipboard
        count += 1
        print(f"S.No {count}/{total_count}", end=" ")

        pyperclip.copy(value)
        # 2) Open a website (URL needs to be specified)
        # web_url = (
        #     "https://epos.mp.gov.in/RC_Mobile_Int.jsp"  # Change to the desired URL
        # )
        # pyautogui.hotkey("ctrl", "l")  # Focus address bar
        # time.sleep(0.2)  # Wait for a second
        # pyautogui.write(web_url)
        # pyautogui.press("enter")

        # Wait for the page to load (you may need to adjust this)
        pyautogui.hotkey("home")
        time.sleep(0.2)
        pyautogui.click(x=971, y=307)  # Replace with actual coordinates
        time.sleep(0.2)
        pyautogui.click(x=971, y=307)  # Replace with actual coordinates
        time.sleep(0.2)
        # 3) Paste value in a search field using pyautogui
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.2)
        # pyautogui.write(value)

        # 4) Click on the submit button (coordinates need to be adjusted)
        pyautogui.click(x=1121, y=305)

        # 5) Wait for 2 seconds
        time.sleep(10)
        pyautogui.click(x=1157, y=599)  # Replace with actual coordinates
        # 6) Drag to select the text
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.3)
        # 7) Copy that text
        pyautogui.hotkey("ctrl", "c")
        # 8) Wait a moment for the clipboard to update
        time.sleep(0.3)
        copied_text = pyperclip.paste()

        # 9) Find a 10-digit number in that copied text
        match = re.search(r"\b\d{8}\b", copied_text)
        fps = re.search(r"\b\d{7}\b", copied_text)
        if match:
            found_number = match.group(0)
            df.loc[index, "Samagra"] = found_number
            if fps:
                fps = fps.group(0)
                df.loc[index, "fps"] = fps
            # Add the found digit number into a new column in the DataFrame
            print(f"{count}/{total_count} - {value},  - {found_number}")
        elif "Details not found for" in copied_text:
            print(f"RC Number {value} is not valid")
        else:
            df.loc[index, "Mobile_Number"] = None
            print(f"{count}/{total_count} - {value},  - NA")

        one_time = time.perf_counter()
        global estimate
        if count == 1:
            estimate = (one_time - start_time) * total_count
            print(f"Estimated time : {estimate / 60:.1f},minutes")
        elif count % 10 == 0:
            remaining_time = estimate - (one_time - start_time)
            print(f"Remaining time : {remaining_time / 60:.1f},minutes")
        df.to_excel(output_file_name, index=False)
    return df


# Main function to execute the script
def main():
    file_path = sys.argv[1]  # Provide your Excel file path
    df = load_excel(file_path)
    output_file_name = os.path.basename(file_path)
    df.to_excel(f"backup{output_file_name}")
    print(output_file_name)
    twelve_digit_cells = find_12_digit_adhar_cells(df)
    if twelve_digit_cells:
        df = process_12digit_number(df, twelve_digit_cells, output_file_name)
        # Saving the modified DataFrame to a new Excel file
        df.to_excel(output_file_name, index=False)  # Output file name
        print(f"Saved to {output_file_name}")
    else:
        print("no digit found")


if __name__ == "__main__":
    main()

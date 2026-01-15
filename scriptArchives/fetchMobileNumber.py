import pandas as pd
import pyperclip
import pyautogui
import time
import re
import sys


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
def process_eight_digit_numbers(df, cells):
    total_count = len(df)
    print("Total : ", total_count)
    count = 0
    for index, col, value in cells:
        # 1) Copy the 8-digit number to clipboard
        count += 1
        print(f"S.No {count}/{total_count}", end=" ")

        pyperclip.copy(value)
        # 2) Open a website (URL needs to be specified)
        web_url = (
            "https://epos.mp.gov.in/RC_Mobile_Int.jsp"  # Change to the desired URL
        )
        pyautogui.hotkey("ctrl", "l")  # Focus address bar
        time.sleep(0.2)  # Wait for a second
        pyautogui.write(web_url)
        pyautogui.press("enter")

        # Wait for the page to load (you may need to adjust this)
        time.sleep(2)
        pyautogui.click(x=930, y=332)  # Replace with actual coordinates
        time.sleep(0.2)
        pyautogui.click(x=930, y=332)  # Replace with actual coordinates
        # 3) Paste value in a search field using pyautogui
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        # pyautogui.write(value)

        # 4) Click on the submit button (coordinates need to be adjusted)
        pyautogui.click(x=1122, y=331)  # Replace with actual coordinates

        # 5) Wait for 2 seconds
        time.sleep(2)
        pyautogui.click(x=303, y=747)
        # 6) Drag to select the text
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        # 7) Copy that text
        pyautogui.hotkey("ctrl", "c")

        # 8) Wait a moment for the clipboard to update
        time.sleep(0.5)
        copied_text = pyperclip.paste()

        # 9) Find a 10-digit number in that copied text
        match = re.search(r"\b\d{10}\b", copied_text)
        if match:
            found_number = match.group(0)
            # Add the found digit number into a new column in the DataFrame
            df.loc[index, "Mobile_Number"] = found_number
            print(value, " - ", found_number)
        else:
            df.loc[index, "Mobile_Number"] = None
            print(value, " - NA")

    return df


# Main function to execute the script
def main():
    file_path = sys.argv[1]  # Provide your Excel file path
    df = load_excel(file_path)
    output_file_name = f"{file_path}mobileExtract.xlsx"
    print(output_file_name)
    eight_digit_cells = find_eight_digit_cells(df)
    if eight_digit_cells:
        df = process_eight_digit_numbers(df, eight_digit_cells)
        # Saving the modified DataFrame to a new Excel file
        df.to_excel(output_file_name, index=False)  # Output file name
        print(f"Saved to {output_file_name}")
    else:
        print("no 8 digit found")


if __name__ == "__main__":
    main()

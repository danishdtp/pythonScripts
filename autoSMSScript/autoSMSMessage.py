"""python3 SMS automation script using pyautogui and Microsoft Link to Windows
This script automates SMS sending through PC/Laptop using Microsoft Phone link and Python scripting
The script first takes excel file path as arguments containing columns named
"Mobile Number" and "Message". Mobile number columns containing all the mobile numbers
and Message containing customised message corresponding to each mobile number.
It's important to write columns names with correct spelling.
The user then needs to run this program in terminal/powershell/DOS as following
python3 autoSMSMessage.py path_toexcel.xlsx
After prompt message saying switch to app, the user should switch to Link to Windows app
in 2 seconds.
The line number
The script uses Phone link software in Microsoft so it's limited to work only in MS Windows 11
However suitable changes can be made to automate in other pc sms apps.
"""

import sys
import time
import pandas as pd
import pyautogui
import pyperclip
import os

# Load data - converting all to string and filling empty cells avoids TypeErrors
global file_path
file_path = sys.argv[
    1
]  # Provide your Excel file path in command like python3 % file.xlsx
df = pd.read_excel(file_path).fillna("").astype(str)
output_file_name = os.path.basename(file_path)
df.to_excel(f"backup{output_file_name}")


def run_automation(df):
    pyautogui.FAILSAFE = True
    print("Switch to your target page. Autostarting in 2 seconds...")
    time.sleep(2)
    count = 0
    for index, row in df.iterrows():
        # Correctly accessing single cell values from the row
        count += 1
        if count < 100:
            mobile = row["Mobile Number"]
            message = row["Message"]
            # Step 1: Copy/Paste Mobile Number
            pyautogui.hotkey("ctrl", "n")
            pyperclip.copy(str(mobile))
            time.sleep(0.3)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)

            # Step 2: Navigate to Message field
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)

            # Step 3: Copy/Paste Message
            pyperclip.copy(str(message))
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            print(f"SMS {count} to sent successfully to {mobile} ")
            df = df.drop(index)
            df.to_excel(output_file_name, index=False)
        else:
            print("more than 100 messages sent")
            break


if __name__ == "__main__":
    run_automation(df)

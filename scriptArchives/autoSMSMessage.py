import pyautogui
import pyperclip
import pandas as pd
import time
import sys

# Load data - converting all to string and filling empty cells avoids TypeErrors
file_path = sys.argv[
    1
]  # Provide your Excel file path in command like python3 % file.xlsx
df = pd.read_excel(file_path).fillna("").astype(str)


def run_automation():
    pyautogui.FAILSAFE = True
    print("Switch to your target page. Starting in 5 seconds...")
    time.sleep(1)
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
            time.sleep(1.3)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.3)

            # Step 2: Navigate to Message field
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)

            # Step 3: Copy/Paste Message
            pyperclip.copy(str(message))
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.3)
            # pyautogui.press("enter")
            time.sleep(0.5)

            print(f"SMS {count} to sent successfully to {mobile} ")
        else:
            print("more than 100 messages sent")
            break


if __name__ == "__main__":
    run_automation()

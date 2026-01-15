"""
This script works as a second clipboard
where you can store a specific text which you need to paste
repeatedly, particularly useful when you need to do Ctrl+c and Ctrl+v
for changing value like an id and you need to enter a specific text in it
Steps:
    1.  Change the text in variable 'text' below
    2.  Install dependency - pyautogui
    3.  Test run the script
    4.  Create keyboard shortcut to run it anywhere,
        In Windows, create a shortcut anywhere then specify hotkey in properties
        In Linux, the pyautogui only works in X11 and hotkey depends on desktop type
            If you are using XFCE like me, create a shortcut in Keyboard setting to run
"""

import pyautogui
import time
import pyperclip
import keyboard
import sys

clipboard1 = "समग्र एवं आधार केवाईसी में नाम में अंतर है इस आधार पर निरस्त किया जा रहा है"
clipboard2 = "good night"


def clipboard(text):
    pyautogui.PAUSE = 0.05
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


try:
    while True:
        # Check if Esc key is currently pressed
        if keyboard.is_pressed("pause"):
            print("\npause key detected! Exiting now...")
            sys.exit(0)  # Terminate the script
        elif keyboard.is_pressed("f8"):
            clipboard(clipboard1)
            time.sleep(0.2)
        elif keyboard.is_pressed("f9"):
            clipboard(clipboard2)
            time.sleep(0.2)

        # Optional: Add a very small sleep to reduce CPU usage
        # import time; time.sleep(0.01)

except KeyboardInterrupt:
    # Handles manual Ctrl+C in terminal
    print("\nScript stopped manually.")

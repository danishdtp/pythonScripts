import pyautogui
import time
# import keyboard

print("loop started, press q to stop")
try:
    for i in range(1, 2000, 2):
        pyautogui.click(497, 823)
        pyautogui.click(496, 863)
        pyautogui.click(496, 923)
        pyautogui.click(496, 973)
        pyautogui.click(496, 943)
        pyautogui.click(496, 999)
        time.sleep(2)  # Wait for 2 seconds
        print("clicked")
        time.sleep(0)

        pyautogui.click(962, 700)
        pyautogui.click(962, 706)
        pyautogui.click(962, 716)
        pyautogui.click(962, 722)
        pyautogui.click(962, 736)
        time.sleep(2)
        print("clicked second time")
        time.sleep(0)  # Wait for 3 seconds
        # if keyboard.is_pressed("q"):
        # print("breaking the loop")
        # break
except KeyboardInterrupt:
    print("\nKeyboardInterrupt received, exiting loop")
print("done")

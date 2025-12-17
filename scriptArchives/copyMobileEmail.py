#!python3
# phoneandEmail.py
import pyperclip
import re

# find matches in clipboard text
text = str(pyperclip.paste())
# print(text)
phoneRegex = re.compile(r"\b[6-9]\d{9}\b").findall(text)
# print(phoneRegex)
if phoneRegex == []:
    print("No exact mobile numbers found, searching for other 10 digit characters")
    #    print(text)
    mo = re.compile(r"\d{10}").findall(text)
    if mo == []:
        print("No 10 digit numbers found")
        exit()
    else:
        mobile = mo

else:
    print("Mobile numbers found")
    mobile = phoneRegex
extractedMobile = "\n".join(map("".join, mobile))
#    print(mo)
print(extractedMobile)
print("Copied to clipboard")
pyperclip.copy(extractedMobile)

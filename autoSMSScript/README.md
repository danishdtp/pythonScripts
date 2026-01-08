## Auto SMS Script to automate sending SMS message to 100 mobile numbers from excel file 

The script does following work automatically 
1. Copies mobile number from the filed "Mobile Number" of excel file
2. The script then asks user to open Phone Link
3. In phone link it opens new message, inserts the mobile number
4. Then it copies custom message to be sent to that mobile number from excel file column name "Message" and send that message to particular apps
##Caution :
After execution of each row, the script will delete that row from excel file, so be careful as it may result in your loss of data although backup file is created still repeated wrong use will result in loss of data. So always create manual backup file before running this script. 
## Execution Steps:
1. Download the script file and save in a blank folder.
2. Create an excel file with mobile numbers in `Mobile Number` column header
3. Create your message on a second column with column name `Message`
4. It's important to name the column header correctly otherwise script will not run. You can change header names in script as to your liking.
5. Save the excel file.
6. The script should 
7. Now run script in the terminal as follows :
  `python autoSMSMessage.py "path\to\excelfile.xlsx"`
  or
  `python3 autoSMSMessage.py "path\to\excelfile.xlsx"`

  If you saved both script and excel file in same folder, open Powershell in same folder then run 
  `python autoSMSMessage.py excelfile.xlsx`

8. The script will create backup of first and then ask you to switch to the program, at this point immediately switch to the Phone link app.
9. The script will send sms and console will show the how much 

## Example use cases
1. You need to send custom invitation SMS with name and details specific to each mobile number, just write it in excel file and run this to send them each
2. You need to send custom alert to your customers with their name and order details 
3. You need to send different information to your different colleagues regarding projects.
The only limit  is your imaginations

## 🧑‍💻  Author
Danish Khan, 
Junior Supply Officer, Khandwa

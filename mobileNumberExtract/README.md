
# Mobile Number Extractor Script
For Windows and Linux

## 🛠️ Description

Mobile Number extractor script created in Python which extracts 10 digit mobile number from copied text in clipboard. 
The script is created using regular expressions (regex) which enables super fast execution even when text size is big. 
The script is created with the aim to create a local application which could find and extract mobile number quickly from clipboard without using internet.
Scripts executes in following steps:

* The script first matches exact mobile numbers starting with 6,7,8 and 9.\ 
* If no exact matches are found it then extracts any 10 digit number.\
* If no 10 digit number is found, console shows No mobile number found.\
* This script has been packaged to run on Windows as well as on linux directly.

## ⚙️ Languages or Frameworks Used
The script is supplied in an executable format with dependencies packaged into one for ease of use. The script primarily uses pyperclip for copy paste controls and re for regular expression.\
If you are running source file, you need to install pyperclip alongwith python3. To install pyperclip using pip use following command.\

`pip install pyperclip`


## 💾How to run:

### For Windows 

1. First copy the text that contains the mobile number. It can either be anything plain text, csv, tsv or text in docx, xlsx, pptx, browser anywhere.\
2. Now Download and run `mobileNumExtract.exe` file\
3. The script will extract mobile numbers from the copied text in clipboard and copy the extracted mobile numbers back into the clipboard.\
4. Paste the extracted mobile numbers anywhere you want.

### For Linux

The binary for linux is available as `mobilenumExtractLinux`\
Now, the steps are same, first copy the text, run binary either by double clicking it in file manager or typing\
`./mobileNumExtractLinux` \
The script will find all mobile numbers and copy it into clipboard. Paste the extracted number where you require\

### Source file

1. First clone the repository\
`git clone https://openforge.gov.in/plugins/git/mobile-number-extractor/mobileNumExtract.git`\
2. Now go to the project directory\
`cd mobileNumExtract` \
3. To run the script in python go to and run following in terminal:\
`python mobileNumExtract.py`\
4. To access source code, open python file in any editor or IDE. I use vim editor in terminal, for this use following command
`vim mobileNumExtract.py` \
5. In this file you can see the source code and logic used for the script.

## 📁Sample file to test the script
The project contains an xlsx file named 'sample10digitMobileNumer.xlsx' which has random 10 digit numbers in first column A1. Copy the first column and run the programs as shown in above steps.\
Now paste into the column B at B2, the pasted numbers should be similar to column C. If it's similar it means the program is executed correctly.\
Notice that script excluded number starting from 1 to 5. However if there are no numbers starting with 6 to 9, script will extract all 10 digit numbers

## 🏗 Project structure
.\
├── LICENSE.txt\
├── mobileNumExtract.exe  <-- Executable file for windows\
├── mobileNumExtractLinux <-- Executable binary for Linux\
├── mobileNumExtract.py   <-- Source file\
├── README.html           <-- Readme\
├── README.md\
├── requirement.txt       <-- requirement file\
├── sample10digitMobileNumber.xlsx  <-- sample file for testing\
├── src                   <-- source directory for linux build\
│   ├── build\
│   │   └── mobileNumExtract\
│   ├── dist\
│   │   └── mobileNumExtract\
│   ├── mobileNumExtract.py\
│   └── mobileNumExtract.spec\
└── srcWindows            <-- source directory for Windows build\
├── build\
│   └── mobileNumExtract\
├── dist\
│   └── mobileNumExtract\
└─── mobileNumExtract.spec\

## 💡 Other modification ideas:
The script only extracts text copied into a clipboard, this is by design as many other similar software are available for extracting mobile numbers, however if it's required to extract mobile numbers from dataset file (xlsx,csv,parquet etc.) and output in another file, appropriate modifications in source file mobileNumExtract.py can be done through the use of appropriate libraries like pandas, openpyxl, pyarrow, dask, polars etc.


## 🧑‍💻  Author
Danish Khan, 
Junior Supply Officer, Khandwa

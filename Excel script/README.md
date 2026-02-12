# Useful python scripts to process excel files :

## 1.Format all excel files in the directory :
This python script format all excel file in the directory and does following :
1. Autofit columns
2. Fill border styles
3. Fit page in one page width

### How to run
Copy python script in folder containing excel files
Run script :
`python3 formatExcel.py`
In Windows, you can run the script directly by double clicking it.
In Linux use `chmod +x formatExcel.py` to run it by double clicking it.

## 2. Split Sheets of excel file based on a column value
For this purpose there are two scripts 
1. Libreoffice macro
This is a macro file for Libreoffice, to run this copy the file, first create folders Scripts and python in this location
`%APPDATA%\LibreOffice\4\user\Scripts\python` then copy splitSheetsLOmacro.py in here. Change the column index from where
you want to split the excel in script.\
After this open the excel file go to Tool>Macro>python, The script will be available in My scripts, run from there.
2. splitExcel based on pandas.


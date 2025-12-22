
# Merge Two tables 

## 🛠️ Description
The script is created to match two large csv files and find the rows in the second file not available in first file.\
The script is created using dask and pyarrow libraries of script to handle large data on a low end hardware - home pc or laptop. The script has been tested with 2 GBs of csv file and works instantly.\

## 🛠️Requirements

    1. First table with large data in one csv file, this file will be on left side of left join 
    2. Second table in one csv file, this file rows will be matched with first file.
    3. PC/Laptop with >8 core processors and >16 GB RAM to run the script
    4. MS Windows or Linux operating system with support for python environment
The hardware requirements are of indicative nature. The low end hardware will also run the script successfully albeit with slower processing. I have ran the script on my personal laptop with dual core processor and 4 GB RAM on linux operating system.\
Hence, there are no expensive servers or frameworks are required for this project.\

## ⚙️ Languages or Frameworks Used
Following python libraries are required to be installed\
    * pandas
    * pyarrow
    * dask
    * numpy
    * xlrd
To install using pip run following :\
`pip install pandas numpy xlrd openpyxl dask pyarrow`\

## 💾How to run:
To run the script you need to specify the file names with address into the script. It's easier if both files are present in the same directory/folder as the script.\
After this, run following command in terminal:\
`python MergeTwoTablesFilterColumns.py`

## 💡 Other modification ideas:

## 🧑‍💻  Author
Danish Khan, 
Junior Supply Officer, Khandwa

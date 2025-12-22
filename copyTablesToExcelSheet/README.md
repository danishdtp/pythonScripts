
# Mobile Number Extractor Script
For Windows and Linux

## 🛠️ Description
This script finds all the 8 digit numbers in the copied text and pastes them into the excel sheet. The digit numbers can be changed according to the requirement. It is useful for works where you quickly need to extract numbers from the table, usually online portal and paste them into excel\
With this script you won't even need to have Spreadsheet program installed let alone open the excel or other spreadsheet program. You only need to specify the location of excel file\
Scripts executes in following steps:
- Reads text from the system clipboard
- Finds all distinct 8-digit numbers
- Appends them (one per row) to Sheet2 of the specified Excel .xlsx file

## ⚙️ Languages or Frameworks Used
The scripts uses re,sys,pyperclip,openpyxl,openpyxl.utils. To install pyperclip and openpyxl using pip use following command.\

`pip install pyperclip openpyxl`


## 💾How to run:
    To run the file go to the directory containing the script file 
copyNumbersAndAppendExcel.py and run following commands.\
    `python copyNumbersAndAppendExcel.py /path/to/file.xlsx`\
It is worth noting that we the script has two conditions that can be modified 
    1. The sheet name is fixed to Sheet2, if you want to paste into a specific sheet, write it's name, if name contains space cover it in quotes like 'Sheet 1'
    2. The digits of number are fixed with 8 using regular expression, you can use any kind of regular expressions to match your data.

## 📁Sample file to test the script
The project contains an xlsx file named 'sampleAppendSheet.xlsx' into which you can insert following 8 digit random numbers. Just copy the following numbers and run script as above changing path to that of sdownloaded xls file location (usually Downloads)
    ### List of 8 digit random number to copy into excel 
91444665	\
75289284	\
64342855	\
64797739	\
93760598	\
75437033	\
65565102	\
64616300	\
75496277	\
97747965	\
86703252	\
90728071	\
89237502	\
75394240	\
69530817	\
70882459	\
79272011	\
96497053	\
73206809	\
80571554	\
88698903	\
94374450	\
89225191	\
96523904	\
95183119	\
79458991	\
79700458	\
87958588	\
81581173	\
87761543	\
93832595	\
92193609	\
89436441	\
84042419	\
84202572	\
75316294	\
96754079	\
95257596	\
87427538	\
71092194	\
93535084	\
95947191	\
91417843	\
75495741	\
74490433	\
68254817	\
95471571	\
91429754	\
94451537	\
77522319	\
82054935	\
79303744	\
95540590	\
90308187	\
73718202	\
94199935	\
68213412	\
89901614	\
83781821	\
75413230	\
68050063	\
94605287	\
90072856	\
94197929	\
95397644	\
97741525	\
65772918	\
76157446	\
86814312	\
66443444	\
69728897	\
69354893	\
93617086	\
74214250	\
96914934	\
88151450	\
96849572	\
97284742	\
85632004	\
64688103	\
87437197	\
81422112	\
79581742	\
67419823	\
92661105	\
89068528	\
98003068	\
65621728	\
83336854	\
64343869	\
98028385	\
92699161	\
91997239	\
95638098	\
89602454	\
97143442	\
71490190	\
93619057	\
96681421	\
95592553	\
70818179	\
84976657	\
76907829	\
87873563	\
97574125	\
92399020	\
74561770	\
68854793	\
80049073	\
81890264	\
81045232	\
94243480	\
95866551	\
96573372	\
76382169	\
97103722	\
90422074	\
69226711	\
71417176	\
86529376	\
6917937	\
89583	\

## 🏗 Project structure

## 💡 Other modification ideas:
The script is created specifically to extract a list of numbers of given digits (8 digits which can be modified) and pastes them into excel. However modifications can be made to append any kind of table into the excel

## 🧑‍💻  Author
Danish Khan, 
Junior Supply Officer, Khandwa

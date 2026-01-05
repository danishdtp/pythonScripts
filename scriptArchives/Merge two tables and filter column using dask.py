#SPR AND RCMS data matching script
#Rename SPR file name MP_SPR.csv
#Rename ration card file name to MP_RCMS.csv

import pandas as pd
import xlrd
import openpyxl
import numpy

# making data frame from csv file of MP_RCMS
df = pd.read_csv('MP_RCMS.csv')
df.dropna(subset=['memberid'], inplace=True) 
	# Drop rows where 'memberID' has missing values
df['uniqueid'] = 'id' + df['rationcardid'].astype(str) + df['memberid'].astype(str)
df.to_csv('MP_SPR.csv')

# making data frame from csv file of MP_RCMS
df1 = pd.read_csv('MP_SPR.csv')
df.dropna(subset=['Member ID'], inplace=True)
	# Drop rows where 'Member ID' column has missing values
df1['uniqueid'] = 'id' + df1['Family ID'].astype(str) + df1['Member ID'].astype(str)
df1.to_csv('sprunique.csv')
# Analysis start – left join based on Primary key created above
df = pd.read_csv('rcmsunique.csv')
df1 = pd.read_csv('sprunique.csv')
output1 = pd.merge(df, df1,
                   on='uniqueid',  
                   how='left')
print (output1.head(10)) #prints first 10 lines of output
#output1.to_csv('output.csv')#uncommment to get full output 
print (“Analysis completed”)
output1_filtered = output1[output1['Member Name'].isnull()]
print (“Filtering data completed”)
	#filters the data and outputs the rows with missing members in SPR 
output1_filtered.to_csv(‘notMatchingMembers.csv')
#On successful run, the filtered csv file named  notMatchingMembers.csv
print (output1_filtered.head(10))
#prints first 10 lines on console to check.

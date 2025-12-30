#SPR AND RCMS data matching script
#SPR file name spr.csv
#RCMS file name MPOctRCMS.csv
import pandas as pd

# making data frame from csv file
df = pd.read_csv('reg_farmer.csv')
#df['uniqueid'] = 'id' + df['rationcardid'].astype(str) + df['memberid'].astype(str)
#df.to_csv('rcmsunique.csv')

df1 = pd.read_csv('sprkhandwa2023total.csv')
#df1['uniqueid'] = 'id' + df1['Family ID'].astype(str) + df1['Member ID'].astype(str)
#df1.to_csv('sprunique.csv')

#df = pd.read_csv('rcmsunique.csv')
#df1 = pd.read_csv('sprunique.csv')
output1 = pd.merge(df, df1,
                   on='PortalMemberID',  
                   how='left')
output1.to_csv('output.csv')
#output1_filtered = output1[output1['Member Name'].isnull()]
#print (output1_filtered)
#output1.to_csv('outputfilter.csv')
#output1_filtered.to_csv('outputfilter.csv')
#rationcardid
#memberid

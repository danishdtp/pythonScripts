# python3
# MergeTwoTablesFilterColumns.pyarrow
"""
The script is created to match two large csv files and find the rows in the second file not available in first file.
The script is created using dask and pyarrow libraries of script to handle large data on a low end hardware - home pc or laptop. The script has been tested with 2 GBs of csv file and works instantly.
"""

import dask.dataframe as dd


def process_df(df, id_col, ref_col):
    # Drop rows with missing values and create 'uniqueid'
    df = df.dropna(subset=[id_col])
    df["uniqueid"] = "id" + df["familyid"].astype(str) + df[id_col].astype(str)
    return df[["uniqueid", "familyid", "memberid"]]


# Load and process the first CSV file
df1 = dd.read_csv("rcms.csv")
df1 = process_df(df1, "memberid", "familyid")
# print (df1.head(10))
# Save intermediate result
# df1.to_csv('rcms2-*.csv', index=False, single_file=True)

# Load and process the second CSV file
df2 = dd.read_csv("spr.csv")
df2 = process_df(df2, "memberid", "familyid")
# print (df2.head(10))
# Save intermediate result
# df2.to_csv('spr4-*.csv', index=False, single_file=True)

# Merge the two DataFrames
output1 = dd.merge(df1, df2, on="uniqueid", how="left")

print(output1.head(10))
# Trigger computation to complete the merge and get the filtered result
output1_filtered = output1[output1["memberid_y"].isnull()]

# Show the first 10 rows of the filtered output
print(output1_filtered.head(10))
# Save the final output
output1_filtered.to_csv("notMatchingMembers.csv", index=False, single_file=True)

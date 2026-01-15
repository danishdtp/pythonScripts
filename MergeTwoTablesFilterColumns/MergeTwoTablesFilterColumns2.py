# python3
# MergeTwoTablesFilterColumns.pyarrow
"""
The script is created to match two large csv files and find the rows in the second file not available in first file.
The script is created using dask and pyarrow libraries of script to handle large data on a low end hardware - home pc or laptop. The script has been tested with 2 GBs of csv file and works instantly.
"""

import dask.dataframe as dd

dtype = {
    "Age": "object",
    "Caste": "object",
    "Family ID": "object",
    "Member ID": "object",
    "Mobile No.": "object",
    "S.No": "object",
    "fpscode": "object",
}


def process_df(df, id_col, ref_col):
    # Check if id_col and ref_col exist in the DataFrame
    if str(id_col) not in df.columns or str(ref_col) not in df.columns:
        raise ValueError(
            f"Columns {str(id_col)} or {str(ref_col)} do not exist in the DataFrame."
        )
    # Drop rows with missing values from id_col
    df = df.dropna(subset=[id_col])
    # Create 'uniqueid' by concatenating identifier strings
    df["uniqueid"] = (
        "id" + df[ref_col].astype(str).str.strip() + df[id_col].astype(str).str.strip()
    )

    return df


# Load and process the first CSV file
# df1 = dd.read_csv("sprKhandwa2026Total.csv", low_memory=False, dtype=dtype)
df1 = dd.read_csv("MPrcmsJan2026.csv", low_memory=False, dtype=dtype)
df2 = dd.read_csv("sprKhandwa2026Total.csv", low_memory=False, dtype=dtype)

df1 = process_df(df1, "memberid", "rationcardid")
df2 = process_df(df2, "Member ID", "Family ID")
# print(df1.columns)
# print(df2.columns)
# Save intermediate result
# df2.to_csv('spr4-*.csv', index=False, single_file=True)

print("rcms  number of rows", len(df1))
print("spr number of rows ", len(df2))
# Merge the two DataFrames
output1 = dd.merge(df1, df2, on="uniqueid", how="left")
# output1.to_csv("notMatchingMembers.csv", index=False, single_file=True)
# print("merged ", (df2))
# print(output1.columns)
# print(output1.head(10))
# Trigger computation to complete the merge and get the filtered result
output1_filtered = output1[output1["Member ID"].isnull()]
print("not matching member found = ", len(output1_filtered))

# Show the first 10 rows of the filtered output
# print(output1_filtered.head(10))

# Save the final output
output1_filtered.to_csv("notMatchingMembers.csv", index=False, single_file=True)

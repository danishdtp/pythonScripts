# python3
# MergeTwoTablesFilterColumns.pyarrow
"""
The script is created to match two large csv files and find the rows in the second file not available in first file.
The script is created using dask and pyarrow libraries of script to handle large data on a low end hardware - home pc or laptop. The script has been tested with 2 GBs of csv file and works instantly.
"""

import dask.dataframe as dd
import polars as pl

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
    df = df.drop_nulls(subset=[id_col])
    # Create 'uniqueid' by concatenating identifier strings
    df = df.with_columns(
        uniqueid=pl.concat_str(
            [pl.lit("id"), pl.col(ref_col).fill_null(""), pl.col(id_col).fill_null("")]
        )
    )
    return df


# Load and process the first CSV file
df1 = pl.read_csv("RCMSKhandwaJan2026.csv", encoding="utf8-lossy").drop_nulls()
temp_df = pl.read_csv("sprKhandwa2026Total.csv", n_rows=0, infer_schema_length=0)
all_strings = {col: pl.String for col in temp_df.columns}
df2 = pl.read_csv(
    "sprKhandwa2026Total.csv", encoding="utf8-lossy", schema_overrides=all_strings
)
df1 = process_df(df1, "memberid", "rationcardid")
print(df1.schema)
print(len(df1))
df2 = process_df(df2, "Member ID", "Family ID")
print(df2.schema)
print(len(df2))
# Save intermediate result
# df2.to_csv('spr4-*.csv', index=False, single_file=True)

# print("rcms  number of rows", len(df1))
# print("spr number of rows ", len(df2))
# Merge the two DataFrames
# output1 = dd.merge(df1, df2, on="uniqueid", how="left")
output2 = df1.join(df2, on="uniqueid", how="left", nulls_equal=True)
# output1.to_csv("notMatchingMembers.csv", index=False, single_file=True)

# print("merged ", (df2))
# print(output1.head(10))

print(output2.schema)
print("output", len(output2))

# output2.write_csv("filtered.csv")

# Trigger computation to complete the merge and get the filtered result
output2_filtered = output2.filter(pl.col("Member ID").is_null())
# output2_filtered = output2_filtered.filter(pl.col("Family ID").is_nan())
print(output2_filtered.schema)
print("filter", len(output2_filtered))

# print(output2_filtered.head)
# print(output2_filtered.head)
# Show the first 10 rows of the filtered output

output2_filtered.write_csv("filtered.csv")
# Save the final output

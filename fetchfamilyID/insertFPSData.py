import pandas as pd
import sys
import os


# Step 1: Load the Excel file into a DataFrame
def load_excel(file_path):
    return pd.read_excel(file_path)


def findinRC(df, dfFPS, output_file_name):
    merged_df = pd.merge(
        df, dfFPS[["fpscode", "rationcardid"]], on="rationcardid", how="left"
    )
    merged_df = merged_df.drop_duplicates(subset=["consumerno"], keep="first")
    merged_df.to_excel(output_file_name, index=False)  # Output file name


def findinFPSdata(df, dfFPS, output_file_name):
    merged_df = pd.merge(
        df,
        dfFPS[["Block", "fpscode", "fpsname", "Salesman", "Mobile_Number"]],
        on="fpscode",
        how="left",
    )
    merged_df = merged_df.drop_duplicates(subset=["consumerno"], keep="first")
    merged_df.to_excel(output_file_name, index=False)  # Output file name


def main():
    file_path = sys.argv[1]  # Provide your Excel file path
    df = load_excel(file_path)
    df.columns.str.strip()
    print(df.head(10))
    dfRC = pd.read_csv("khandwa.csv")
    dfFPS = load_excel("fpsMasterList.xlsx")
    dfFPS.columns.str.strip()
    print(dfFPS.head(10))
    output_file_name = f"analysis{os.path.basename(file_path)}"
    print(output_file_name)
    # findinRC(df, dfRC, output_file_name)
    findinFPSdata(df, dfFPS, output_file_name)


if __name__ == "__main__":
    main()

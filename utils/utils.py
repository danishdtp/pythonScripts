import polars as pl
#process dataframe using single id cell, appends 'id' string to id cell

def process_df_single(df, id_col)-> pl.DataFrame:
    # Check if id_col and ref_col exist in the DataFrame
    if str(id_col) not in df.columns:
        raise ValueError(f"Columns {str(id_col)} not exist in the DataFrame.")
    # Drop rows with missing values from id_col
    df = df.drop_nulls(subset=[id_col])
    # Create 'uniqueid' by concatenating identifier strings
    df = df.with_columns(
        uniqueid=pl.concat_str(
            [
                pl.lit("id"),
                pl.col(id_col).fill_null("").str.strip_chars(),
            ]
        )
    )
    return df
#process dataframe using single id cell, concatenates'id' string to id and ref cells
def process_df(df, id_col, ref_col) -> pl.DataFrame:
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
            [
                pl.lit("id"),
                pl.col(ref_col).fill_null("").str.strip_chars(),
                pl.col(id_col).fill_null("").str.strip_chars(),
            ]
        )
    )
    return df
import pandas as pd

# read clipboard (assumes tabular data copied, use sep if needed)
df = pd.read_clipboard(header=None)  # header=None since no header

# set the indices for the four columns (replace with your actual indices)
name_idx, total_idx, workdone_idx, pct_idx = 1, 3, 13, 14

# select columns by position and rename
df2 = df.iloc[:, [name_idx, total_idx, workdone_idx, pct_idx]].copy()
df1.columns = ["Name", "Total", "Completed", "Per%"]

# ensure percentage is numeric
df2["Per%"] = pd.to_numeric(df2["Per%"], errors="coerce")

#sorting ascending and taking bottom 20 values
bottom20 = df2.sort_values("Per%", ascending=True).head(20).reset_index(drop=True)
#sorting descending and taking top 20 values
top20 = df2.sort_values("Per%", ascending=False).head(20).reset_index(drop=True)
#Insert serial number column
bottom20.insert(0, "SNo", bottom20.index + 1)
top20.insert(0, "SNo", bottom20.index + 1)

# show result
print("Result :") 
print("Bottom 20:") 
print(bottom20)
print("Top 20 :") 
print(top20)
#copying bottom 20 to clipboard
bottom20.to_clipboard()
#if you want to copy top 20 uncomment following
#top20.to_clipboard()


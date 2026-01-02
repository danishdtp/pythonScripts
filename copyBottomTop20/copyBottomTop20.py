#!/usr/bin/env python3
#copies bottom or top 20 rows from copied table data in clipboard 
#the script requires the columns numbers to be manually specified in line before df2. 
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -- %(message)s")
logging.debug("Start of program")
# read clipboard (assumes tabular data copied, use sep if needed)
df = pd.read_clipboard(header=None)  # header=None since no header

# set the indices for the four columns (replace with your actual indices)
name_idx, total_idx, workdone_idx, pct_idx = 1, 3, 13, 14

# select columns by position and rename
df2 = df.iloc[:, [name_idx, total_idx, workdone_idx, pct_idx]].copy()

df2.columns = ["दुकान", "कुल", "वितरण", "Per%"]

# ensure percentage is numeric
df2["Per%"] = pd.to_numeric(df2["Per%"], errors="coerce")
logging.debug("changed to numeric")

bottom20 = df2.sort_values("Per%", ascending=True).head(20).reset_index(drop=True)
# logging.debug(bottom20)
top20 = df2.sort_values("Per%", ascending=False).head(20).reset_index(drop=True)
# logging.debug(top20)
# bottom20 = df2[df2["Per%"] <= cutoff].sort_values("Per%", ascending=True)
# Option B: exactly 20% of rows by count
bottom20.insert(
    0,
    "सक्",
    bottom20.index + 1,
)
top20.insert(0, "सक्", bottom20.index + 1)
columns_to_combine = ["दुकान", "कुल", "वितरण", "Per%"]
bottom20["FPS -------- Total --- Vitran --- %"] = (
    bottom20[columns_to_combine].astype(str).apply(" --- ".join, axis=1)
)

# show result
print("कम वितरण्  वाली दुकानें")
print(bottom20)  # or bottom20_bycount
print("top 20")
print(top20)
# print(bottom20_bycount)
bottom20["FPS -------- Total --- Vitran --- %"].to_clipboard()
# top20.to_clipboard()

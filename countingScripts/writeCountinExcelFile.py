import re
import pandas as pd

df = pd.read_csv("jpkhandwa.csv")
count = 0
df["count"] = df.groupby("samagra")["samagra"].transform("count")
df["cumu_count"] = df.groupby("samagra")["samagra"].cumcount() + 1

print(df.head(10))
df.to_csv("jpkhandwa.csv", index=False)

# Requires: pandas
# Install: pip install pandas
import sys
import pandas as pd
import pyperclip
def read_clipboard_as_series():
    try:
        df = pd.read_clipboard(header=None)  # read whatever is in clipboard
    except Exception as e:
        print(f"Error reading clipboard: {e}", file=sys.stderr)
        sys.exit(1)

    # Flatten to a single series of values (preserve strings as-is)
    if df.empty:
        print("Clipboard is empty", file=sys.stderr)
        sys.exit(1)
    ser = df.stack().astype(str).reset_index(drop=True)
    return ser

def count_values(series):
    counts = series.value_counts()
    return counts

def main():
    ser = read_clipboard_as_series()
    lines = []
#    print (ser)
    counts = count_values(ser)
#    print (counts)
    # Find max and min counts
    max_count = counts.max()
    min_count = counts.min()
#    print (max_count)
    # Values (could be multiple) with those counts
    max_values = counts[counts == max_count].index.tolist()
    min_values = counts[counts == min_count].index.tolist()
#    print("Max count:", max_count , max_values)
#    print("Min count:", min_count, min_values)
    print(max_count)
    for i in range(max_count):
        num = counts[counts==(i+1)].index.tolist()
        print('Count',(i+1),'is',num )
       # print (max_count)
        lines.append(('Count',(i+1),'is',num))          # replace with your loop work
       # print (lines)
    output = "\n".join(str(item) for item in lines)
    #output = "\n".join(lines)               # or "".join(...) or any format
    pyperclip.copy(output)
    print("Copied to clipboard")


if __name__ == "__main__":
    main()

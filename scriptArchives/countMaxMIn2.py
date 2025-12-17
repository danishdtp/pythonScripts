from collections import Counter
import pyperclip
import sys

text = pyperclip.paste()
#print (text)
lines = [line.strip() for line in text.splitlines() if line.strip()]

if not lines:
    msg = "Error: clipboard is empty or contains only blank lines."
    print(msg)
    pyperclip.copy(msg)
    sys.exit(1)

counts = Counter(lines)
max_key, max_count = max(counts.items(), key=lambda kv: kv[1])
min_key, min_count = min(counts.items(), key=lambda kv: kv[1])

result = f"Max: {max_key} — {max_count} occurrences\nMin: {min_key} — {min_count} occurrence"
print(result)
pyperclip.copy(result)


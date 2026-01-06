import pyperclip

# Retrieve the copied list from the clipboard
copied_list = pyperclip.paste().splitlines()


# Function to count occurrences
def count_occurrences(input_list):
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


# Counting occurrences
item_counts = count_occurrences(copied_list)
sorted_item_counts = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)

# Outputting the counts
# for item, count in item_counts.items():
# print(f"{item}: {count}")
# Sorted output
for item, count in sorted_item_counts:
    print(f"{item}: {count}")

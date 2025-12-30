import time
import random


def insertion_sort(arr):
    # Traverse through 1 to len(arr) (start from the second element)
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place the key at its correct position


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and split the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call merge_sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the temp arrays back into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
data = [38, 27, 43, 3, 9, 82, 10]
merge_sort(data)
print(f"Sorted array: {data}")


# Example usage:
start_time = time.perf_counter()
# my_list = [random.randrange(1, 10000000000000000000, 1) for _ in range(100000)]
my_list = [random.randint(1, 20000) for _ in range(100000)]
merge_list = my_list[:]
print("random number generated")
print("starting merge sort")
merge_sort(merge_list)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"time taken {elapsed_time:.4f} second")
print("starting insertion sort")

insertion_sort(my_list)
# print("Sorted array:", my_list)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"time taken {elapsed_time:.4f} second")
start_time = time.perf_counter()
# Output: Sorted array: [5, 6, 11, 12, 13]

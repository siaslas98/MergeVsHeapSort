# timsort implementation
# How this algorithm works in a nutshell
# Divide the array into runs (small chunks), sort them with binary insertion sort, then merge\
# Time complexities:
# Best case: O(n), Average case: O(n log n), Worst case: O(n log n)

def binary_search(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return left


def binary_insertion_sort(arr, left, right):
    # O(n^2) complexity, but because the array is always 32 elements overall time complexity isn't
    # impacted significantly
    # skip first element, already sorted
    for i in range(left + 1, right + 1):
        key = arr[i]
        position = binary_search(arr, left, i - 1, key)
        for j in range(i, position, -1):
            arr[j] = arr[j - 1]
        arr[position] = key


def merge(arr, left, mid, right):
    array_one_length = mid - left + 1
    array_two_length = right - mid
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < array_one_length and j < array_two_length:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < array_one_length:
        arr[k] = left_array[i]
        k += 1
        i += 1

    while j < array_two_length:
        arr[k] = right_array[j]
        k += 1
        j += 1


def timsort(arr):
    # run size, subject to change
    run_size = 32
    array_length = len(arr)

    # splitting array
    for start in range(0, array_length, run_size):
        end = min(start + run_size - 1, array_length - 1)
        binary_insertion_sort(arr, start, end)

    size = run_size
    while size < array_length:
        for left in range(0, array_length, 2 * size):
            mid = min(array_length - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_length - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


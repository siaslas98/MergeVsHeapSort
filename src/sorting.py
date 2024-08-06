import pygame as pg
from box import Box
from node import Node
from bars import *
from draw import *


''' Heap building in place'''


def heapify(sort_info, parent, comparator, n):

    arr = sort_info.list

    largest = parent
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    # Check if left child exists and is greater than root
    if left_child < n and comparator(arr[left_child]) > comparator(arr[largest]):
        largest = left_child

    # Check if right child exists and is greater than largest so far
    if right_child < n and comparator(arr[right_child]) > comparator(arr[largest]):
        largest = right_child

    # If largest is not root
    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]  # Swap
        heapify(sort_info, largest, comparator, n)


def build_heap(sort_info, comparator, n):
    for idx in range(n // 2 - 1, -1, -1):
        heapify(sort_info, idx, comparator, n)


def extract_max(sort_info, comparator, n):
    arr = sort_info.list
    for idx in range(n-1, 0, -1):
        arr[0], arr[idx] = arr[idx], arr[0]  # Swap

        n -= 1

        heapify(sort_info, 0, comparator, n)


def heap_sort(sort_info, comparator):
    n = len(sort_info.list)
    build_heap(sort_info, comparator, n)
    extract_max(sort_info, comparator, n)


''' End of Heap building in place'''


''' Heap sort using heap insert: 
    This is less efficient than the in-place sorting
    Please Ignore as this will not be used '''


def heap_sort2(heap, sort_info):
    while heap.size > 0 and sort_info.sort and not sort_info.lst_sorted:
        heap.extract(sort_info)

    if sort_info.ascending:
        sort_info.list = heap.sorted_arr
    else:
        sort_info.list = heap.sorted_arr[::-1]

    sort_info.sort = False


''' Tim Sort '''


def binary_insertion_sort(sort_info, start, end, comparator):
    arr = sort_info.list
    for i in range(start + 1, end + 1):
        key = arr[i]
        left = start
        right = i - 1

        while left <= right:
            mid = (left + right) // 2
            if comparator(key) < comparator(arr[mid]):
                right = mid - 1
            else:
                left = mid + 1

        for j in range(i, left, -1):
            arr[j] = arr[j-1]
        arr[left] = key


def merge(arr, left, mid, right, comparator):
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if comparator(left_array[i]) <= comparator(right_array[j]):
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        arr[k] = left_array[i]
        k += 1
        i += 1

    while j < len(right_array):
        arr[k] = right_array[j]
        k += 1
        j += 1


def timsort(sort_info, comparator):
    arr = sort_info.list
    n = len(arr)

    # Split array into runs and sort each run using binary insertion sort
    for start in range(0, n, MIN_RUN_SIZE):
        end = min(start + MIN_RUN_SIZE - 1, n - 1)
        binary_insertion_sort(sort_info, start, end, comparator)

    size = MIN_RUN_SIZE
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right, comparator)

        size *= 2

    sort_info.sort = False




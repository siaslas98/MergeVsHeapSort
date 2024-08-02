import pygame as pg
from box import Box
from node import Node
from bars import *
from draw import *
from typing import List
from constants import *
from calculations import *


''' Heap building in place'''


def heapify(screen, sort_info, parent, root_pos, clock, steps=20):
    from main import draw_heap

    largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2

    # Check if left child exists and is greater than root
    if left < n and sort_info.nodes[left].val > sort_info.nodes[largest].val:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and sort_info.nodes[right].val > sort_info.nodes[largest].val:
        largest = right

    # If largest is not root
    if largest != parent:

        # Slide values into their new positions
        slide_values(screen, sort_info, parent, largest, steps, clock)

        sort_info.nodes[parent].val, sort_info.nodes[largest].val = sort_info.nodes[largest].val, sort_info.nodes[parent].val  # Swap

        # Swap values in the boxes
        parent_box = None
        largest_box = None
        for box in sort_info.boxes:
            if box.idx == parent:
                parent_box = box
            elif box.idx == largest:
                largest_box = box
        if parent_box and largest_box:
            parent_box.update_val(sort_info.nodes[parent].val)
            largest_box.update_val(sort_info.nodes[largest].val)

        # Visualize the swap
        draw_heap(screen, sort_info, highlight={parent, largest})
        pg.display.update()
        clock.tick(60)

        # Recursively heapify the affected subtree
        heapify(screen, sort_info, largest, root_pos, clock)


def build_heap(screen, sort_info, root_pos, clock):
    for idx in range(n // 2 - 1, -1, -1):
        heapify(screen, sort_info, idx, root_pos, clock)
        # Visualize the heap after each heapify call

    sort_info.list = [node.val for node in sort_info.nodes]


''' End of Heap building in place'''


''' Heap sort using heap insert'''


def heap_sort(heap, sort_info):
    while heap.size > 0 and sort_info.sort and not sort_info.lst_sorted:
        heap.extract(sort_info)

    if sort_info.ascending:
        sort_info.list = heap.sorted_arr
    else:
        sort_info.list = heap.sorted_arr[::-1]

    sort_info.sort = False


''' Tim Sort '''


def binary_search(arr, left, right, key, comparator):
    while left <= right:
        mid = left + (right - left) // 2
        if comparator(arr[mid]) == comparator(key):
            return mid + 1
        elif comparator(arr[mid]) < comparator(key):
            left = mid + 1
        else:
            right = mid - 1

    return left


def binary_insertion_sort(arr, left, right, comparator, sort_info, screen, run_idx, runs, run_colors):
    color = RUN_COLORS[run_idx % len(RUN_COLORS)]
    run_colors.append(color)
    for i in range(left + 1, right + 1):
        key = arr[i]
        position = binary_search(arr, left, i - 1, key, comparator)
        for j in range(i, position, -1):
            arr[j] = arr[j - 1]
        arr[position] = key

        # Update the runs with the current state of the array
        current_runs = runs + [arr[left:i + 1]]  # Add the current run being processed
        min_stock = min(arr[left:right + 1], key=comparator)
        max_stock = max(arr[left:right + 1], key=comparator)
        bars = get_bars_timsort(current_runs, arr[i + 1:], SIDE_PAD, min_stock, max_stock, sort_info.selected_attribute, run_colors)
        if not sort_info.ascending:
            bars = bars[::-1]
        draw(screen, sort_info, bars)
        pg.display.update()
        pg.time.delay(50)

    runs.append(arr[left:right + 1])


def merge(arr, left, mid, right, comparator, sort_info, screen, run_idx, runs, run_colors):
    color = RUN_COLORS[run_idx % len(RUN_COLORS)]
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    new_run = []

    # Initial visualization of the runs before merging
    runs_to_visualize = [left_array, right_array]
    visualize_merge_step(screen, sort_info, runs_to_visualize, arr[right + 1:], comparator)

    while i < len(left_array) and j < len(right_array):
        if comparator(left_array[i]) <= comparator(right_array[j]):
            arr[k] = left_array[i]
            new_run.append(left_array[i])
            i += 1
        else:
            arr[k] = right_array[j]
            new_run.append(right_array[j])
            j += 1
        k += 1

        # Visualize the current state of the merging process
        runs_to_visualize = [left_array[i:], right_array[j:], new_run]
        visualize_merge_step(screen, sort_info, runs_to_visualize, arr[right + 1:], comparator)

    while i < len(left_array):
        arr[k] = left_array[i]
        new_run.append(left_array[i])
        k += 1
        i += 1

        # Visualize the current state of the merging process
        runs_to_visualize = [left_array[i:], new_run]
        visualize_merge_step(screen, sort_info, runs_to_visualize, arr[right + 1:], comparator)

    while j < len(right_array):
        arr[k] = right_array[j]
        new_run.append(right_array[j])
        k += 1
        j += 1

        # Visualize the current state of the merging process
        runs_to_visualize = [right_array[j:], new_run]
        visualize_merge_step(screen, sort_info, runs_to_visualize, arr[right + 1:], comparator)

    # Update the runs and run colors
    runs.append(new_run)
    run_colors.append(color)
    runs[:] = [run for run in runs if run not in [left_array, right_array]]
    if runs:
        visualize_merge_step(screen, sort_info, runs, arr[right + 1:], comparator, final=True)


def timsort(arr, comparator, sort_info, screen):
    array_length = len(arr)
    run_idx = 0
    runs = []
    runs_colors = []

    # Draw initial array
    bars = get_bars_timsort([arr], [], SIDE_PAD, min(arr, key=comparator), max(arr, key=comparator), sort_info.selected_attribute, [RUN_COLORS[run_idx % len(RUN_COLORS)]])
    if not sort_info.ascending:
        bars = bars[::-1]
    draw(screen, sort_info, bars)
    pg.display.update()
    pg.time.delay(1000)  # Delay to show the initial array

    # split array
    for start in range(0, array_length, MIN_RUN_SIZE):
        end = min(start + MIN_RUN_SIZE - 1, array_length - 1)
        binary_insertion_sort(arr, start, end, comparator, sort_info, screen, run_idx, runs, runs_colors)
        run_idx += 1

    size = MIN_RUN_SIZE
    while size < array_length:
        for left in range(0, array_length, 2 * size):
            mid = min(array_length - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_length - 1))

            if mid < right:
                merge(arr, left, mid, right, comparator, sort_info, screen, run_idx, runs, runs_colors)
                run_idx += 1

        size *= 2

    # Draw final sorted array

    bars = get_bars_timsort([arr], [], SIDE_PAD, min(arr, key=comparator), max(arr, key=comparator), sort_info.selected_attribute, [RUN_COLORS[run_idx % len(RUN_COLORS)]])
    if not sort_info.ascending:
        bars = bars[::-1]
    draw(screen, sort_info, bars)
    pg.display.update()
    pg.time.delay(1000)  # Delay to show the final sorted array

    sort_info.sort = False
    sort_info.list = arr

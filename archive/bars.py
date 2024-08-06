import pygame as pg
from constants import *


def calc_parameters(total_len):
    parameters = {
        "side_pad": round(TOTAL_SIDE_PAD / 2),
        "top_pad": TOP_PADDING,
        "bottom_pad": WINDOWSIZE[1] - sorting_bottom,
        "bar_width": (WINDOWSIZE[0] - TOTAL_SIDE_PAD) / total_len,
        "vert_space": (WINDOWSIZE[1] - TOP_PADDING) - (WINDOWSIZE[1] - sorting_bottom)
    }
    return parameters


def get_bars_heapsort(sorted_lst, unsorted_lst, unsorted_start_x, u_min_stock, u_max_stock, attribute, new_element_idx=None, color=None):
    if not sorted_lst and not unsorted_lst:  # Ensure the array is not empty
        return []
    bar_list = []

    p = calc_parameters(len(sorted_lst) + len(unsorted_lst))

    attribute = attribute.lower()
    u_min_val = getattr(u_min_stock, attribute)
    u_max_val = getattr(u_max_stock, attribute)

    diff = u_max_val - u_min_val
    if diff == 0:
        diff = 1
    bar_unit = p['vert_space'] / diff

    for i, stock in enumerate(sorted_lst):
        attribute_value = getattr(stock, attribute)
        n_height = (attribute_value - u_min_val) / diff  # Normalized Height
        s_height = n_height * (p['vert_space'] - 10)  # Scaled Height
        rect = pg.Rect(p['side_pad'] + i * p['bar_width'], 0, p['bar_width'], s_height)
        rect.bottom = sorting_bottom
        bar_list.append((rect, color if color else UNSORTED[i % 3]))

    for i, stock in enumerate(unsorted_lst):
        attribute_value = getattr(stock, attribute)
        if unsorted_lst[i] not in sorted_lst:
            n_height = (attribute_value - u_min_val) / diff
            s_height = n_height * (p['vert_space'] - 10)
            rect = pg.Rect(unsorted_start_x + i * p['bar_width'], 0, p['bar_width'], s_height)
            rect.bottom = sorting_bottom
            bar_list.append((rect, color if color else UNSORTED[i % 3]))

    return bar_list


def get_bars_timsort(runs, unsorted_lst, unsorted_start_x, u_min_stock, u_max_stock, attribute, run_colors):
    if not runs and not unsorted_lst:  # Ensure the array is not empty
        return []

    bar_list = []

    total_len = sum(len(run) for run in runs if isinstance(run, list)) + len(unsorted_lst)
    if total_len == 0:
        return []

    p = calc_parameters(total_len)

    attribute = attribute.lower()
    u_min_val = getattr(u_min_stock, attribute)
    u_max_val = getattr(u_max_stock, attribute)

    diff = u_max_val - u_min_val
    if diff == 0:
        diff = 1
    bar_unit = p['vert_space'] / diff

    x_offset = p['side_pad']

    for run_idx, run in enumerate(runs):
        for stock in run:
            attribute_value = getattr(stock, attribute)
            n_height = (attribute_value - u_min_val) / diff  # Normalized Height
            s_height = n_height * (p['vert_space'] - 10)  # Scaled Height
            rect = pg.Rect(x_offset, 0, p['bar_width'], s_height)
            rect.bottom = sorting_bottom
            bar_list.append((rect, run_colors[run_idx]))
            x_offset += p['bar_width']

    for stock in unsorted_lst:
        attribute_value = getattr(stock, attribute)
        n_height = (attribute_value - u_min_val) / diff
        s_height = n_height * (p['vert_space'] - 10)
        rect = pg.Rect(x_offset, 0, p['bar_width'], s_height)
        rect.bottom = sorting_bottom
        bar_list.append((rect, UNSORTED[0]))
        x_offset += p['bar_width']

    return bar_list


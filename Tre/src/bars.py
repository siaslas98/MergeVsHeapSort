import pygame as pg
from constants import *
from heap import *


def calc_parameters(total_len):
    parameters = {
        "side_pad": round(TOTAL_SIDE_PAD / 2),
        "top_pad": TOP_PADDING,
        "bottom_pad": WINDOWSIZE[1] - sorting_bottom,
        "bar_width": (WINDOWSIZE[0] - TOTAL_SIDE_PAD) / total_len,
        "vert_space": (WINDOWSIZE[1] - TOP_PADDING) - (WINDOWSIZE[1] - sorting_bottom)
    }
    return parameters


def get_bars(sorted_lst, unsorted_lst, unsorted_start_x, u_min_val, u_max_val):
    if not sorted_lst and not unsorted_lst:  # Ensure the array is not empty
        return []
    bar_list = []

    p = calc_parameters(len(sorted_lst) + len(unsorted_lst))

    diff = u_max_val - u_min_val
    if diff == 0:
        diff = 1
    bar_unit = p['vert_space'] / diff

    length = len(sorted_lst)
    for i in range(length):
        n_height = (sorted_lst[i] - u_min_val) / diff  # Normalized Height
        s_height = n_height * (p['vert_space'] - 10)  # Scaled Height
        rect = pg.Rect(p['side_pad'] + i * p['bar_width'], 0, p['bar_width'], s_height)
        rect.bottom = sorting_bottom
        bar_list.append(rect)

    length = len(unsorted_lst)
    for i in range(length):
        if unsorted_lst[i] not in sorted_lst:
            n_height = (unsorted_lst[i] - u_min_val) / diff
            s_height = n_height * (p['vert_space'] - 10)
            rect = pg.Rect(unsorted_start_x + i * p['bar_width'], 0, p['bar_width'], s_height)
            rect.bottom = sorting_bottom
            bar_list.append(rect)

    return bar_list


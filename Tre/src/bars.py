import pygame as pg

# Constants
WINDOWSIZE = (800, 600)
TOTAL_SIDE_PAD = 100
TOP_PADDING = 100
sorting_bottom = 550
BG_COLOR = (30, 30, 30)
BAR_COLOR = (100, 200, 200)
SORTED_BAR_COLOR = (100, 200, 100)

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
    if not sorted_lst and not unsorted_lst:
        return []
    bar_list = []

    p = calc_parameters(len(sorted_lst) + len(unsorted_lst))

    diff = u_max_val - u_min_val
    if diff == 0:
        diff = 1
    bar_unit = p['vert_space'] / diff

    for i, (name, value) in enumerate(sorted_lst):
        n_height = (value - u_min_val) / diff
        s_height = n_height * (p['vert_space'] - 10)
        rect = pg.Rect(p['side_pad'] + i * p['bar_width'], 0, p['bar_width'], s_height)
        rect.bottom = sorting_bottom
        bar_list.append((rect, SORTED_BAR_COLOR))

    for i, (name, value) in enumerate(unsorted_lst):
        if (name, value) not in sorted_lst:
            n_height = (value - u_min_val) / diff
            s_height = n_height * (p['vert_space'] - 10)
            rect = pg.Rect(unsorted_start_x + i * p['bar_width'], 0, p['bar_width'], s_height)
            rect.bottom = sorting_bottom
            bar_list.append((rect, BAR_COLOR))

    return bar_list

def draw_bars(screen, bars):
    screen.fill(BG_COLOR)
    for rect, color in bars:
        pg.draw.rect(screen, color, rect)
    pg.display.flip()
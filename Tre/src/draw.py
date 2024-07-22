import pygame as pg
from constants import *

def draw_bars(screen, bars, new_ele_idx=None):
    for i, bar in enumerate(bars):
        if i == new_ele_idx:
            color = (255, 0, 0)
        else:
            color = UNSORTED[i % 3]

        pg.draw.rect(screen, color, bar)
        pg.draw.rect(screen, 'Blue', bar, 2)
def draw(screen, buttons_group, bars, new_ele_idx=None):
    screen.fill(BACKGROUND_COLOR)
    pg.draw.rect(screen, (169, 173, 76), (0, 0, WINDOWSIZE[0], sorting_bottom + 4), 4, 1)
    pg.draw.line(screen, (169, 173, 76), (0, 100), (1800, 100), 4)
    screen.blit(basic_controls, (controls_x, 5))
    screen.blit(sort_controls, (controls_x, 35))
    buttons_group.update(FONT2, TEXT_COLOR1)
    draw_bars(screen, bars, new_ele_idx)
import pygame as pg
from constants import *

def draw_bars(screen, bars):
    for i, bar in enumerate(bars):
        pg.draw.rect(screen, UNSORTED[i % 3], bar)
        pg.draw.rect(screen, 'Blue', bar, 2)
def draw(screen, buttons_group, bars):
    screen.fill(BACKGROUND_COLOR)
    pg.draw.rect(screen, (169, 173, 76), (0, 0, WINDOWSIZE[0], sorting_bottom + 4), 4, 1)
    pg.draw.line(screen, (169, 173, 76), (0, 100), (1800, 100), 4)
    screen.blit(basic_controls, (controls_x, 5))
    screen.blit(sort_controls, (controls_x, 35))
    buttons_group.update(FONT2, TEXT_COLOR1)
    draw_bars(screen, bars)
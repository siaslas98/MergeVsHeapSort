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

def draw_buttons(screen, buttons_group):
    buttons_group.update(Button_Font, Colors.get_color('black'))       

def draw_background(screen):
    background_image = pg.image.load('Background/Cash.jpg').convert()
    scaled_background = pg.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_background, (0, 0))


def draw(screen, buttons_group, Category=None, bars=None, new_ele_idx=None):
    background_image = pg.image.load('Background/Cash.jpg').convert()

    if Category == 'Visuals':
        draw_background(screen)
        pg.draw.rect(screen, (169, 173, 76), (0, 0, WINDOWSIZE[0], sorting_bottom + 4), 4, 1)
        pg.draw.line(screen, (169, 173, 76), (0, 100), (1800, 100), 4)
        draw_bars(screen, bars, new_ele_idx)
        draw_buttons(screen, buttons_group)
    elif Category == 'Menu':
        draw_background(screen)
        draw_buttons(screen, buttons_group)
        screen.blit(Menu_Title, Menu_Title_Position)
        screen.blit(Menu_Tips, Menu_Tips_Position)
    elif Category == 'Analyze':
        draw_background(screen)
        draw_buttons(screen, buttons_group)
    else:
        draw_background(screen)
        draw_buttons(screen, buttons_group)

        
        


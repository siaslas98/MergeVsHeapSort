import pygame as pg
from constants import *
import sys
import random
from load_data import load_data
from images import *
from button import *
from bars import *
from box import *
from node import Node
from heap import Heap
from sorting import *
from draw import *
from calculations import *
from stock import *


class SortInfo:
    def __init__(self):
        self.sort = False
        self.click = False
        self.lst_sorted = False
        self.selected_order = None
        self.selected_attribute = None
        self.top_5 = [0, 0, 0, 0, 0]
        self.date = ""
        self.list = []  # List  of stock data objects to perform sorting on
        self.heap_timer = None
        self.timsort_timer = None
        self.images = Images()
        self.menu_buttons_group = pg.sprite.Group()
        self.sort_buttons_group = pg.sprite.Group()
        self.order_buttons_group = pg.sprite.Group()
        self.attribute_buttons_group = pg.sprite.Group()
        self.analyze_buttons_group = pg.sprite.Group()
        self.input_box_group = pg.sprite.Group()
        self.heap = None
        self.bars = None
        self.sort_dropdown_expanded = False
        self.order_dropdown_expanded = False
        self.attribute_dropdown_expanded = False


def initialize_pygame():
    pg.init()
    screen = pg.display.set_mode(WINDOWSIZE)
    pg.display.set_caption("Sorting Stock Data")
    return screen


def gen_starting_list(sort_info):
    sort_info.list = [generate_random_stock(company_names[i]) for i in range(n)]  # n == 100000


# Reference button.py for more info
def gen_menu_buttons(screen, sort_info):
    main_buttons = [
        ('Order', ORDER_BUTTON),
        ('Attributes', ATTRIBUTE_BUTTON),
        ('Sort!', SUBMIT_BUTTON)
    ]

    for name, pos in main_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.menu_buttons_group.add(button)

    # ******************************************************************

    order_buttons = [
        ('Ascending', ASC),
        ('Descending', DESC)
    ]

    for name, pos in order_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.order_buttons_group.add(button)

    # ******************************************************************

    attribute_buttons = [
        ('Open', OPEN),
        ('High', HIGH),
        ('Low', LOW),
        ('Close', CLOSE),
        ('Volume', VOLUME),
        ('OpenInt', OPENINT)
    ]

    for name, pos in attribute_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.attribute_buttons_group.add(button)

    # ******************************************************************

    analyze_buttons = [
        ('Main Menu', MAIN_MENU_BUTTON_POSITION)
    ]
    
    for name, pos in analyze_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.analyze_buttons_group.add(button)
    # ******************************************************************


def menu_display(screen, sort_info, clock):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # If mouse inside borders of button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for btn in sort_info.menu_buttons_group:
                    if btn.rect.collidepoint(mouse_pos) and btn.update(FONT2, TEXT_COLOR1):
                        if btn.name == 'Order':
                            sort_info.order_dropdown_expanded = not sort_info.order_dropdown_expanded
                            sort_info.sort_dropdown_expanded = False
                            sort_info.attribute_dropdown_expanded = False
                        elif btn.name == 'Attributes':
                            sort_info.attribute_dropdown_expanded = not sort_info.attribute_dropdown_expanded
                            sort_info.sort_dropdown_expanded = False
                            sort_info.order_dropdown_expanded = False

                if sort_info.order_dropdown_expanded:
                    for btn in sort_info.order_buttons_group:
                        if btn.rect.collidepoint(mouse_pos):
                            for parentBtn in sort_info.menu_buttons_group:
                                if parentBtn.name == 'Order':
                                    parentBtn.change_button_name(btn.name)
                            sort_info.selected_order = btn.name
                            sort_info.order_dropdown_expanded = False

                # This sets the attributes for the stock objects
                if sort_info.attribute_dropdown_expanded:
                    for btn in sort_info.attribute_buttons_group:
                        if btn.rect.collidepoint(mouse_pos):
                            for parentBtn in sort_info.menu_buttons_group:
                                if parentBtn.name == 'Attributes':
                                    parentBtn.change_button_name(btn.name)
                            sort_info.selected_attribute = btn.name
                            sort_info.attribute_dropdown_expanded = False

                if sort_info.selected_order and sort_info.selected_attribute:
                    # submit button can now have functionality
                    pass
                for btn in sort_info.menu_buttons_group:
                    if btn.rect.collidepoint(mouse_pos):
                        if btn.name == 'Sort!':
                            return True

        draw(screen, sort_info)  # Updated draw call
        pg.display.update()
        clock.tick(60)


def analytics_screen(screen, sort_info, clock):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for btn in sort_info.analyze_buttons_group:
                    if btn.rect.collidepoint(mouse_pos):
                        return

        draw(screen, sort_info, None, None, 'Analyze')
        pg.display.update()
        clock.tick(60)


def loading_display(screen, sort_info, clock):
    loading_complete = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        screen.blit(Loading_dialogue, (loading_text_x, loading_text_y))
        pg.display.update()
        clock.tick(60)

        if loading_complete:
            return True

        gen_starting_list(sort_info)
        sort_off_attribute(sort_info.selected_attribute, sort_info)

        if sort_info.selected_order == "Descending":
            handle_descending(sort_info)

        set_top_5(sort_info.selected_attribute, sort_info)
        loading_complete = True


def initialize_buttons(screen, sort_info):
    gen_menu_buttons(screen, sort_info)


def main():
    screen = initialize_pygame()
    clock = pg.time.Clock()
    sort_info = SortInfo()
    initialize_buttons(screen, sort_info)
    while(True):
        move_to_loading_screen = menu_display(screen, sort_info, clock)
        if move_to_loading_screen:
            move_to_analytics_screen = loading_display(screen, sort_info, clock)
            if move_to_analytics_screen:
                analytics_screen(screen, sort_info, clock)


if __name__ == "__main__":
    main()

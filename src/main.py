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
        self.ascending = True
        self.lst_sorted = False
        self.selected_sort = None
        self.selected_order = None
        self.selected_attribute = None
        self.date = ""
        self.list = []  # List  of stock data objects to perform sorting on
        self.images = Images()
        self.menu_buttons_group = pg.sprite.Group()
        self.sort_buttons_group = pg.sprite.Group()
        self.order_buttons_group = pg.sprite.Group()
        self.attribute_buttons_group = pg.sprite.Group()
        self.input_box_group = pg.sprite.Group()
        self.boxes = pg.sprite.Group()  # This is for testing a tree based representation
        self.nodes = pg.sprite.Group()  # This is for testing a tree based representation
        self.heap = None
        self.bars = None
        self.sort_dropdown_expanded = False
        self.order_dropdown_expanded = False
        self.attribute_dropdown_expanded = False

        # Initialize the input box for menu_display screen
        self.input_box = InputBox(120, 35)
        self.input_box_group.add(self.input_box)


def initialize_pygame():
    pg.init()
    screen = pg.display.set_mode(WINDOWSIZE)
    pg.display.set_caption("Sorting Algorithm Visualizer")
    return screen


def gen_starting_list(sort_info):
    if sort_info.date and sort_info.selected_attribute:
        stock_data = load_data(sort_info.date, '../Stocks')  # Load data with date filtering
        sort_info.list = stock_data[:n]


# Reference button.py for more info
def gen_menu_buttons(screen, sort_info):
    main_buttons = [
        ('Sort Type', SORT_BUTTON),
        ('Order', ORDER_BUTTON),
        ('Attributes', ATTRIBUTE_BUTTON),
    ]

    for name, pos in main_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.menu_buttons_group.add(button)

    # ******************************************************************

    sort_buttons = [
        ('Heap Sort', HEAP_SORT),
        ('Tim Sort', TIM_SORT)
    ]

    for name, pos in sort_buttons:
        button = Button(screen, sort_info, name, pos[0], pos[1], SCALE, ELEVATION)
        sort_info.sort_buttons_group.add(button)

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


def menu_display(screen, sort_info, clock):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            sort_info.input_box.handle_event(event, sort_info)  # Handle text-box input

            # If mouse inside borders of button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for btn in sort_info.menu_buttons_group:
                    if btn.rect.collidepoint(mouse_pos) and btn.update(FONT2, TEXT_COLOR1):
                        if btn.name == 'Sort Type':
                            sort_info.sort_dropdown_expanded = not sort_info.sort_dropdown_expanded
                            sort_info.order_dropdown_expanded = False
                            sort_info.attribute_dropdown_expanded = False
                        elif btn.name == 'Order':
                            sort_info.order_dropdown_expanded = not sort_info.order_dropdown_expanded
                            sort_info.sort_dropdown_expanded = False
                            sort_info.attribute_dropdown_expanded = False
                        elif btn.name == 'Attributes':
                            sort_info.attribute_dropdown_expanded = not sort_info.attribute_dropdown_expanded
                            sort_info.sort_dropdown_expanded = False
                            sort_info.order_dropdown_expanded = False

                if sort_info.sort_dropdown_expanded:
                    for btn in sort_info.sort_buttons_group:
                        if btn.rect.collidepoint(mouse_pos):
                            sort_info.selected_sort = btn.name
                            sort_info.sort_dropdown_expanded = False

                if sort_info.order_dropdown_expanded:
                    for btn in sort_info.order_buttons_group:
                        if btn.rect.collidepoint(mouse_pos):
                            sort_info.selected_order = btn.name
                            sort_info.ascending = (btn.name == 'Ascending')
                            sort_info.order_dropdown_expanded = False

                # This sets the attributes for the stock objects
                if sort_info.attribute_dropdown_expanded:
                    for btn in sort_info.attribute_buttons_group:
                        if btn.rect.collidepoint(mouse_pos):
                            sort_info.selected_attribute = btn.name
                            sort_info.attribute_dropdown_expanded = False

        if sort_info.selected_sort and sort_info.selected_order and sort_info.selected_attribute\
                and sort_info.date:
            return  # Exit the menu when both sort and order are selected

        draw(screen, sort_info)  # Updated draw call
        pg.display.update()
        clock.tick(60)


def bar_sort_display(screen, sort_info, clock):
    comparator = Stock.get_comparator(sort_info.selected_attribute.lower(), sort_info.ascending)
    # Adjust this based on selected_sort
    sort_function = heap_sort if sort_info.selected_sort == 'Heap Sort' else timsort

    if sort_info.selected_sort == 'Heap Sort':
        sort_info.heap = Heap(screen, sort_info, comparator)
        sort_info.bars = get_bars_heapsort(
            sort_info.heap.arr,
            sort_info.list,
            SIDE_PAD,
            min(sort_info.list, key=comparator),
            max(sort_info.list, key=comparator),
            sort_info.selected_attribute.lower()
        )

    elif sort_info.selected_sort == "Tim Sort":
        sort_info.bars = get_bars_timsort(
            [],
            sort_info.list,
            SIDE_PAD,
            min(sort_info.list, key=comparator),
            max(sort_info.list, key=comparator),
            sort_info.selected_attribute.lower(),
            RUN_COLORS
        )

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                # Toggles sort or stop
                if event.key == pg.K_SPACE:
                    sort_info.sort = not sort_info.sort

                # Controls reset
                elif event.key == pg.K_r:
                    sort_info.sort = False
                    gen_starting_list(sort_info)
                    if sort_info.selected_sort == 'Heap Sort':
                        sort_info.heap = Heap(screen, sort_info, comparator)
                        sort_info.bars = get_bars_heapsort(sort_info.heap.arr, sort_info.list, SIDE_PAD, min(sort_info.list, key=comparator),  max(sort_info.list, key=comparator), sort_info.selected_attribute.lower())
                    elif sort_info.selected_sort == 'Tim Sort':
                        sort_info.bars = get_bars_timsort(sort_info.list, [], SIDE_PAD, min(sort_info.list, key=comparator), max(sort_info.list, key=comparator), sort_info.selected_attribute.lower(), RUN_COLORS)

        if not sort_info.sort:
            draw(screen, sort_info, sort_info.bars)  # Initial state of the bars, before we press space to begin sorting

        elif sort_info.sort:
            if sort_info.selected_sort == 'Heap Sort':
                sort_info.heap.insert_unsorted(sort_info)  # Part 1 - Insert elements into heap
                sort_function(sort_info.heap, sort_info)  # Part 2 - Sort elements
                sort_info.bars = get_bars_heapsort(sort_info.list, [], SIDE_PAD, min(sort_info.list, key=comparator), max(sort_info.list, key=comparator), sort_info.selected_attribute.lower())
            elif sort_info.selected_sort == 'Tim Sort':
                sort_function(sort_info.list, comparator, sort_info, screen)
                sort_info.bars = get_bars_timsort([], sort_info.list, SIDE_PAD, min(sort_info.list, key=comparator), max(sort_info.list, key=comparator), sort_info.selected_attribute.lower(), RUN_COLORS)

        pg.display.update()
        clock.tick(60)


def initialize_buttons(screen, sort_info):
    gen_menu_buttons(screen, sort_info)


def main():
    screen = initialize_pygame()
    clock = pg.time.Clock()
    sort_info = SortInfo()
    initialize_buttons(screen, sort_info)
    menu_display(screen, sort_info, clock)
    gen_starting_list(sort_info)
    bar_sort_display(screen, sort_info, clock)


if __name__ == "__main__":
    main()

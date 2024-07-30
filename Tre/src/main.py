import sys
import random
import pygame as pg
from images import *
from button import *
from constants import *
from heap import Heap
import merge_sort
from sorting import *
from bars import *
from draw import *

pg.init()
pg.mixer.init()
pg.mixer.music.load("../22.mp3")
screen = pg.display.set_mode(WINDOWSIZE)
pg.display.set_caption("Sorting Algorithm Visualizer")
clock = pg.time.Clock()  # For controlling framerate


class GS:
    sort = False
    stop = True
    click = False
    ascending = True
    lst_sorted = False
    selected_sort = None
    selected_order = None


def disp_message(text, font, color, x, y):
    message = font.render(text, True, color)
    message_rect = message.get_rect(center=(x, y))
    screen.blit(message, message_rect)


def gen_starting_list():
    lst = []
    for i in range(1, n + 1):
        num = random.randint(min_val, max_val)
        lst.append(num)
    return lst


def gen_sort_buttons(images):
    buttons_lst = []
    sort_button = Button(screen, images, 'Sort', SORT[0], SORT[1], SCALE, ELEVATION)
    stop_button = Button(screen, images, 'Stop', STOP[0], STOP[1], SCALE, ELEVATION)
    buttons_lst.extend([sort_button, stop_button])
    return buttons_lst


def gen_menu_buttons(images):
    buttons_lst = []
    heap_sort_button = Button(screen, images, 'Heap Sort', HEAP_SORT[0], HEAP_SORT[1], SCALE, ELEVATION)
    merge_sort_button = Button(screen, images, 'Merge Sort', MERGE_SORT[0], MERGE_SORT[1], SCALE, ELEVATION)
    asc_button = Button(screen, images, 'Ascending', ASC[0], ASC[1], SCALE, ELEVATION)
    desc_button = Button(screen, images, 'Descending', DESC[0], DESC[1], SCALE, ELEVATION)
    buttons_lst.extend([heap_sort_button, merge_sort_button, asc_button, desc_button])
    return buttons_lst


def menu_display(images):
    global gs

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # If mouse inside borders of button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in menu_buttons_group:
                    if button.check_click():
                        if button.name == 'Heap Sort':
                            gs.selected_sort = 'Heap Sort'
                            # Make sure only the Heap Sort button is pressed
                            for btn in menu_buttons_group:
                                if btn.name != 'Heap Sort':
                                    btn.pressed = False
                        elif button.name == 'Merge Sort':
                            gs.selected_sort = 'Merge Sort'
                            for btn in menu_buttons_group:
                                if btn.name != 'Merge Sort':
                                    btn.pressed = False
                        elif button.name == 'Ascending':
                            gs.selected_order = 'Ascending'
                            for btn in menu_buttons_group:
                                if btn.name != 'Ascending':
                                    btn.pressed = False
                        elif button.name == 'Descending':
                            gs.selected_order = 'Descending'
                            for btn in menu_buttons_group:
                                if btn.name != 'Descending':
                                    btn.pressed = False

            if gs.selected_sort and gs.selected_order:
                return  # Exit the menu when both sort and order are selected

        draw(screen, menu_buttons_group)  # Use the draw function from draw.py
        pg.display.update()
        clock.tick(60)


def sort_display(images):
    # global unsorted_lst, min_heap, bars, sort_buttons_group
    # Adjust this based on selected_sort and selected_order
    if gs.selected_sort == 'Heap Sort':
        sort_function = heap_sort
    elif gs.selected_sort == 'Merge Sort':
        sort_function = merge_sort
    else:
        raise ValueError("No valid sorting algorithm selected")
    
    unsorted_lst = gen_starting_list()
    min_heap = Heap(screen, unsorted_lst, sort_buttons_group)  # Instantiate heap
    bars = get_bars(min_heap.arr, unsorted_lst, SIDE_PAD, min(unsorted_lst), max(unsorted_lst))  # Generate Bar rectangles for drawing
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and gs.stop:
                    gs.stop = False
                    gs.sort = True

                if event.key == pg.K_r:  # Reset
                    gs.sort = False
                    gs.stop = True
                    unsorted_lst = gen_starting_list()
                    min_heap = Heap(screen, unsorted_lst, sort_buttons_group)
                    bars = get_bars(min_heap.arr, unsorted_lst, SIDE_PAD, min(unsorted_lst), max(unsorted_lst))

                # Controls min or max sorting order
                if event.key == pg.K_a and not gs.sort and not gs.ascending:
                    gs.ascending = True

            if event.type == pg.MOUSEBUTTONDOWN:
                for button in sort_buttons_group:
                    if button.check_click():
                        if button.name == 'Sort':
                            gs.sort = True
                            gs.stop = False
                        if button.name == 'Stop':
                            gs.stop = True

        if gs.stop and min_heap.size == 0:
            draw(screen, sort_buttons_group, bars)

        elif gs.sort:
            pg.mixer.music.play(-1)
            min_heap.insert_unsorted(gs)
            sort_function(min_heap, gs)
            gs.sort = False
            pg.mixer.music.stop()

        pg.display.update()
        clock.tick(60)


# Initialization of globals
gs = GS()
menu_buttons_group = None
sort_buttons_group = None
images = Images()


def main():
    global gs, images, sort_buttons_group, menu_buttons_group

    # Define menu buttons
    menu_buttons = gen_menu_buttons(images)
    menu_buttons_group = pg.sprite.Group(menu_buttons)
    
    menu_display(images)
    
    # Define sort buttons
    buttons = gen_sort_buttons(images)
    sort_buttons_group = pg.sprite.Group(buttons)
    
    sort_display(images)

if __name__ == "__main__":
    main()

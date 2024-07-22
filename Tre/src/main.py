import sys
import random
from images import *
from button import *
from constants import *
from heap import Heap
from sorting import *
from bars import *
from draw import *

pg.init()
screen = pg.display.set_mode(WINDOWSIZE)
pg.display.set_caption("Sorting Algorithm Visualizer")
clock = pg.time.Clock()  # For controlling framerate
sort = False
click = False
ascending = True


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


def gen_buttons():
    buttons_lst = []
    sort_button = Button(screen, images, 'Sort', SORT[0], SORT[1], SCALE, ELEVATION)
    stop_button = Button(screen, images, 'Stop', STOP[0], STOP[1], SCALE, ELEVATION)
    buttons_lst.append(sort_button)
    buttons_lst.append(stop_button)
    return buttons_lst


# Load images here and store in Images class
images = Images()

# Create sprite group for buttons
buttons = gen_buttons()
buttons_group = pg.sprite.Group(buttons)

unsorted_lst = gen_starting_list()  # Generate list to sort
min_heap = Heap(screen, unsorted_lst, buttons_group)  # Instantiate heap
bars = get_bars(min_heap.arr, unsorted_lst, SIDE_PAD, min(unsorted_lst), max(unsorted_lst))  # Generate Bar rectangles for drawing


def main_menu():
    global click, sort, ascending, unsorted_lst, min_heap, bars
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not sort:
                    sort = True

                if event.key == pg.K_r:  # Reset
                    sort = False
                    unsorted_lst = gen_starting_list()
                    min_heap = Heap(screen, unsorted_lst, buttons_group)
                    bars = get_bars(min_heap.arr, unsorted_lst, SIDE_PAD, min(unsorted_lst), max(unsorted_lst))

                # Controls min or max sorting order
                if event.key == pg.K_a and not sort and not ascending:
                    ascending = True

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if sort:
            min_heap.insert_unsorted()
            sort = False

        elif not sort and min_heap.size == 0:
            draw(screen, buttons_group, bars)

        pg.display.update()
        clock.tick(60)


def main():
    main_menu()


if __name__ == "__main__":
    main()

import pygame as pg
import sys
from constants import *
from bars import get_bars_heapsort
from draw import *


class Heap:
    # Constructor
    def __init__(self, screen, sort_info, comparator, heap_type="min"):
        self.screen = screen
        self.sort_info = sort_info
        self.unsorted_arr = sort_info.list
        self.arr = []
        self.sorted_arr = []  # This is where the final sorted list goes
        self.buttons_group = sort_info.sort_buttons_group
        self.heap_type = heap_type
        self.size = 0
        self.comparator = comparator
        self.min_val = min(self.unsorted_arr, key=self.comparator) if self.unsorted_arr else None
        self.max_val = max(self.unsorted_arr, key=self.comparator) if self.unsorted_arr else None

    def key(self, stock):
        return self.comparator(stock)

    def insert(self, x, sort_info):
        self.arr.append(x)
        self.unsorted_arr.pop()
        self.size += 1
        self.heapify_up(self.size - 1, sort_info)  # Heapify up from the last element

    def insert_unsorted(self, sort_info):
        while self.unsorted_arr:
            self.handle_events(sort_info)
            if not sort_info.sort:
                while not sort_info.sort:
                    self.handle_events(sort_info)

            self.insert(self.unsorted_arr[-1], sort_info)

    # Accesses the min or max element in the heap
    def get(self):
        return self.arr[0] if self.arr else None

    # Removes the min or max element in the heap
    def extract(self, sort_info):
        if sort_info.lst_sorted:
            while sort_info.lst_sorted:
                self.display(self.sorted_arr, self.unsorted_arr)
                self.handle_events(sort_info)
                if not sort_info.lst_sorted:
                    return

        if not sort_info.sort:
            return

        if not self.arr:
            sort_info.lst_sorted = True

        root = self.arr[0]
        if self.size > 1:
            self.sorted_arr.append(self.arr[0])
            self.arr[0] = self.arr.pop()
            self.size -= 1
            self.heapify_down(0, sort_info)
        else:
            self.arr.pop()
            self.size -= 1

        return root

    def heapify_up(self, child, sort_info):
        parent = (child - 1) // 2
        while child > 0:
            self.handle_events(sort_info)
            if not sort_info.sort:
                while not sort_info.sort:
                    self.handle_events(sort_info)

            if self.heap_type == "min":
                if self.key(self.arr[child]) < self.key(self.arr[parent]):
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                else:
                    break
            else:
                if self.key(self.arr[child]) > self.key(self.arr[parent]):
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                else:
                    break

            self.display(self.arr, self.unsorted_arr, child)
            pg.time.delay(50)
            child = parent
            parent = (child - 1) // 2

    def heapify_down(self, parent, sort_info):
        while True:
            self.handle_events(sort_info)
            if not sort_info.sort:
                while not sort_info.sort:
                    self.handle_events(sort_info)
            left = 2 * parent + 1
            right = 2 * parent + 2
            child = parent

            if self.heap_type == "min":
                if left < len(self.arr) and self.key(self.arr[left]) < self.key(self.arr[child]):
                    child = left
                if right < len(self.arr) and self.key(self.arr[right]) < self.key(self.arr[child]):
                    child = right

            else:
                if left < len(self.arr) and self.key(self.arr[left]) > self.key(self.arr[child]):
                    child = left
                if right < len(self.arr) and self.key(self.arr[right]) > self.key(self.arr[child]):
                    child = right

            if child == parent:
                break

            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            self.display(self.sorted_arr, self.arr, child)
            pg.time.delay(50)
            parent = child

    def handle_events(self, sort_info):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:  # Pause sorting
                    sort_info.sort = not sort_info.sort

                if event.key == pg.K_r:  # Reset
                    sort_info.sort = False
                    sort_info.lst_sorted = False

    def display(self, sorted_lst, unsorted_lst, new_ele_idx=None):
        bar_width = (WINDOWSIZE[0] - TOTAL_SIDE_PAD) / (self.size + len(unsorted_lst))
        unsorted_start_x = SIDE_PAD + len(sorted_lst) * bar_width

        # Reverse the arrays if sorting in descending order
        if not self.sort_info.ascending:
            sorted_lst = sorted_lst[::-1]
            unsorted_lst = unsorted_lst[::-1]

        bars = get_bars_heapsort(sorted_lst, unsorted_lst, unsorted_start_x, self.min_val, self.max_val, self.sort_info.selected_attribute.lower(), new_ele_idx)

        draw(self.screen, self.sort_info, bars, new_ele_idx)
        vert_space = (WINDOWSIZE[1] - TOP_PADDING) - (WINDOWSIZE[1] - sorting_bottom)
        pg.display.update()


















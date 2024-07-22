import sys
import pygame as pg
from bars import get_bars
from draw import *
from constants import *


class Heap:
    # Constructor
    def __init__(self, screen, unsorted_arr, buttons_group, heap_type="min",  key=lambda x: x):
        self.screen = screen
        self.unsorted_arr = unsorted_arr
        self.arr = []
        self.sorted_arr = []
        self.buttons_group = buttons_group
        self.key = key
        self.heap_type = heap_type
        self.size = 0
        self.min_val = min(unsorted_arr)
        self.max_val = max(unsorted_arr)

    def insert(self, x, gs):
        self.arr.append(x)
        self.unsorted_arr.pop()
        self.size += 1
        self.heapify_up(self.size - 1, gs)  # Heapify up from the last element

    def insert_unsorted(self, gs):
        for i in reversed(self.unsorted_arr):
            self.handle_events(gs)

            if not gs.sort:
                break
            self.insert(i, gs)

    # Accesses the min or max element in the heap
    def get(self):
        return self.arr[0] if self.arr else None

    # Removes the min or max element in the heap
    def extract(self, gs):
        if gs.lst_sorted:
            while gs.lst_sorted:
                self.display(self.sorted_arr, self.unsorted_arr)
                self.handle_events(gs)
                if not gs.lst_sorted:
                    return
        if not gs.sort:
            return

        if not self.arr:
            gs.lst_sorted = True

        root = self.arr[0]
        if self.size > 1:
            self.sorted_arr.append(self.arr[0])
            self.arr[0] = self.arr.pop()
            self.size -= 1
            self.heapify_down(0, gs)
        else:
            self.arr.pop()
            self.size -= 1

        return root

    def heapify_up(self, child, gs):
        parent = (child - 1) // 2
        while child > 0:
            self.handle_events(gs)
            if not gs.sort:
                return

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

    def heapify_down(self, parent, gs):
        while True:
            self.handle_events(gs)
            if not gs.sort:
                return

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

    def handle_events(self, gs):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in self.buttons_group:
                    if button.check_click():
                        if button.name == 'Sort' and gs.stop and not gs.sort:
                            gs.sort = True
                            gs.stop = False
                        elif button.name == 'Stop' and gs.sort and not gs.stop:
                            gs.stop = True
                            gs.sort = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:  # Reset
                    gs.sort = False
                    gs.lst_sorted = False
                    gs.stop = True

    def display(self, sorted_lst, unsorted_lst, new_ele_idx=None):
        bar_width = (WINDOWSIZE[0] - TOTAL_SIDE_PAD) / (self.size + len(unsorted_lst))
        unsorted_start_x = SIDE_PAD + len(sorted_lst) * bar_width

        bars = get_bars(sorted_lst, unsorted_lst, unsorted_start_x, self.min_val, self.max_val, new_ele_idx)

        draw(self.screen, self.buttons_group, bars, new_ele_idx)
        pg.display.update()


















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
        self.buttons_group = buttons_group
        self.key = key
        self.heap_type = heap_type
        self.size = 0
        self.min_val = min(unsorted_arr)
        self.max_val = max(unsorted_arr)

    def insert(self, x):
        self.arr.append(x)
        self.unsorted_arr.pop()
        self.size += 1
        self.heapify_up(self.size - 1)  # Heapify up from the last element

    def insert_unsorted(self):
        for i in reversed(self.unsorted_arr):
            self.insert(i)

    # Accesses the min or max element in the heap
    def get(self):
        return self.arr[0] if self.arr else None

    # Removes the min or max element in the heap
    def extract(self):
        if not self.arr:
            return None
        root = self.arr[0]
        if self.size > 1:
            self.arr[0] = self.arr.pop()
            self.size -= 1
            self.heapify_down(0)
        else:
            self.arr.pop()
            self.size -= 1
        return root

    def heapify_up(self, child):
        parent = (child - 1) // 2
        while child > 0:
            if self.heap_type == "min":
                if self.key(self.arr[child]) < self.key(self.arr[parent]):
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                    self.draw()
                    pg.time.delay(250)
                else:
                    break
            else:
                if self.key(self.arr[child]) > self.key(self.arr[parent]):
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                    self.draw()
                    pg.time.delay(250)
                else:
                    break

            child = parent
            parent = (child - 1) // 2

    def heapify_down(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        child = 0

        if left >= len(self.arr):
            return

        if right >= len(self.arr):
            child = left

        if self.type == "min":
            if right < len(self.arr):
                child = left if self.key(self.arr[left]) < self.key(self.arr[right]) else right

            if(self.key(self.arr[parent]) > self.key(self.arr[child])):
                temp = self.arr[parent]
                self.arr[parent] = self.arr[child]
                self.arr[child] = temp
                self.heapify_down(child)
        else:
            if right < len(self.arr):
                child = left if self.key(self.arr[left]) > self.key(self.arr[right]) else right

            if(self.key(self.arr[parent]) < self.key(self.arr[child])):
                temp = self.arr[parent]
                self.arr[parent] = self.arr[child]
                self.arr[child] = temp
                self.heapify_down(child)
        return


    def draw(self):
        bar_width = (WINDOWSIZE[0] - TOTAL_SIDE_PAD) / (self.size + len(self.unsorted_arr))
        unsorted_start_x = SIDE_PAD + len(self.arr) * bar_width

        bars = get_bars(self.arr, self.unsorted_arr, unsorted_start_x, self.min_val, self.max_val)

        draw(self.screen, self.buttons_group, bars)
        pg.display.update()

















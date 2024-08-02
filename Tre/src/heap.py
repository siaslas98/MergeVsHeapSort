import sys
import pygame as pg
from bars import get_bars
from draw import *
from constants import *

class Heap:
    # Constructor
    def __init__(self, screen, unsorted_arr, buttons_group, heap_type="min", key=lambda x: x):
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
            self.insert(i, gs)

    def heapify_up(self, index, gs):
        parent_index = (index - 1) // 2
        if index <= 0:
            return

        if self.heap_type == "min":
            if self.key(self.arr[index]) < self.key(self.arr[parent_index]):
                self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
                self.heapify_up(parent_index, gs)
        else:  # max heap
            if self.key(self.arr[index]) > self.key(self.arr[parent_index]):
                self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
                self.heapify_up(parent_index, gs)

    def heapify_down(self, index, gs):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_or_largest = index

        if self.heap_type == "min":
            if left_child_index < self.size and self.key(self.arr[left_child_index]) < self.key(self.arr[smallest_or_largest]):
                smallest_or_largest = left_child_index
            if right_child_index < self.size and self.key(self.arr[right_child_index]) < self.key(self.arr[smallest_or_largest]):
                smallest_or_largest = right_child_index
        else:  # max heap
            if left_child_index < self.size and self.key(self.arr[left_child_index]) > self.key(self.arr[smallest_or_largest]):
                smallest_or_largest = left_child_index
            if right_child_index < self.size and self.key(self.arr[right_child_index]) > self.key(self.arr[smallest_or_largest]):
                smallest_or_largest = right_child_index

        if smallest_or_largest != index:
            self.arr[index], self.arr[smallest_or_largest] = self.arr[smallest_or_largest], self.arr[index]
            self.heapify_down(smallest_or_largest, gs)

    def extract(self, gs):
        if self.size == 0:
            return None
        root = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.heapify_down(0, gs)
        return root
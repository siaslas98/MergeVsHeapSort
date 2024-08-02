class Heap:
    def __init__(self, screen, unsorted_arr, buttons_group, heap_type="min", key=lambda x: x[1]):
        self.screen = screen
        self.unsorted_arr = unsorted_arr
        self.arr = []
        self.sorted_arr = []
        self.buttons_group = buttons_group
        self.key = key
        self.heap_type = heap_type
        self.size = 0
        self.min_val = min(unsorted_arr, key=self.key)[1]
        self.max_val = max(unsorted_arr, key=self.key)[1]
        self.build_heap()

    def build_heap(self):
        for item in self.unsorted_arr:
            self.insert(item)

    def insert(self, x):
        self.arr.append(x)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        if (self.heap_type == "min" and self.key(self.arr[index]) < self.key(self.arr[parent])) or \
           (self.heap_type == "max" and self.key(self.arr[index]) > self.key(self.arr[parent])):
            self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest_or_largest = index

        if left < self.size and ((self.heap_type == "min" and self.key(self.arr[left]) < self.key(self.arr[smallest_or_largest])) or \
                                 (self.heap_type == "max" and self.key(self.arr[left]) > self.key(self.arr[smallest_or_largest]))):
            smallest_or_largest = left

        if right < self.size and ((self.heap_type == "min" and self.key(self.arr[right]) < self.key(self.arr[smallest_or_largest])) or \
                                  (self.heap_type == "max" and self.key(self.arr[right]) > self.key(self.arr[smallest_or_largest]))):
            smallest_or_largest = right

        if smallest_or_largest != index:
            self.arr[index], self.arr[smallest_or_largest] = self.arr[smallest_or_largest], self.arr[index]
            self.heapify_down(smallest_or_largest)

    def extract(self):
        if self.size == 0:
            return None
        root = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.arr.pop()
        self.heapify_down(0)
        return root

    def sort_heap(self):
        self.sorted_arr = []
        while self.size > 0:
            self.sorted_arr.append(self.extract())
            self.show_heap_state()

    def show_heap_state(self):
        bars = get_bars(self.sorted_arr, self.arr, TOTAL_SIDE_PAD // 2, self.min_val, self.max_val)
        draw_bars(self.screen, bars)

    def get_top_5_with_names(self):
        top_5 = self.sorted_arr[:5] if self.heap_type == "min" else self.sorted_arr[-5:]
        return top_5
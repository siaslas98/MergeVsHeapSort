def heap_sort(min_heap):
    sorted_array = []

    while min_heap.size > 0:
        sorted_array.append(min_heap.extract())

    return sorted_array

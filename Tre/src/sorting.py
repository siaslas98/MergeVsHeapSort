def heap_sort(min_heap, gs):
    sorted_array = []

    while min_heap.size > 0 and gs.sort and not gs.lst_sorted:
        sorted_array.append(min_heap.extract(gs))

    return sorted_array

Here is a more organized version of your documentation:

---

# Documentation

## main():
1. **Initialize pygame and store the window**
2. **Create a clock object**
3. **Initialize SortInfo object**
    - This object is used across the entire program.
4. **Initialize the buttons with a drop-down feature**
5. **Enter the menu_display window**
    - Within this window:
        - Check for the selected sort.
        - Check for the selected sort order.
        - Check for the selected attribute.
        - Check for input into the input box (format: "year-month-day").
    - Once all selections are made and `sort_info` is updated, return to `main()`.
6. **Generate the starting list using the updated sort_info**
    - The starting list is a list of stock objects of size `n` (defined in `constants.py`).
7. **Enter the bar_sort_display window**
    - Within this window:
        - Create a comparator to sort stock objects based on the selected attribute.
        - Set the sort function to `heap_sort` or `timsort` based on `sort_info`.
        - For Heap Sort:
            - Create a Heap instance.
            - Get bars using `get_bars_heapsort`.
        - For Tim Sort:
            - Get bars using `get_bars_timsort`.
            - Note the difference between the two methods.
        - Start sorting when the user presses "space" (you can add more buttons if desired).
        - If "r" is pressed:
            - Call `gen_sorting_list(sort_info)` to reset the comparator.
            - Add functionality to return to the `menu_display` screen for easier resetting.
        - Draw the initial bars if `sort_info.sort` is false.
        - If Heap Sort is selected:
            - Insert values into the heap.
            - Call `heap_sort` on the heap.
            - Display the final sorted bars until further actions are detected.

---

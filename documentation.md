main():
    1.) Initialize pygame and store the window
    2.) Create a clock object
    3.) Initialize SortInfo object to be used across the entire program
    4.) Initialize the buttons with a drop-down feature
    5.) Enter the menu_display window
        Within this window we do the following:
            -Check for the sort selected
            -Check for sort order selected
            -Check for attribute selected
            -Check for input into the input box. The input box is for entering a date of the
                format "year-month-day"
            Once all of these are selected and sort_info has been updated, we return to main()
    6.) Generate the starting list using the updated sort_info
        The starting list is a list of stock objects of size n. n is defined in constants.py
    7.) Enter the bar_sort_display window
        Within this window we do the following:
            -Create a comparator so that we can later sort stock Objects based on the selected attribute
            - Set the sort function to be equal to heap_sort or timsort based on what we have in sort info
            - For heap, we need to create a Heap instance and get bars using get_bars_heapsort
            - For tim, we get bars using get_bars_timsort
            - Notice the difference between the two
            - If the user presses "space" we begin sorting. You can add more buttons if you'd like
            - If "r" is pressed, we call gen_sorting_list(sort_info) again and reset comparator
              * Add functionality so that if r is pressed, we go back to the menu_display screen
                this will probably make resetting much easier
            - Draw the initial bars if sort_info.sort is false
            - Else if the selected sort is Heap Sort we insert the values into the heap,
              Then call heap_sort on this heap
              In the end, display the final sorted bars until further actions are detected
            

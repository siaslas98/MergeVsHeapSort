import sys
import random
import pygame as pg
from images import *
from button import *
from constants import *
from heap import Heap
from sorting import *
from bars import *
from draw import *
from timer import Timer
from timsort import *
from colors import *
from Load_Stocks import Stocks
from Text_Input import Text_Input_Box

pg.init()
pg.mixer.init()
pg.mixer.music.load("Audio/22.mp3")
# setting the screen 
screen = pg.display.set_mode(WINDOWSIZE)
pg.display.set_caption("Stock Statistics + Sorting Algorithm Visualizer")
clock = pg.time.Clock()  # For controlling framerate

# initializing the timer
timer = Timer()

class GS:
    lst_sorted = False
    selected_option = None
    selected_order = None
    show_visuals = None
    visual = None
    date = (None,None)

def disp_message(text, font, color, x, y):
    message = font.render(text, True, color)
    message_rect = message.get_rect(center=(x, y))
    screen.blit(message, message_rect)

def gen_button_stats(images):
    buttons_lst = []
    stats_visible = Button(screen, images, 'Statistics', 200, 200, SCALE, ELEVATION)
    return buttons_lst

def gen_visual_buttons(images):
    buttons_lst = []
    sort_button = Button(screen, images, 'Start/Resume Sort', SORT[0], SORT[1], SCALE, ELEVATION)
    stop_button = Button(screen, images, 'Stop', STOP[0], STOP[1], SCALE, ELEVATION)
    buttons_lst.append(sort_button)
    buttons_lst.append(stop_button)
    return buttons_lst

def gen_menu_buttons_part1(images):
    buttons_lst = []

    percent_change_button = Button(screen, images, 'Percent Change', percent_change_position[0], percent_change_position[1], SCALE, ELEVATION)
    price_change_button = Button(screen, images, 'Price Change', price_change_position[0], price_change_position[1], SCALE, ELEVATION)
    week_52_low_button = Button(screen, images, '52-Week-Low', week_52_Low_position[0], week_52_Low_position[1], SCALE, ELEVATION)
    week_52_high_button = Button(screen, images, '52-Week-High', week_52_High_position[0], week_52_High_position[1], SCALE, ELEVATION)
    market_cap_button = Button(screen, images, 'Market Cap', market_cap_position[0], market_cap_position[1], SCALE, ELEVATION)  
    buttons_lst.extend([week_52_high_button, week_52_low_button, price_change_button, percent_change_button, market_cap_button])
    return buttons_lst

def gen_menu_buttons_part2(images):
    buttons_lst = []
    low_button = Button(screen, images, 'Minimum', low_button_position[0], low_button_position[1] , SCALE, ELEVATION)
    high_button = Button(screen, images, 'Maximum', high_button_position[0], high_button_position[1], SCALE, ELEVATION)
    buttons_lst.extend([ high_button, low_button])
    return buttons_lst

def gen_menu_buttons_part3(images):
    buttons_lst = []
    yes_button = Button(screen, images, 'Yes', high_button_position[0], high_button_position[1], SCALE, ELEVATION)
    no_button = Button(screen, images, 'No', low_button_position[0], low_button_position[1], SCALE, ELEVATION)
    buttons_lst.extend([ no_button, yes_button])
    return buttons_lst

def gen_menu_buttons_part4(images):
    buttons_lst = []
    timsort_button = Button(screen, images, 'Timsort', high_button_position[0], high_button_position[1], SCALE, ELEVATION)
    heap_sort_button = Button(screen, images, 'Heap Sort', low_button_position[0], low_button_position[1], SCALE, ELEVATION)
    buttons_lst.extend([ timsort_button, heap_sort_button])
    return buttons_lst

def is_sorted(lst, ascending=True):
    """Check if the list is sorted in the specified order."""
    if ascending:
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    else:
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

def Display_Statistics():
    # Create a screen
    screen_width = 800
    screen_height = 600
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Sorting Statistics")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Define font
    font = pg.font.Font(None, 74)

    # Get the elapsed time
    elapsed_time = timer.get_elapsed_time()

    # Convert elapsed time to a string and round to 2 decimal places
    elapsed_time_str = f"Elapsed Time: {elapsed_time:.2f} seconds"

    # Main loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        # Fill the screen with white color
        screen.fill(white)

        # Render the elapsed time text
        text = font.render(elapsed_time_str, True, black)
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

        # Blit the text onto the screen
        screen.blit(text, text_rect)

        # Update the display
        pg.display.flip()
    
    # Quit Pygame
    pg.quit()
    sys.exit()

def menu_display_1(images):
    global gs

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # if inside of the button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in menu_buttons_part1_group:
                    if button.check_if_clicked():
                        if button.name == 'Percent Change':
                            gs.selected_option = 'Percent Change'
                            return
                        elif button.name == 'Price Change':
                            gs.selected_option = 'Price Change'
                            return
                        elif button.name == '52-Week-Low':
                            gs.selected_option = '52-Week'
                            return
                        elif button.name == 'Market Cap':
                            gs.selected_option = 'Market Cap'
                            return
                        elif button.name == '52-Week-High':
                            gs.selected_option = '52-Week-High'
                            return
                        else:
                            raise ValueError("No valid option selected")

        draw(screen, menu_buttons_part1_group, 'Menu')  # Use the draw function from draw.py
        
        pg.display.update()
        clock.tick(60)

def menu_display_2(images):
    global gs, menu_buttons_part2_group

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if inside of the button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in menu_buttons_part2_group:
                    if button.check_if_clicked():
                        if button.name == 'Minimum':
                            gs.selected_order = 'Minimum'
                            return
                        elif button.name == 'Maximum':
                            gs.selected_order = 'Maximum'
                            return 
                        else:
                            raise ValueError("No valid option selected")

        draw(screen, menu_buttons_part2_group, 'Menu')  # Use the draw function from draw.py
        pg.display.update()
        clock.tick(60)

def menu_display_3(images):
    global gs, menu_buttons_part3_group

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if inside of the button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in menu_buttons_part3_group:
                    if button.check_if_clicked():
                        if button.name == 'Yes':
                            gs.show_visuals = 'Yes'
                            return
                        elif button.name == 'No':
                            gs.show_visuals = 'No'
                            return 
                        else:
                            raise ValueError("No valid option selected")
        draw(screen, menu_buttons_part3_group, 'Menu')  # Use the draw function from draw.py
        pg.display.update()
        clock.tick(60)

def menu_display_4(images):
    global gs, menu_buttons_part4_group

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if inside of the button and pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in menu_buttons_part4_group:
                    if button.check_if_clicked():
                        if button.name == 'Timsort':
                            gs.visual= 'Timsort'
                            return
                        elif button.name == 'Heap Sort':
                            gs.visual = 'Heap Sort'
                            return
                        else:
                            raise ValueError("No valid option selected")

        draw(screen, menu_buttons_part4_group, 'Menu')  # Use the draw function from draw.py
        pg.display.update()
        clock.tick(60)

def sort_display(images):
    global unsorted_lst, bars, visual_buttons_group, stats_group, timer
    # Adjust this based on selected_sort and selected_order
    if gs.visual == 'Heap Sort':
        sort_function = heap_sort
    elif gs.visual == 'Timsort':
        sort_function = timsort
    else:
        raise ValueError("No valid sorting algorithm selected")
    
    # Initialize the sorting state
    sorting_paused = True
    sorting_start = False

    gs.date = ('2023-10-01', '2023-10-02')
    
    # Generate the two Stocks
    Stock_1 = Stocks()
    Stock_1.Generate_Stock_for_day(n,gs.date[0])
    Stock_2 = Stocks()
    Stock_2.Generate_Stock_for_day(n,gs.date[1])

    # Generate the list that needs to be sorted
    u_list = []
    
    if gs.selected_option == 'Percent Change':
        for i in range(len(day1)):
            percent_change = ((day2[i] - day1[i]) / day1[i] * 100)
            stock_name = stock_name[i]
            u_list.append((stock_name), (percent_change))
    elif gs.selected_option == 'Price Change':
        day2 = Stock_1.get_all_stock_prices()
        for i in range(len(day1)):
            price_change = (day2[i] - day1[i])
            stock_name = stock_name[i]
            u_list.append((stock_name), (price_change))
    elif gs.selected_option == '52-Week-Low':
        day1 = Stock_1.get_all_stock_52_week_low()
        for i in range(len(day1)):
            week_low = day1[i]
            u_list.append((stock_name), (week_low))
    elif gs.selected_option == '52-Week-High':
        day1 = Stock_1.get_all_stock_52_week_high()
        for i in range(len(day1)):
            week_high = day1[i]
            u_list.append((stock_name), (week_high))
    elif gs.selected_option == 'Market Cap':
        day1 = Stock_1.get_all_stock_market_caps()
        for i in range(len(day1)):
            market_cap = day1[i]
            u_list.append((stock_name), (market_cap))

    

    unsorted_lst = u_list

    if gs.selected_order == 'Maximum':
        heap = Heap(screen, unsorted_lst, visual_buttons_group, 'max')
    elif gs.selected_order == 'Minimum':
        heap = Heap(screen, unsorted_lst, visual_buttons_group, 'min')

    bars = get_bars(heap.arr, unsorted_lst, SIDE_PAD, min(unsorted_lst), max(unsorted_lst))  # Generate Bar rectangles for drawing
    
    Sorting_Finished = False

    while (Sorting_Finished == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # checking if space bar was pressed to start/stop/resume the sorting
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # If the sorting hasnt started, start it and the timer
                    if sorting_start == False:
                        sorting_start = True
                        timer.start()
                    # If the sorting is paused, resume it and the timer
                    elif (sorting_start and sorting_paused):
                        sorting_paused = False
                        timer.resume()
                    # If the sorting is running, pause it and the timer
                    elif (sorting_start and (sorting_paused == False)):
                        timer.pause()
                        sorting_paused = True

            if event.type == pg.MOUSEBUTTONDOWN:
                for button in visual_buttons_group:
                    if button.check_click():
                        if button.name == 'Start/Resume Sort':
                            # If the sorting hasnt started, start it and the timer
                            if sorting_start == False:
                                sorting_paused = False
                                sorting_start = True
                                timer.start()
                            # If the sorting is paused, resume it and the timer
                            elif (sorting_start and sorting_paused):
                                sorting_paused = False
                                timer.resume()
                        if button.name == 'Stop':
                            # If the sorting is running, pause it and the timer
                            if (sorting_start and (sorting_paused == False)):
                                timer.pause()
                                sorting_paused = True
                            
                                
                        if button.name == 'Statistics':
                            Sorting = False  
                            # Exit the sorting loop
        
        if Sorting_Finished == False and sorting_start == True:
            pg.mixer.music.play(-1)
            heap.insert_unsorted(gs)
            sort_function(heap, gs)
            draw(screen, visual_buttons_group, bars)
            # Check if the list is sorted in the desired order
            if is_sorted(min_heap.arr, gs.ascending):
                draw_buttons(screen, stats_group)
            pg.mixer.music.stop()

        pg.display.update()
        clock.tick(60)


def main():
    global gs, visual_buttons_group, menu_buttons_part1_group, stats_group, menu_buttons_part2_group, menu_buttons_part3_group, menu_buttons_part4_group
    gs = GS()  # Initialize the game state
    
    # Initialize images
    images = Images()

    # initialize the buttons for the menu part 1
    menu_buttons_part1 = gen_menu_buttons_part1(images)
    menu_buttons_part1_group = pg.sprite.Group(menu_buttons_part1)

    menu_display_1(images)

    # initialize the buttons for the menu part 2
    menu_buttons_part2 = gen_menu_buttons_part2(images)
    menu_buttons_part2_group = pg.sprite.Group(menu_buttons_part2)

    menu_display_2(images)

    # initialize the buttons for the menu part 3
    menu_buttons_part3 = gen_menu_buttons_part3(images)
    menu_buttons_part3_group = pg.sprite.Group(menu_buttons_part3)

    menu_display_3(images)

    if(gs.show_visuals == 'Yes'):
        # initialize the buttons for the menu part 4
        menu_buttons_part4 = gen_menu_buttons_part4(images)
        menu_buttons_part4_group = pg.sprite.Group(menu_buttons_part4)

        menu_display_4(images)
        # Initialize the buttons for sorting display
        visual_buttons = gen_visual_buttons(images)
        visual_buttons_group = pg.sprite.Group(visual_buttons)

        sort_display(images)
    else:
        Calculate_Statistics()

    # initialize the buttons for statistics display
    stats_visible = gen_button_stats(images)
    stats_group = pg.sprite.Group(stats_visible)

    Display_Statistics()

if __name__ == "__main__":
    main()

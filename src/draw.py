import pygame as pg
from constants import *
from bars import get_bars_timsort


def draw_bar_graph(sort_info, screen, x, y, width, height, values):

    # Draw the background of the graph as a white rectangle
    pg.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    # Calculate the width of each bar
    bar_width = width // len(values)
    max_value = max(values)

    # Draw each bar
    for i in range(len(values)):
        # Ensure a minimum height of 1 for visibility
        bar_height = int((values[i] / max_value) * (height - 1)) + 1 if max_value > 0 else 1
        bar_x = x + i * bar_width
        bar_y = y + (height - bar_height)
        pg.draw.rect(screen, (247, 210, 57), (bar_x, bar_y, bar_width, bar_height))

    # Update the display
    pg.display.flip()


def draw_buttons(screen, sort_info, btn_type):
    if btn_type == 'menu':
        for btn in sort_info.menu_buttons_group:
            btn.update(FONT2, TEXT_COLOR1)
    elif btn_type == 'sort':
        for button in sort_info.sort_buttons_group:
            button.update(FONT2, TEXT_COLOR1)
    elif btn_type == 'order':
        for button in sort_info.order_buttons_group:
            button.update(FONT2, TEXT_COLOR1)
    elif btn_type == 'attribute':
        for button in sort_info.attribute_buttons_group:
            button.update(FONT2, TEXT_COLOR1)
    elif btn_type == 'Analyze':
        for button in sort_info.analyze_buttons_group:
            button.update(FONT2, TEXT_COLOR1)
<<<<<<< HEAD
    elif btn_type == 'Analyze2':
        for button in sort_info.analyze_buttons_group2:
            button.update(FONT2, TEXT_COLOR1)
=======
>>>>>>> feature-branch-testing


def draw_Analysis_results(screen, sort_info):
    screen.blit(BACKGROUND_IMAGE, (0,0))
    draw_text_with_outline(screen, FONT2, "Results", analyze_title_x, analyze_title_y, pg.Color('black'), pg.Color('white'), 2)
    draw_text_with_outline(screen, FONT2, "Below are the top 5 stocks", analyze_tips_x, analyze_tips_y, pg.Color('black'), pg.Color('white'), 2)
    
    names, values = zip(*sort_info.top_5)
    for i in range(5):
<<<<<<< HEAD
        draw_text_with_outline(screen, FONT2, f"{names[i]}: {values[i]}", (WINDOWSIZE[0]/6), 150 + 50 * i, pg.Color('black'), pg.Color('white'), 2)
    
    draw_text_with_outline(screen, FONT2, f"Heap Sort: {sort_info.heap_timer} Seconds", (WINDOWSIZE[0]/6), 150 + 50 * 6, pg.Color('black'), pg.Color('white'), 2)
    draw_text_with_outline(screen, FONT2, f"TimSort: {sort_info.timsort_timer} Seconds", (WINDOWSIZE[0]/6), 150 + 50 * 7, pg.Color('black'), pg.Color('white'), 2)
=======
        draw_text_with_outline(screen, FONT2, f"{names[i]}: {values[i]}", (WINDOWSIZE[0]/4), 150 + 50 * i, pg.Color('black'), pg.Color('white'), 2)
    
    draw_text_with_outline(screen, FONT2, f"Heap Sort: {sort_info.heap_timer}", (WINDOWSIZE[0]/4), 150 + 50 * 6, pg.Color('black'), pg.Color('white'), 2)
    draw_text_with_outline(screen, FONT2, f"TimSort: {sort_info.timsort_timer}", (WINDOWSIZE[0]/4), 150 + 50 * 7, pg.Color('black'), pg.Color('white'), 2)
>>>>>>> feature-branch-testing


def draw(screen, sort_info, bars=None, new_ele_idx=None, Category=None):

    if Category == 'Analyze':
        draw_Analysis_results(screen, sort_info)
        draw_buttons(screen, sort_info, btn_type='Analyze')
    else:
        screen.blit(BACKGROUND_IMAGE, (0,0)) 
        draw_text_with_outline(screen, FONT1, "Sorting Algorithm Visualizer", controls_menu, 5, pg.Color('white'), pg.Color('black'), 2)
        draw_text_with_outline(screen, FONT2, "Click on the buttons to select the sorting order and attribute", controls_menu-80, 5 + Menu_Title_fake.get_height() + 10, pg.Color('white'), pg.Color('black'),2)
        draw_buttons(screen, sort_info, btn_type='menu')

        # Draw the expanded dropdown menus if they are expanded
        if sort_info.sort_dropdown_expanded:
            draw_buttons(screen, sort_info, btn_type='sort')

        if sort_info.order_dropdown_expanded:
            draw_buttons(screen, sort_info, btn_type='order')

        if sort_info.attribute_dropdown_expanded:
            draw_buttons(screen, sort_info, btn_type='attribute')


def visualize_merge_step(screen, sort_info, runs, unsorted_lst, comparator, final=False):
    # Ensure runs and unsorted_lst are not empty
    if not runs and not unsorted_lst:
        return

    combined_list = []
    for run in runs:
        if isinstance(run, list):
            combined_list.extend(run)
    combined_list.extend(unsorted_lst)

    if not combined_list:
        return

    min_stock = min(combined_list, key=comparator)
    max_stock = max(combined_list, key=comparator)

    bars = get_bars_timsort(runs, unsorted_lst, SIDE_PAD, min_stock, max_stock, sort_info.selected_attribute, RUN_COLORS)
    if not sort_info.ascending:
        bars = bars[::-1]
    draw(screen, sort_info, bars)
    pg.display.update()
    if not final:
        pg.time.delay(50)  # Delay for visualization of each merge step


def disp_message(screen, text, font, color, x, y):
    message = font.render(text, True, color)
    message_rect = message.get_rect(center=(x, y))
    screen.blit(message, message_rect)


def draw_text_with_outline(screen, font, text, x, y, main_color, outline_color, outline_width=1):
    text_surface = font.render(text, True, main_color)
    outline_surfaces = []
    for dx, dy in [(-outline_width, -outline_width), (-outline_width, outline_width), (outline_width, -outline_width), (outline_width, outline_width)]:
        outline_surface = font.render(text, True, outline_color)
        outline_surfaces.append((outline_surface, (x + dx, y + dy)))

    for outline_surface, (ox, oy) in outline_surfaces:
        screen.blit(outline_surface, (ox, oy))

    screen.blit(text_surface, (x, y))
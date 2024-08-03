import pygame as pg
from constants import *
from bars import get_bars_timsort

''' draw_heap is for tree-based representation'''


def draw_heap(screen, sort_info, highlight=None, intermediate_positions=None):
    # Clear the screen before drawing
    screen.fill('light blue')

    for box in sort_info.boxes:
        box.draw()

    for node in sort_info.nodes:
        left_idx = 2 * node.idx + 1
        right_idx = 2 * node.idx + 2
        if left_idx < n:
            pg.draw.line(screen, 'black', node.center, sort_info.nodes[left_idx].center, 2)
        if right_idx < n:
            pg.draw.line(screen, 'black', node.center, sort_info.nodes[right_idx].center, 2)
    for node in sort_info.nodes:
        border_color = 'red' if highlight and node.idx in highlight else 'black'
        node.draw(border_color=border_color)

    # Draw the moving values
    if intermediate_positions:
        for idx, pos in intermediate_positions.items():
            node_val_surf = FONT3.render(str(sort_info.nodes[idx].val), True, 'black')
            node_val_rect = node_val_surf.get_rect(center=pos)
            screen.blit(node_val_surf, node_val_rect)

    pg.display.update()


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


def draw_bars(screen, bars, new_ele_idx=None):
    for i, (bar, color) in enumerate(bars):
        if i == new_ele_idx:
            bar_color = (255, 0, 0)
        else:
            bar_color = color if color else UNSORTED[i % 3]

        pg.draw.rect(screen, bar_color, bar)
        pg.draw.rect(screen, 'Blue', bar, 1)


def draw(screen, sort_info, bars=None, new_ele_idx=None):

    if bars is not None:
        screen.fill(BACKGROUND_COLOR)
        pg.draw.rect(screen, (169, 173, 76), (0, 0, WINDOWSIZE[0], sorting_bottom + 4), 4, 1)
        # pg.draw.line(screen, (169, 173, 76), (0, 100), (1800, 100), 4)
        draw_bars(screen, bars, new_ele_idx)
        # draw_buttons(screen, sort_info, btn_type='sort')

    else:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(Menu_Title, (controls_menu, 5))
        screen.blit(Menu_tips, (controls_menu-80, 5 + Menu_Title.get_height() + 10))
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
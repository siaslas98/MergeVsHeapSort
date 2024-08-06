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
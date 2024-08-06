import sys
from archive.box import Box
from sorting import *

def gen_boxes(screen, sort_info):
    for idx, val in enumerate(sort_info.list):
        box = Box(screen, val, idx, STARTING_X + BOX_WIDTH * idx, STARTING_Y, BOX_WIDTH, BOX_HEIGHT)
        sort_info.boxes.add(box)

def tree_sort_display(screen, sort_info, clock):
    running = True
    root_pos = (WINDOWSIZE[0] // 2, ROOT_Y_POS)

    while running:
        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                elif event.key == pg.K_SPACE:
                    build_heap(screen, sort_info, root_pos, clock)

        screen.fill('light blue')
        # Draw the array boxes at the top of the display
        for box in sort_info.boxes:
            box.draw()

        # Calculate center positions of nodes + create a list of node objects using these positions
        node_positions = calc_positions(root_pos, sort_info.list)
        sort_info.nodes = [Node(screen, val, idx, node_positions[idx], RADIUS) for idx, val in enumerate(sort_info.list)]

        # Draw edges
        for idx, pos in node_positions.items():
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2

            if left_idx in node_positions:
                pg.draw.line(screen, 'black', pos, node_positions[left_idx], 2)
            if right_idx in node_positions:
                pg.draw.line(screen, 'black', pos, node_positions[right_idx], 2)

        # Draw the nodes
        for idx, pos in node_positions.items():
            sort_info.nodes[idx].draw()

        # Update display
        pg.display.update()
        clock.tick(60)
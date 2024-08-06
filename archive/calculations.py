from constants import *
from collections import deque

''' ALL OF THIS CODE IS AN EXPERIMENT PLEASE IGNORE'''
def calc_positions(root_pos, node_vals_list):
    positions = {}
    queue = deque([(0, root_pos)])  # (idx, pos)
    levels = (len(node_vals_list)-1).bit_length()
    vert_spacing = (WINDOWSIZE[1] - 100) // (levels + 1)

    while queue:
        idx, (x, y) = queue.popleft()

        if idx < len(node_vals_list):
            positions[idx] = (x, y)

        # Calculate left child pos
        left_idx = 2 * idx + 1
        if left_idx < len(node_vals_list):
            left_x = x - WINDOWSIZE[0] // (2 ** ((idx + 1).bit_length() + 1))
            left_y = y + vert_spacing
            queue.append((left_idx, (left_x, left_y)))

        # Calculate right child position
        right_idx = 2 * idx + 2
        if right_idx < len(node_vals_list):
            right_x = x + WINDOWSIZE[0] // (2 ** ((idx + 1).bit_length() + 1))
            right_y = y + vert_spacing
            queue.append((right_idx, (right_x, right_y)))

    return positions


def interpolate(start, end, t):
    return start + (end - start) * t


def slide_values(screen, sort_info, parent_idx, largest_idx, steps, clock):
    from main import draw_heap
    parent_node = sort_info.nodes[parent_idx]
    largest_node = sort_info.nodes[largest_idx]

    start_parent_pos = pg.Vector2(parent_node.center)
    start_largest_pos = pg.Vector2(largest_node.center)

    for step in range(steps + 1):
        t = step / steps
        intermediate_pos_parent = interpolate(start_parent_pos, start_largest_pos, t)
        intermediate_pos_largest = interpolate(start_largest_pos, start_parent_pos, t)

        draw_heap(screen, sort_info, highlight={parent_idx, largest_idx}, intermediate_positions={
            parent_idx: intermediate_pos_parent,
            largest_idx: intermediate_pos_largest
        })
        pg.display.update()
        clock.tick(15)  # Adjust frame rate as needed

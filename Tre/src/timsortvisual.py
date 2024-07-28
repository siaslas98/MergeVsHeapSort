import pygame, sys

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Timsort")
text_font = pygame.font.SysFont('Arial', 30)

# fade animation for nice look
fade_counter = 0

# to control animations and prevent spamming errors
first_transition_started = None
first_transition_complete = False
second_transition_started = None
second_transition_complete = False
third_transition_started = None
third_transition_complete = False

# prevent rerender from deleting everything we drew
final_transition_surface = None

# algorithm walkthrough
sort_left_side = True
sort_right_side = False
left_side_sort_steps = [
    "08, 23, 12, 31",
    "08, 12, 23, 31"
]
current_left_side_step = 0

right_side_sort_steps = [
    "02, 04, 15, 29"
]
current_right_side_step = 0

merge_steps = [
    "02",
    "02, 04",
    "02, 04, 08",
    "02, 04, 08, 12",
    "02, 04, 08, 12, 15",
    "02, 04, 08, 12, 15, 23",
    "02, 04, 08, 12, 15, 23, 29",
    "02, 04, 08, 12, 15, 23, 29, 31"
]
current_merge_step = 0

clock = pygame.time.Clock()


def draw_arrow(
        surface: pygame.Surface,
        start: pygame.Vector2,
        end: pygame.Vector2,
        color: pygame.Color,
        body_width: int = 2,
        head_width: int = 4,
        head_height: int = 2,
):
    arrow = start - end
    angle = arrow.angle_to(pygame.Vector2(0, -1))
    body_length = arrow.length() - head_height

    head_verts = [
        pygame.Vector2(0, head_height / 2),  # Center
        pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
        pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
    ]
    # Rotate and translate the head into place
    translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
    for i in range(len(head_verts)):
        head_verts[i].rotate_ip(-angle)
        head_verts[i] += translation
        head_verts[i] += start

    pygame.draw.polygon(surface, color, head_verts)

    # Stop weird shapes when the arrow is shorter than arrow head
    if arrow.length() >= head_height:
        # Calculate the body rect, rotate and translate into place
        body_verts = [
            pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
            pygame.Vector2(body_width / 2, body_length / 2),  # Topright
            pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
            pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
        ]
        translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
        for i in range(len(body_verts)):
            body_verts[i].rotate_ip(-angle)
            body_verts[i] += translation
            body_verts[i] += start

        pygame.draw.polygon(surface, color, body_verts)


def draw_all_numbers(given_text, y, alpha, color=(0, 0, 0)):
    font = text_font
    text = font.render(given_text, True, color)
    text.set_alpha(alpha)
    text_rect = text.get_rect(center=(width / 2, y))
    screen.blit(text, text_rect)


def draw_split_numbers(given_text, x, y, alpha):
    font = text_font
    text = font.render(given_text, True, (0, 0, 0))
    text.set_alpha(alpha)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def clear_area(x, y, width, height):
    # to avoid overlapping
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))


def draw_first_arrows(alpha):
    arrow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    mid_top_left = pygame.Vector2(width / 2 - 75, 50 + 30)
    mid_top_right = pygame.Vector2(width / 2 + 75, 50 + 30)
    left_arrow_end = pygame.Vector2(width / 4, 120)
    right_arrow_end = pygame.Vector2(3 * width / 4, 120)
    color = pygame.Color(0, 0, 0, alpha)
    draw_arrow(arrow_surface, mid_top_left, left_arrow_end, color, 3, 7, 7)
    draw_arrow(arrow_surface, mid_top_right, right_arrow_end, color, 3, 7, 7)
    screen.blit(arrow_surface, (0, 0))


def draw_middle_arrow(alpha):
    arrow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    arrow_start = pygame.Vector2(width / 2, 175)
    arrow_end = pygame.Vector2(width / 2, 250)
    color = pygame.Color(0, 0, 0, alpha)
    draw_arrow(arrow_surface, arrow_start, arrow_end, color, 3, 7, 7)
    screen.blit(arrow_surface, (0, 0))


while True:
    # first transition is splitting numbers
    # second transition is insertion sort
    # third transition is merging
    screen.fill((255, 255, 255))
    draw_all_numbers("23, 12, 31, 08, 04, 15, 29, 02", 50, 255)

    if first_transition_started:
        transition = int(255 * (fade_counter / 100))
        draw_first_arrows(transition)
        left_coords = (width / 4, 140)
        right_coords = (3 * width / 4, 140)
        draw_split_numbers("23, 12, 31, 08", left_coords[0], left_coords[1], transition)
        draw_split_numbers("04, 15, 29, 02", right_coords[0], right_coords[1], transition)

        if fade_counter < 100:
            fade_counter += 5

        if fade_counter == 100:
            first_transition_started = False
            first_transition_complete = True
            final_transition_surface = screen.copy()
            fade_counter = 0

    if second_transition_started:
        screen.blit(final_transition_surface, (0, 0))
        left_coords = (width / 4, 140)
        right_coords = (3 * width / 4, 140)
        transition = int(255 * (fade_counter / 100))

        if sort_left_side:
            clear_area(left_coords[0] - 77, left_coords[1] - 17, 154, 35)
            draw_split_numbers(left_side_sort_steps[current_left_side_step],
                               left_coords[0], left_coords[1], transition)

        if sort_right_side:
            clear_area(right_coords[0] - 77, right_coords[1] - 17, 154, 35)
            draw_split_numbers(right_side_sort_steps[current_right_side_step],
                               right_coords[0], right_coords[1], transition)

        if fade_counter < 100:
            fade_counter += 4

        if fade_counter == 100:
            fade_counter = 0
            if sort_left_side:
                if current_left_side_step < len(left_side_sort_steps) - 1:
                    current_left_side_step += 1
                else:
                    sort_left_side = False
                    sort_right_side = True
                    final_transition_surface = screen.copy()

            elif sort_right_side:
                if current_right_side_step < len(right_side_sort_steps) - 1:
                    current_right_side_step += 1
                else:
                    second_transition_started = False
                    second_transition_complete = True
                    final_transition_surface = screen.copy()

    elif third_transition_started:
        screen.blit(final_transition_surface, (0, 0))
        transition = int(255 * (fade_counter / 100))
        draw_middle_arrow(transition)
        clear_area(0, 275, width, 50)
        draw_all_numbers(merge_steps[current_merge_step], 300, transition, (0, 128, 0))

        if fade_counter < 100:
            fade_counter += 4

        if fade_counter == 100:
            fade_counter = 0
            current_merge_step += 1
            if current_merge_step == len(merge_steps):
                third_transition_started = False
                final_transition_surface = screen.copy()

    elif final_transition_surface:
        screen.blit(final_transition_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # use space to forward the animation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if first_transition_started is None:
                    first_transition_started = True
                elif second_transition_started is None and first_transition_complete:
                    first_transition_started = False
                    second_transition_started = True
                elif third_transition_started is None and second_transition_complete:
                    second_transition_started = False
                    third_transition_started = True

    pygame.display.update()
    clock.tick(30)  # 30 fps

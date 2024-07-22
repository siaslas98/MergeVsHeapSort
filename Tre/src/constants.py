import pygame as pg

pg.init()

# Display size
#WINDOWSIZE = (900, 500)
WINDOWSIZE = (1800, 1000)

# Padding
TOTAL_SIDE_PAD = 100
SIDE_PAD = round(TOTAL_SIDE_PAD / 2)
TOP_PADDING = 100

# Colors
BACKGROUND_COLOR = (64, 64, 64)
TEXT_COLOR1 = (225, 223, 230)
TEXT_COLOR2 = (114, 118, 184)
SORTED = 'Green'
CURRENT = 'Blue'
UNSORTED = [(200, 200, 200), (128, 128, 128), (50, 50, 50)]

# Fonts
FONT1 = pg.font.SysFont('Arial Black', 50)
FONT2 = pg.font.SysFont('Arial Black', 30)

# Button positions
SORT_BEGIN = ((WINDOWSIZE[0]-434) / 2)
SORT = (SORT_BEGIN, round(0.95 * WINDOWSIZE[1]))
STOP = (SORT_BEGIN + 242, round(0.95 * WINDOWSIZE[1]))

# Image Dictionary
# Key is path, value is reference name
IMAGE_DICT = {'../imgs/Blank.png': 'Blank'}

# Additional button attributes
SCALE = 1
ELEVATION = 1.5

sorting_bottom = int(WINDOWSIZE[1] * 0.85)

basic_controls = FONT2.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, TEXT_COLOR1)
controls_x = WINDOWSIZE[0] / 2 - basic_controls.get_width()/2
sort_controls = FONT2.render("H - Heap Sort | M - Merge Sort", 1, TEXT_COLOR1)

# Sorting Range
n = 200
min_val = 50
max_val = 150

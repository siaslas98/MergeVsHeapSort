import pygame as pg

pg.init()

# Display size
WINDOWSIZE = (1200, 800)
#WINDOWSIZE = (1800, 1000)

# Padding for the sorting screen display
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
FONT3 = pg.font.SysFont('Arial Black', 18)
FONT4 = pg.font.SysFont('Arial Black', 17)

# This is for the input box on menu display
DROPDOWN_OFFSET = 50

ORDER_BUTTON = (263, 200)
ATTRIBUTE_BUTTON = (747, 200)
SUBMIT_BUTTON = (600 - 96, 500)
MAIN_MENU_BUTTON = (800, 100)

# Order positions
ASC = (ORDER_BUTTON[0], ORDER_BUTTON[1] + DROPDOWN_OFFSET)
DESC = (ORDER_BUTTON[0], ORDER_BUTTON[1] + 2 * DROPDOWN_OFFSET)

# Attribute positions
OPEN = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + DROPDOWN_OFFSET)
HIGH = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + 2 * DROPDOWN_OFFSET)
LOW = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + 3 * DROPDOWN_OFFSET)
CLOSE = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + 4 * DROPDOWN_OFFSET)
VOLUME = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + 5 * DROPDOWN_OFFSET)
OPENINT = (ATTRIBUTE_BUTTON[0], ATTRIBUTE_BUTTON[1] + 6 * DROPDOWN_OFFSET)

# Analyze button position
MAIN_MENU_BUTTON_POSITION = (MAIN_MENU_BUTTON[0], MAIN_MENU_BUTTON[1])


# Image Dictionary
# Key is path, value is reference name
IMAGE_DICT = {'../imgs/Blank.png': 'Blank'}

# Additional button attributes
SCALE = 1
ELEVATION = 1.5

# Define vertical offset between title and tips
TITLE_TO_TIPS_OFFSET = 20

sorting_bottom = int(WINDOWSIZE[1] * 0.85)

Menu_Title = FONT1.render("Sorting Algorithm Visualizer", 1, TEXT_COLOR1)
controls_menu = WINDOWSIZE[0] / 2 - Menu_Title.get_width()/2

Menu_tips = FONT2.render("Click on the buttons to select the sorting algorithm and order", 1, TEXT_COLOR1)
controls_menu_tips = controls_menu + Menu_Title.get_height() + TITLE_TO_TIPS_OFFSET


Loading_dialogue = FONT1.render("Sorting data...", 1, TEXT_COLOR1)
loading_text_x = WINDOWSIZE[0] / 2 - Loading_dialogue.get_width()/2
loading_text_y = WINDOWSIZE[1] / 2 - Loading_dialogue.get_height()/2

Analyze_Title = FONT1.render("Results", 1, TEXT_COLOR1)
analyze_title_x = WINDOWSIZE[0] / 2 - Analyze_Title.get_width()/2
analyze_title_y = 10

Analyze_tips = FONT2.render("Below are the top 5 stocks", 1, TEXT_COLOR1)
analyze_tips_x = WINDOWSIZE[0] / 2 - Analyze_tips.get_width()/2
analyze_tips_y = analyze_title_y + Analyze_Title.get_height() + TITLE_TO_TIPS_OFFSET

# Sorting
n = 100000

# Box Attributes + Node Attributes(Ignore this)
STARTING_X = 50
STARTING_Y = 50
BOX_WIDTH = (WINDOWSIZE[0] - 100) / 31
BOX_HEIGHT = 40
RADIUS = 25
BOX_TOP_PAD = 50
BOX_BOTTOM_PAD = 20
ROOT_Y_POS = BOX_TOP_PAD + BOX_BOTTOM_PAD + BOX_HEIGHT + RADIUS
VERT_SPACING = 150

# Input Box
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')

# Tim Sort
MIN_RUN_SIZE = 32
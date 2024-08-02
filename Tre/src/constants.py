import pygame as pg
from colors import *

#Initialize the color class
Colors = Colors()

# Function to render text with an outline
def render_text_with_outline(font, text, main_color, outline_color):
    base = font.render(text, True, outline_color)
    outline = pg.Surface((base.get_width() + 2, base.get_height() + 2), pg.SRCALPHA)
    outline.blit(font.render(text, True, outline_color), (0, 1))
    outline.blit(font.render(text, True, outline_color), (2, 1))
    outline.blit(font.render(text, True, outline_color), (1, 0))
    outline.blit(font.render(text, True, outline_color), (1, 2))
    outline.blit(font.render(text, True, main_color), (1, 1))
    return outline
    
def render_text_with_shadow(font, text, main_color, shadow_color, offset=(2, 2), shadow_thickness=3):
    # Create a surface for the text with shadow
    text_surface = font.render(text, True, main_color)
    width, height = text_surface.get_size()
    shadow_surface = pg.Surface((width + offset[0] * shadow_thickness, height + offset[1] * shadow_thickness), pg.SRCALPHA)
    
    # Render the shadow text multiple times to create a thicker shadow
    for i in range(shadow_thickness):
        shadow = font.render(text, True, shadow_color)
        shadow_surface.blit(shadow, (offset[0] * i, offset[1] * i))
    
    # Blit the main text onto the surface
    shadow_surface.blit(text_surface, (0, 0))
    return shadow_surface

pg.init()

info = pg.display.Info()
# Display size
WINDOWSIZE = (info.current_w, info.current_h)
#WINDOWSIZE = (1800, 1000)

# Padding
TOTAL_SIDE_PAD = 100
SIDE_PAD = round(TOTAL_SIDE_PAD / 2)
TOP_PADDING = 100


SORTED = 'Green'
CURRENT = 'Blue'
UNSORTED = [(200, 200, 200), (128, 128, 128), (50, 50, 50)]

# Fonts
Title_Font = pg.font.SysFont('Comic Sans MS', 80)
Tips_Font = pg.font.SysFont('Comic Sans MS', 40)
FONT1 = pg.font.SysFont('Arial Black', 50)
FONT2 = pg.font.SysFont('Arial Black', 30)
Button_Font = pg.font.SysFont('Arial Black', 25)


# Image Dictionary
# Key is path, value is reference name
IMAGE_DICT = {'imgs/Blank.png': 'Blank',
              'imgs/Rectangular/Green/Blank.png': 'Green',
              'imgs/Rectangular/Blue/Blank.png': 'Blue',
              'Background/Cash.jpg': 'Cash',
              'imgs/Buttons.png': 'Buttons',
              }

# Additional button attributes
SCALE = (400, 100)
ELEVATION = 1.5

Menu_Title = render_text_with_shadow(Title_Font, "Stock_Statistics", Colors.get_color('yellow_gold'), Colors.get_color('black'))
Menu_Tips = render_text_with_shadow(Tips_Font, "Click on the button to select the statistic, order, whether to visualize", Colors.get_color('yellow_gold'), Colors.get_color('black'))

# Button positions
SORT_BEGIN = ((WINDOWSIZE[0]-434) / 2)
SORT = (SORT_BEGIN, round(0.95 * WINDOWSIZE[1]))
STOP = (SORT_BEGIN + 242, round(0.95 * WINDOWSIZE[1]))
Menu_Title_Position = ((WINDOWSIZE[0] /2 - Menu_Title.get_width() /2), (20))
Menu_Tips_Position = ((WINDOWSIZE[0] / 2 - Menu_Tips.get_width() / 2), (Menu_Title.get_height() + 15))
high_button_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), Menu_Title_Position[1] + Menu_Tips_Position[1] + 50)
low_button_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), high_button_position[1] + 100)
percent_change_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), Menu_Title_Position[1] + Menu_Tips_Position[1] + 50)
price_change_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), percent_change_position[1] + 100)
week_52_Low_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), price_change_position[1] + 100)
week_52_High_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), week_52_Low_position[1] + 100)
market_cap_position = ((WINDOWSIZE[0] / 2) - (SCALE[0] / 2), week_52_High_position[1] + 100)

# Define bottom

sorting_bottom = int(WINDOWSIZE[1] * 0.85)

# Number of items to sort
n = 80
# Sorting Range
min_val = 10
max_val = 150

min_range = 0.5
max_range = 1000


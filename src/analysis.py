import pygame as pg
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt


# Initialize Pygame
pg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Analyze stocks with Matplotlib and Pygame")


class INFO:
    def __init__(self):
        self.start_date = ""
        self.end_date = ""
        self.input_active = False
        self.input_type = "start_date"
        self.start_date_text = "Enter Start Date: (YYYY-MM-DD)"
        self.end_date_text = "Enter End Date: (YYYY-MM-DD)"
        self.START_DATE_TEXT_POS = (50, 50)
        self.END_DATE_TEXT_POS = (50, 100)
        self.START_DATE_POS = (410, 45)  # Input box
        self.END_DATE_POS = (410, 95)  # Input box
        self.BASE_FONT = pg.font.Font(None, 30)  # Default pygame font
        self.ACTIVE_COLOR = pg.Color('dodgerblue2')
        self.PASSIVE_COLOR = pg.Color('lightskyblue3')
        self.MIN_BOX_WIDTH = 100

        self.input_boxes = {
            "start_date": pg.Rect(self.START_DATE_POS[0], self.START_DATE_POS[1], 210, 35),
            "end_date": pg.Rect(self.END_DATE_POS[0], self.END_DATE_POS[1], self.MIN_BOX_WIDTH, 35)
        }

        self.input_box_active = {
            "start_date": False,
            "end_date": False
        }


class Dropdown:
    def __init__(self, x, y, w, h, font, options):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('lightskyblue3')
        self.border_color = pg.Color('blue')
        self.border_width = 2
        self.default_text = "Choose Company"
        self.font = font
        self.options = options
        self.selected = None
        self.active = False
        self.option_rects = [pg.Rect(x, y + (i+1)*h, w, h) for i in range(len(options))]

    def draw(self, screen):
        # Draw border
        pg.draw.rect(screen, self.border_color, self.rect.inflate(self.border_width*2, self.border_width*2))

        pg.draw.rect(screen, self.color, self.rect)
        if self.selected is not None:
            selected_text = self.font.render(self.options[self.selected], True, (0, 0, 0))
            screen.blit(selected_text, (self.rect.x + 10, self.rect.y + 5))
        else:
            selected_text = self.font.render(self.default_text, True, (0, 0, 0))
            screen.blit(selected_text, (self.rect.x + 10, self.rect.y + 5))
        if self.active:
            for i, option in enumerate(self.options):
                pg.draw.rect(screen, self.color, self.option_rects[i])
                option_text = self.font.render(option, True, (0, 0, 0))
                screen.blit(option_text, (self.option_rects[i].x + 10, self.option_rects[i].y + 5))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            for i, option_rect in enumerate(self.option_rects):
                if option_rect.collidepoint(event.pos):
                    self.selected = i
                    self.active = False


class Button:
    def __init__(self, x, y, w, h, text, font, action=None):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('dodgerblue2')
        self.border_color = pg.Color('blue')
        self.border_width = 2
        self.font = font
        self.text = text
        self.action = action

    def draw(self, screen):
        # Draw border
        pg.draw.rect(screen, self.border_color, self.rect.inflate(self.border_width*2, self.border_width*2))
        pg.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()


def draw_input_boxes(screen, info, color=(255, 255, 255)):
    # Draw input box prompt
    start_text_surf = info.BASE_FONT.render(info.start_date_text, True, color)
    start_text_rect = start_text_surf.get_rect(topleft=info.START_DATE_TEXT_POS)
    screen.blit(start_text_surf, start_text_rect)

    end_text_surf = info.BASE_FONT.render(info.end_date_text, True, (255, 255, 255))
    end_text_rect = end_text_surf.get_rect(topleft=info.END_DATE_TEXT_POS)
    screen.blit(end_text_surf, end_text_rect)

    # Draw input box
    for key in info.input_boxes:
        color = info.ACTIVE_COLOR if info.input_box_active[key] else info.PASSIVE_COLOR
        pg.draw.rect(screen, color, info.input_boxes[key], 2)


# This is to check if the files within the provided list exists
def check_stock_files():
    # Path to the Stocks folder
    stocks_folder = '../Stocks'

    # List of company file names to check
    company_files = ['aapl.us.csv', 'msft.us.csv', 'amzn.us.csv', 'googl.us.csv', 'tsla.us.csv']

    # Check for each company file
    for file_name in company_files:
        file_path = os.path.join(stocks_folder, file_name)
        if os.path.isfile(file_path):
            print(f"File '{file_name}' exists in the '{stocks_folder}' folder.")
        else:
            print(f"File '{file_name}' does not exist in the '{stocks_folder}' folder.")


def analyze_action():
    print("Analyze button clicked!")
    # Perform further actions here

    if dropdown.selected is None:
        print("Please select a company.")
        return

    # Mapping of company names to their respective file names
    company_map = {
        'Apple': 'aapl',
        'Microsoft': 'msft',
        'Amazon': 'amzn',
        'Alphabet': 'googl',
        'Tesla': 'tsla'
    }

    # Assuming 'dropdown.selected' is the selected company index and 'dropdown.options' contains company names
    selected_company = dropdown.options[dropdown.selected].split(' ')[0]
    selected_company_file = company_map.get(selected_company, "").lower()
    start_date = info.start_date
    end_date = info.end_date

    if not selected_company_file or not start_date or not end_date:
        print("Please select a company and enter valid start and end dates.")
        return

    # Load data and filter by date range
    file_path = f'../Stocks/{selected_company_file}.us.csv'
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

        # Perform analysis (e.g., plot closing prices)
        plt.figure(figsize=(10, 5))
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.xlabel('Date',fontsize=14)
        plt.ylabel('Price',fontsize=14)
        plt.title(f'Closing Prices for {selected_company.upper()}')
        plt.legend(fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        # Save plot as a PNG file
        plot_filename = 'plot.png'
        plt.savefig(plot_filename)
        plt.close()

        global plot_image
        plot_image = pg.image.load(plot_filename)
        plot_image = pg.transform.scale(plot_image, (700,300))

    except Exception as e:
        print(f"Error loading or processing data: {e}")


def main():
    global info, dropdown, analyze_button, plot_image,  clock

    info = INFO()
    # check_stock_files()
    dropdown = Dropdown(50, 150, 200, 35, info.BASE_FONT, ['Apple (AAPL)', 'Microsoft (MSFT)', 'Amazon (AMZN)', 'Alphabet (GOOGL)', 'Tesla (TSLA)'])
    analyze_button = Button(270, 150, 150, 35, "Analyze", info.BASE_FONT, analyze_action)
    plot_image = None

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if info.input_active:
                    if event.key == pg.K_RETURN:
                        if info.input_type == "start_date":
                            info.input_type = ("end_date")
                            info.input_active = False
                            info.input_box_active["start_date"] = False
                        elif info.input_type == "end_date":
                            info.input_type = "start_date"
                            info.input_active = False
                            info.input_box_active["end_date"] = False

                    # Handles text deletion
                    elif event.key == pg.K_BACKSPACE:
                        if info.input_type == "start_date":
                            info.start_date = info.start_date[:-1]
                        elif info.input_type == "end_date":
                            info.end_date = info.end_date[:-1]
                    else:
                        if info.input_type == "start_date":
                            info.start_date += event.unicode
                            if len(info.start_date) > 10:  # Only allow 10 characters
                                info.start_date = info.start_date[:-1]
                            if len(info.start_date) == 4 or len(info.start_date) == 7:
                                info.start_date += '-'
                        elif info.input_type == "end_date":
                            info.end_date += event.unicode
                            if len(info.end_date) > 10:  # Only allow 10 characters
                                info.end_date = info.end_date[:-1]
                            if len(info.end_date) == 4 or len(info.end_date) == 7:
                                info.end_date += '-'

            if event.type == pg.MOUSEBUTTONDOWN:
                if not dropdown.handle_event(event):
                    for key in info.input_boxes:
                        if info.input_boxes[key].collidepoint(event.pos):
                            info.input_active = True
                            info.input_type = key
                            info.input_box_active[key] = True
                        else:
                            info.input_box_active[key] = False
                analyze_button.handle_event(event)

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_input_boxes(screen, info)
        dropdown.draw(screen)
        analyze_button.draw(screen)

        # Draw input text
        start_date_surf = info.BASE_FONT.render(info.start_date, True, (255, 255, 255))
        screen.blit(start_date_surf, (info.START_DATE_POS[0] + 5, info.START_DATE_POS[1] + 5))

        end_date_surf = info.BASE_FONT.render(info.end_date, True, (255, 255, 255))
        screen.blit(end_date_surf, (info.END_DATE_POS[0] + 5, info.END_DATE_POS[1] + 5))

        # Adjust the width of the input box based on the text width
        text_width = start_date_surf.get_width()
        info.input_boxes["start_date"].width = max(info.MIN_BOX_WIDTH, text_width + 10)

        end_text_width = end_date_surf.get_width()
        info.input_boxes["end_date"].width = max(info.MIN_BOX_WIDTH, end_text_width + 10)

        # Blit the plot image if it exists
        if plot_image:
            screen.blit(plot_image, (50, 250))

        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
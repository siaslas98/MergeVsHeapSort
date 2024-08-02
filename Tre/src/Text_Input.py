import pygame as pg
from datetime import datetime
from constants import *

class Text_Input_Box:
    def __init__(self, x, y, width, height, font, color_active=pg.Color('green'), color_inactive=pg.Color('blue'), text_color=pg.Color('black')):
        self.rect = pg.Rect(x, y, width, height)
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = color_inactive
        self.active = False
        self.font = font
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.final_text = None

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            
            if(self.active == True):
                self.color = self.color_active
            else:
                self.color = self.color_inactive

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.final_text = self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode


    def draw(self, screen):
            self.txt_surface = self.font.render(self.text, True, self.color)
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            pg.draw.rect(screen, self.color, self.rect, 2)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
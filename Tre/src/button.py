import pygame as pg
import constants as c
from images import *

class Button(pg.sprite.Sprite):
    def __init__(self, screen, images, name, x, y, scale, elevation):
        super().__init__()
        self.screen = screen
        self.name = name
        self.x_pos = x
        self.y_pos = y
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation

        # Background
        self.bg_surf = images.get_image('Blank')
        self.top_rect = self.bg_surf.get_rect(bottomleft=(self.x_pos, self.y_pos))
        self.top_rect_elevated = self.bg_surf.get_rect(bottomleft=(self.x_pos, self.y_pos - self.dynamic_elevation))
        self.bottom_rect = self.bg_surf.get_rect(bottomleft=(self.x_pos, self.y_pos + self.dynamic_elevation))

        # Text
        self.text_surf1 = c.FONT2.render(name, True, c.TEXT_COLOR1)
        self.text_surf2 = c.FONT2.render(name, True, c.TEXT_COLOR2)
        self.text_surf_ele = c.FONT2.render(name, True, c.TEXT_COLOR2)
        self.text_rect1 = self.text_surf1.get_rect(center=self.top_rect.center)
        self.text_rect2 = self.text_surf2.get_rect(center=self.top_rect.center)
        self.text_rect_ele = self.text_surf_ele.get_rect(center=self.top_rect_elevated.center)

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
                self.dynamic_elevation = 0
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation

    def draw_button_background(self):
        if self.pressed == True:
            self.screen.blit(self.bg_surf, self.top_rect)
        else:
            self.screen.blit(self.bg_surf, self.bottom_rect)
            self.screen.blit(self.bg_surf, self.top_rect_elevated)

    def draw_text(self, font, color):
        mouse_pos = pg.mouse.get_pos()
        if not self.top_rect.collidepoint(mouse_pos):
            self.screen.blit(self.text_surf1, self.text_rect1)
        else:
            if self.pressed:
                self.screen.blit(self.text_surf_ele, self.text_rect_ele)
            else:
                self.screen.blit(self.text_surf2, self.text_rect2)

    def update(self, font, color):
        self.draw_button_background()
        self.draw_text(font, color)
        self.check_click()

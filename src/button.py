import pygame as pg
import constants as c
from images import *


class Button(pg.sprite.Sprite):
    def __init__(self, screen, sort_info, name, x, y, scale, elevation):
        super().__init__()
        self.screen = screen  # Display window
        self.name = name  # Button name
        self.x_pos = x  # Button's top left x coordinate
        self.y_pos = y  # Button's top left y coordinate
        self.pressed = False  # State of whether button has been pressed
        self.elevation = elevation  # How elevated is the button
        self.scale = scale  # How much larger is the button image than the actual size
        self.dynamic_elevation = elevation

        # Background
        self.image = sort_info.images.get_image('Blank')
        self.image = pg.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))  # Assign to self.rect for compatibility

        self.top_rect = self.rect.copy()
        self.top_rect_elevated = self.rect.copy()
        self.top_rect_elevated.y -= self.dynamic_elevation
        self.bottom_rect = self.rect.copy()
        self.bottom_rect.y += self.dynamic_elevation

        # Text
        self.text_color = (255, 255, 255)  # White color
        self.text_surf1 = c.FONT2.render(name, True, self.text_color)
        self.text_surf2 = c.FONT2.render(name, True, self.text_color)
        self.text_surf_ele = c.FONT2.render(name, True, self.text_color)
        self.text_rect1 = self.text_surf1.get_rect(center=self.top_rect.center)
        self.text_rect2 = self.text_surf2.get_rect(center=self.top_rect.center)
        self.text_rect_ele = self.text_surf_ele.get_rect(center=self.top_rect_elevated.center)

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        left_mouse_pressed = pg.mouse.get_pressed()[0]

        if self.top_rect.collidepoint(mouse_pos):
            if left_mouse_pressed and not self.pressed:
                self.pressed = True
                return True
            elif left_mouse_pressed and self.pressed:
                self.pressed = False
                self.dynamic_elevation = self.elevation
                return False
        else:
            self.pressed = False

        return False

    def draw_button_background(self):
        if self.pressed:
            self.screen.blit(self.image, self.top_rect)
        else:
            self.screen.blit(self.image, self.bottom_rect)
            self.screen.blit(self.image, self.top_rect_elevated)

    def change_button_name(self, text):
        self.text_color = (255, 255, 255)  # White color
        self.text_surf1 = c.FONT2.render(text, True, self.text_color)
        self.text_surf2 = c.FONT2.render(text, True, self.text_color)
        self.text_surf_ele = c.FONT2.render(text, True, self.text_color)
        self.text_rect1 = self.text_surf1.get_rect(center=self.top_rect.center)
        self.text_rect2 = self.text_surf2.get_rect(center=self.top_rect.center)
        self.text_rect_ele = self.text_surf_ele.get_rect(center=self.top_rect_elevated.center)

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
        return self.check_click()

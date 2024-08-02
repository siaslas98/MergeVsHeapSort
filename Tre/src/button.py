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
        self.bg_surf = images.get_image('Buttons')
        self.bg_surf = pg.transform.scale(self.bg_surf, scale)  # Scale the image
        self.image = self.bg_surf  # Assign to self.image for compatibility with pygame.sprite.Sprite
        self.rect = self.bg_surf.get_rect(topleft=(self.x_pos, self.y_pos))  # Assign to self.rect for compatibility

        self.top_rect = self.rect.copy()
        self.top_rect_elevated = self.rect.copy()
        self.top_rect_elevated.y -= self.dynamic_elevation
        self.bottom_rect = self.rect.copy()
        self.bottom_rect.y += self.dynamic_elevation

        # Text
        self.text_color = c.Colors.get_color('black')  # black color
        self.text_surf1 = c.Button_Font.render(name, True, self.text_color)
        self.text_surf2 = c.Button_Font.render(name, True, self.text_color)
        self.text_surf_ele = c.Button_Font.render(name, True, self.text_color)

        # Center the text within the button

        self.text_rect1 = self.text_surf1.get_rect(center = (self.rect.center[0],(self.rect.center[1] - 10)))
        self.text_rect2 = self.text_surf2.get_rect(center=self.rect.center)
        self.text_rect_ele = self.text_surf_ele.get_rect(center= ((self.top_rect_elevated.center),))


    def check_if_clicked(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def draw_button_background(self):
        if self.pressed:
            self.screen.blit(self.bg_surf, self.top_rect)
        else:
            self.screen.blit(self.bg_surf, self.bottom_rect)
            self.screen.blit(self.bg_surf, self.top_rect_elevated)

    def draw_text(self, font, color):
        self.screen.blit(self.text_surf1, self.text_rect1)
        
    def update(self, font, color):
        self.draw_button_background()
        self.draw_text(font, color)
        self.check_if_clicked()

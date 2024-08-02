import pygame as pg
from constants import *


class Box(pg.sprite.Sprite):
    def __init__(self, screen, val, idx, x, y, box_width, box_height):
        super().__init__()
        self.screen = screen
        self.val = str(val)
        self.idx = idx
        self.image = pg.Surface((box_width, box_height))
        self.image.fill('White')
        self.rect = self.image.get_rect(topleft=(x,y))

        # Render the text for the array value
        box_info = FONT3.render(self.val, True, 'Black')
        box_info_rect = box_info.get_rect(center=(box_width // 2, box_height // 2))
        self.image.blit(box_info, box_info_rect)

        # Render the text for the index
        self.index_info = FONT3.render(str(self.idx), True, 'Orange')
        self.index_info_rect = self.index_info.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))
        # self.screen.blit(self.index_info, self.index_info_rect)

    def update_text(self):
        self.image.fill('White')  # Clear the previous value
        box_info = FONT3.render(self.val, True, 'Black')
        box_info_rect = box_info.get_rect(center=(BOX_WIDTH // 2, BOX_HEIGHT// 2))
        self.image.blit(box_info, box_info_rect)

    def update_val(self, new_val):
        self.val = str(new_val)
        self.update_text()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        pg.draw.rect(self.screen, 'Black', self.rect,2)
        self.screen.blit(self.index_info, self.index_info_rect)


class InputBox(pg.sprite.Sprite):
    def __init__(self, w, h, text=''):
        super().__init__()
        self.rect = pg.Rect(0, 0, w, h)
        self.rect.center = (WINDOWSIZE[0] // 2, WINDOWSIZE[1] // 2)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT4.render(text, True, self.color)
        self.active = False
        self.max_length = 10

    def handle_event(self, event, sort_info):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    if len(self.text) == 10:
                        sort_info.date = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.max_length:
                        self.text += event.unicode
                    if len(self.text) == 4 or len(self.text) == 7:
                        self.text += '-'

                self.txt_surface = FONT4.render(self.text, True, self.color)




    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
        self.rect.center = (WINDOWSIZE[0] // 2, WINDOWSIZE[1] // 2)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)
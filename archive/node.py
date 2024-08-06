import pygame as pg
from constants import FONT3, RADIUS, n


class Node(pg.sprite.Sprite):
    def __init__(self, screen, val, idx, center, radius=RADIUS):
        super().__init__()
        self.screen = screen
        self.val = val
        self.idx = idx
        self.center = center
        self.radius = radius

    def draw(self, fill_color='orange2', border_color='black'):
        node_val_surf = FONT3.render(str(self.val), True, 'black')
        node_val_rect = node_val_surf.get_rect(center=self.center)
        pg.draw.circle(self.screen, fill_color, self.center, RADIUS)
        pg.draw.circle(self.screen, border_color, self.center, RADIUS, 4)
        self.screen.blit(node_val_surf, node_val_rect)


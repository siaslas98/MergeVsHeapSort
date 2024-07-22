import pygame as pg
from constants import IMAGE_DICT


class Images:
    def __init__(self):
        self.images = {}
        self.load()

    def load_image(self, path, name):
        self.images[name] = pg.image.load(path).convert_alpha()

    def load(self):
        for path, name in IMAGE_DICT.items():
            self.load_image(path, name)

    def get_image(self, name):
        return self.images[name]


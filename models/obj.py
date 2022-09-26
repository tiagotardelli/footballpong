import pygame as pg


class Obj:

    def __init__(self, image, x, y):

        self.image = pg.image.load(image)
        self.react = self.image.get_rect()
        self.react[0] = x
        self.react[1] = y

    def drawing(self, window):

        window.blit(self.image, (self.react[0], self.react[1]))

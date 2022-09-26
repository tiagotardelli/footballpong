import pygame as pg


class Window:

    def __init__(self, x, y, title):

        pg.init()

        self.window = pg.display.set_mode([x, y])
        self.title = pg.display.set_caption(title)

        self.loop = True

        self.list_obj = []

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.loop = False

    def add_obj(self, item):
        self.list_obj.append(item)

    def updates(self):

        while self.loop:
            self.events()
            pg.display.update()

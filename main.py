import pygame as pg

pg.init()

windows = pg.display.set_mode([1280,720])
title = pg.display.set_caption("Football Pong")

loop = True
while loop:

    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False

    pg.display.update()
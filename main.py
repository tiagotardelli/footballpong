import pygame as pg

pg.init()

window = pg.display.set_mode([1280,720])
title = pg.display.set_caption("Football Pong")
field = pg.image.load("assets/field.png")
window.blit(field,(0,0))

loop = True
while loop:

    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False

    pg.display.update()
from tkinter.tix import Balloon
import pygame as pg

pg.init()

window = pg.display.set_mode([1280,720])
title = pg.display.set_caption("Football Pong")

field = pg.image.load("assets/field.png")
window.blit(field,(0,0))

player1 = pg.image.load("assets/player1.png")
window.blit(player1, (50,310))

player2 = pg.image.load("assets/player2.png")
window.blit(player2, (1150,310))

ball = pg.image.load("assets/ball.png")
window.blit(ball, (617,337))

loop = True
while loop:

    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False

    pg.display.update()
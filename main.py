import pygame as pg

pg.init()

window = pg.display.set_mode([1280, 720])
title = pg.display.set_caption("Football Pong")

field = pg.image.load("assets/field.png")

player1 = pg.image.load("assets/player1.png")

player2 = pg.image.load("assets/player2.png")

ball = pg.image.load("assets/ball.png")
ball_xy = {"x": 617, "y": 337}


def move_ball(none):
    global ball_xy

    ball_xy["x"] += 1


def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, 310))
    window.blit(player2, (1150, 310))
    window.blit(ball, (ball_xy["x"], ball_xy["y"]))


loop = True
while loop:

    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False

    draw()
    move_ball()
    pg.display.update()

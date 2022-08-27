import pygame as pg

pg.init()

window = pg.display.set_mode([1280, 720])
title = pg.display.set_caption("Football Pong")

field = pg.image.load("assets/field.png")

player1 = pg.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False


player2 = pg.image.load("assets/player2.png")

ball = pg.image.load("assets/ball.png")
ball_x = 617
ball_y = 337


def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0


def move_ball():
    global ball_x

    ball_x += 1


def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, 310))
    window.blit(ball, (ball_x, ball_y))


loop = True
while loop:

    for events in pg.event.get():
        if events.type == pg.QUIT:
            loop = False
        if events.type == pg.KEYDOWN:
            if events.key == pg.K_w:
                player1_moveup = True
            if events.key == pg.K_s:
                player1_movedown = True
        if events.type == pg.KEYUP:
            if events.key == pg.K_w:
                player1_moveup = False
            if events.key == pg.K_s:
                player1_movedown = False

    draw()
    move_ball()
    move_player()
    pg.display.update()

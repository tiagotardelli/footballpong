import pygame as pg

pg.init()

window = pg.display.set_mode([1280, 720])
title = pg.display.set_caption("Football Pong")

win = pg.image.load("assets/win.png")

score1 = 0
score1_img = pg.image.load("assets/score/0.png")
score2 = 0
score2_img = pg.image.load("assets/score/0.png")

field = pg.image.load("assets/field.png")

player1 = pg.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False


player2 = pg.image.load("assets/player2.png")
player2_y = 310

ball = pg.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1


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

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575


def move_player2():
    global player2_y
    player2_y = ball_y


def move_ball():
    global ball_x, ball_y
    global ball_dir, ball_dir_y
    global score1, score2
    global score1_img, score2_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 700:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if ball_x <= -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= 1
        score2 += 1
        score2_img = pg.image.load(f"assets/score/{str(score2)}.png")

    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= 1
        score1 += 1
        score1_img = pg.image.load(f"assets/score/{str(score1)}.png")


def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))


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

    pg.display.update()

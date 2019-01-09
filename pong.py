# Creato da AndreaErario nel 2018

import pygame
import random

pygame.init()

# Create Window
win = pygame.display.set_mode((800, 500))
icon = pygame.image.load("pong_icon.png")
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)

# Classes of the objects
class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 200
        self.widht = 20
        self.collision = False
        self.score = 0

class ball(object):
    def __init__(self, radius):
        self.x = 300
        self.y = 250
        self.radius = radius
        self.direction = 0
        self.default_way = random.choice([1, -1])


# Important variables
player1 = player(2, 150)
player2 = player(778, 150)
ball = ball(10)
run = True
draw_ball = True
game = True
font = pygame.font.SysFont("Times New Roman", 18)

# Main Loop
while run:
    
    # Exit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Players Movement
    keys = pygame.key.get_pressed()
    if game == True:
        if keys[pygame.K_w] and player1.y > 0:
            player1.y -= 0.5
        
        if keys[pygame.K_s] and player1.y < 500 - player1.height:
            player1.y += 0.5

        if keys[pygame.K_UP] and player2.y > 0:
            player2.y -= 0.5
        
        if keys[pygame.K_DOWN] and player2.y < 500 - player2.height:
            player2.y += 0.5
    
    if game:
        if keys[pygame.K_ESCAPE]:
            game = False
    if not game:
        if keys[pygame.K_RETURN]:
            game = True
            

    # Collisions
    if game == True:
        if ball.x == player1.x + ball.radius :
            if ball.y - ball.radius < player1.y + player1.height and ball.y + ball.radius > player1.y:
                player1.collision = True
                player2.collision = False
        if ball.x == player2.x - ball.radius:
            if ball.y - ball.radius < player2.y + player2.height and ball.y + ball.radius > player2.y:
                player2.collision = True
                player1.collision = False
        
        if ball.y == 0 + ball.radius:
            ball.direction = 1
        if ball.y == 500 - ball.radius:
            ball.direction = -1
        if ball.direction == 1:
            ball.y += 1
        if ball.direction == -1:
            ball.y -= 1

        if player1.collision == False and player2.collision == False:
            ball.x += ball.default_way
        if player1.collision == True and player2.collision == False: 
            if ball.direction == 0:
                ball.direction = 1
            ball.x += 1
            player2.collision = False
        if player2.collision == True and player1.collision == False:
            if ball.direction == 0:
                ball.direction = -1
            ball.x -= 1
            player1.collision = False

    # Reset Ball and add Score
    if ball.x == player2.x + ball.radius:
        draw_ball = False
        ball.x = 300
        ball.y = int(player2.y + 100)
        player1.collision = False
        player2.collision = False
        ball.direction = 0
        draw_ball = True
        ball.default_way = 1
        player1.score += 1
    if ball.x == player1.x - ball.radius:
        draw_ball = False
        ball.x = 300
        ball.y = int(player1.y + 100)
        player1.collision = False
        player2.collision = False
        ball.direction = 0
        draw_ball = True
        ball.default_way = -1
        player2.score += 1
    
    # Drawings
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255), (player1.x, player1.y, player1.widht, player1.height))
    pygame.draw.rect(win, (255, 255, 255), (player2.x, player2.y, player2.widht, player2.height))
    score = font.render("Player1: {}  Player2: {}".format(player1.score, player2.score), 1, (255,255,255))
    win.blit(score, (320, 0))
    if draw_ball == True:
        pygame.draw.circle(win, (255, 255, 255), (ball.x, ball.y), ball.radius)
    if game == True:
        esc = font.render("ESC", 1, (255,255,255))
        win.blit(esc, (0,0))
    if game == False:
        pause = font.render("Il Gioco è in pausa, Premi Invio per continuare", 1, (255, 255, 255))
        win.blit(pause, (235,20))
    pygame.display.update()

pygame.quit()
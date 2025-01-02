#ADJUST VARIABLES AS NEEDED
#physics constants
friction = 0.05
speed = 0.1

#window size
window_x = 1200
windox_y = 1200

import pygame
from pygame import gfxdraw

pygame.init()

class colours:
    white = (240,240,240)
    black = (0,0,0)

class playerClass:
    accelx = 0
    accely = 0
    velx = 0
    vely = 0
    x = 450.0
    y = 450.0

def renderCircle(obj,size):
    pygame.gfxdraw.aacircle(window,int(obj.x),int(obj.y),size,globalColours.black)
    pygame.gfxdraw.filled_circle(window,int(obj.x),int(obj.y),size,globalColours.black)

def playerPhysics(obj):
    obj.velx += obj.accelx
    obj.vely += obj.accely

    # add friction to velocity
    if not(-0.001 < obj.velx < 0.001):
        if obj.velx > 0:
            obj.velx -= friction
        elif obj.velx < 0:
            obj.velx += friction

    if not(-0.001 < obj.vely < 0.001):
        if obj.vely > 0:
            obj.vely -= friction
        elif obj.vely < 0:
            obj.vely += friction

    #bound in box
    if not(0 <= (obj.x + obj.velx) <= window_x):
        obj.velx = -obj.velx
    if not(0 <= (obj.y + obj.vely) <= windox_y):
        obj.vely = -obj.vely

    obj.x += obj.velx
    obj.y += obj.vely

    return obj

globalColours = colours()

clock = pygame.time.Clock()

window = pygame.display.set_mode((window_x,windox_y))
pygame.display.set_caption("2d physics sim")

run = True

player = playerClass()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.accelx = -speed
    elif keys[pygame.K_RIGHT]:
        player.accelx = speed
    else:
        player.accelx = 0
    if keys[pygame.K_UP]:
        player.accely = -speed
    elif keys[pygame.K_DOWN]:
        player.accely = speed
    else:
        player.accely = 0
        
    print(f"\nBall (x,y):\n   position = ({round(player.x,2)},{round(player.y,2)})\n   velocity = ({round(player.velx,2)},{round(player.vely,2)})\n   acceleration = ({player.accelx},{player.accely})")

    window.fill(globalColours.white)

    player = playerPhysics(player)

    renderCircle(player,30)

    pygame.display.update()
    clock.tick(60)
pygame.quit()

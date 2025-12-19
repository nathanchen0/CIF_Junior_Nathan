import pygame
pygame.init()

import random

#set a bunch of random colours
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

colour_change_event = pygame.USEREVENT + 1
pygame.time.set_timer(colour_change_event, 2000)  # Change colour every 2 seconds

width = 800
height = 600

boxwidth = 30
boxheight = 30

box_x = 0
box_y = 0
box_x_change = 0
box_y_change = 0

colour_list = [red, orange, yellow, green, blue, purple]
box_colour = random.choice(colour_list)

delta = 5

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
#make the box move with WASD keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                box_x_change = delta
            if event.key == pygame.K_a:
                box_x_change = -delta
            if event.key == pygame.K_w:
                box_y_change = -delta
            if event.key == pygame.K_s:
                box_y_change = delta
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                box_x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                box_y_change = 0
        elif event.type == colour_change_event:
            box_colour = random.choice(colour_list)
    box_x += box_x_change 
    box_y += box_y_change 
    if box_x + boxwidth > width:
        box_x = width - boxwidth
    if box_x < 0:
        box_x = 0
    if box_y + boxheight > height:
        box_y = height - boxheight
    if box_y < 0:
        box_y = 0
    # drawing the boxes
    rect1 = pygame.Rect(box_x, box_y, boxwidth, boxheight)
    pygame.draw.rect(screen, box_colour, rect1)
    pygame.display.update()
    screen.fill(black)

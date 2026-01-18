import pygame
import random
pygame.init()


#set a bunch of random colours
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
pink = (255, 192, 203)

width = 800
height = 800

boxwidth = 30
boxheight = 30
maze_boxwidth = 50
maze_boxheight = 50


myfont = pygame.font.SysFont('Arial', 30)

#setup moving box and series of boxes to make a maze
box_x = 0
box_y = 0
box_x_change = 0
box_y_change = 0

colour_list = [orange, yellow, purple, pink]
box_colour = random.choice(colour_list)

delta = 5

screen = pygame.display.set_mode((width, height))


tilesize = 61

tiles = ['empty', 'wall', 'goal', 'player_start']

#define a random maze layout using a 2D list (0 = empty, 1 = wall, 2 = goal, 3 = player start)
maze = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
maze2 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
]
maze3 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
maze4 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
gamemap = random.choice([maze, maze2, maze3, maze4])
maze = gamemap
mazeboxlist = []
#draw the maze based on the 2D list with lens to find the amount of tiles
def draw():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = maze[row][col]
            if tile == 1:  # wall
                pygame.draw.rect(screen, blue, (col * tilesize, row * tilesize, tilesize, tilesize))
                mazeboxlist.append((col, row))
            elif tile == 2:  # goal
                pygame.draw.rect(screen, green, (col * tilesize, row * tilesize, tilesize, tilesize))
                global goal_pos
                goal_pos = pygame.Rect(col * tilesize, row * tilesize, tilesize, tilesize)
                #remeber this position for collision detection
            elif tile == 3:  # player start
                pygame.draw.rect(screen, red, (col * tilesize, row * tilesize, tilesize, tilesize))


clock = pygame.time.Clock()
playing = True
while playing:
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
    draw()
    # drawing the player box
    rect1 = pygame.Rect(box_x, box_y, boxwidth, boxheight)
    pygame.draw.rect(screen, box_colour, rect1)
    #make it so the player cannot go through walls
    for wall in mazeboxlist:
        if rect1.colliderect(pygame.Rect(wall[0] * tilesize, wall[1] * tilesize, tilesize, tilesize)):
            playing = False
    if rect1.colliderect(goal_pos):
        textsurface = myfont.render('You Win!', False, (255, 255, 255))
        screen.blit(textsurface, (350, 400))
        playing = False
    pygame.display.update()
    screen.fill(black)

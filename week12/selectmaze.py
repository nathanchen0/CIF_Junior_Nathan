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

#set variables for instruction page and boxes
width = 800
height = 800

boxwidth = 30
boxheight = 30
maze_boxwidth = 50
maze_boxheight = 50

instruction = 1
collected = 0

myfont = pygame.font.SysFont('Arial', 50)

#setup moving box and series of boxes to make a maze
box_x = 0
box_y = 0
box_x_change = 0
box_y_change = 0

colour_list = [orange, purple, pink]
box_colour = random.choice(colour_list)

delta = 5

screen = pygame.display.set_mode((width, height))


tilesize = 61
coinsize = 40
coincount1 = 18
coincount2 = 26
coincount3 = 22
coincount4 = 27

tiles = ['empty', 'wall', 'goal', 'player_start', 'coin']

#define a random maze layout using a 2D list (0 = empty, 1 = wall, 2 = goal, 3 = player start, 4 = coin)
maze1 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 4, 4, 1, 0, 0, 0, 0, 4, 4, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 4, 4, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 4, 4, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 4, 4, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 4, 4, 1, 4, 4, 4, 4, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
maze2 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 4, 4, 4, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 4, 4, 4, 1, 1, 0, 1, 0, 1],
    [1, 4, 1, 1, 1, 1, 4, 1, 1, 0, 1, 0, 1],
    [1, 4, 4, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 4, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 4, 1, 4, 4, 4, 4, 4, 0, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 4, 4, 1, 0, 4, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
]
maze3 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 4, 4, 4, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 4, 4, 4, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 4, 4, 4, 4, 0, 4, 4, 4, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 4, 4, 0, 0, 4, 4, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 2],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
maze4 = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1],
    [1, 0, 0, 0, 4, 4, 4, 4, 4, 0, 1, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 1],
    [1, 4, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 4, 4, 4, 0, 0, 0, 0, 4, 4, 4, 4, 1],
    [1, 1, 1, 1, 0, 1, 1, 4, 1, 1, 1, 1, 1],
    [1, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
#let the user select a maze
selectscreen = int(input("Select screen number (1-4): "))
if selectscreen == 1:
    maze = maze1
elif selectscreen == 2:
    maze = maze2
elif selectscreen == 3:
    maze = maze3
elif selectscreen == 4:
    maze = maze4
#gamemap = maze #uncomment this line to use the same maze every time for testing
gamemap = maze
global coincount
if gamemap == maze1:
    coincount = coincount1
elif gamemap == maze2:
    coincount = coincount2
elif gamemap == maze3:
    coincount = coincount3
elif gamemap == maze4:
    coincount = coincount4
coincount = int(coincount)
print("Total coins in this maze:", coincount)
mazeboxlist = []
coinlist = []
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
            elif tile == 4: #coin
                #have the coin centered in the tile
                pygame.draw.circle(screen, yellow, (col * tilesize + (28), row * tilesize + (30)), coinsize // 2)
                global coin_pos
                coin_pos = pygame.Rect(col * tilesize + (tilesize - coinsize) // 2, row * tilesize + (tilesize - coinsize) // 2, coinsize, coinsize)
                #remeber this position for coin detection
                coinlist.append(coin_pos)

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
    #make an instructions page
    if instruction == 1:
        instructions = myfont.render('Use WASD to move and get coins!', False, (255, 255, 255))
        screen.blit(instructions, (10, 300))
        instructions2 = myfont.render('Reach the green square to win!', False, (255, 255, 255))
        screen.blit(instructions2, (10, 360))
        pygame.display.update()
        pygame.time.delay(3000)
        instruction = 0
    draw()
    # drawing the player box
    rect1 = pygame.Rect(box_x, box_y, boxwidth, boxheight)
    pygame.draw.rect(screen, box_colour, rect1)
    #display elapsed time once per second
    runtime = pygame.time.get_ticks() // 1000 - 3
    #make it so the player cannot go through walls
    for wall in mazeboxlist:
        if rect1.colliderect(pygame.Rect(wall[0] * tilesize, wall[1] * tilesize, tilesize, tilesize)):
            playing = False
    #check for collecting coins and make them disappear and add to collected count
    for coin in coinlist:
        if rect1.colliderect(coin):
           if maze[coin.y // tilesize][coin.x // tilesize] > 0:
                maze[coin.y // tilesize][coin.x // tilesize] = 0
                coinlist.remove(coin)
                collected += 1
                print("Coins collected:", collected)
    #check for reaching the goal and having all coins collected
    if rect1.colliderect(goal_pos):
        if coincount == collected:
            print("You win! Time:", runtime, "seconds")
            textsurface = myfont.render('You Win! Time: ' + str(runtime) + 's', False, (255, 255, 255))
            screen.blit(textsurface, (200, 400))
            runtime = "none"
            pygame.display.update()
            pygame.time.delay(3000)
            playing = False
        else:
            textsurface = myfont.render('Collect all coins first!', False, (255, 255, 255))
            screen.blit(textsurface, (200, 400))
    pygame.display.update()
    screen.fill(black)

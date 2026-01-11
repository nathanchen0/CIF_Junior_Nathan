import pygame
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

myfont = pygame.font.SysFont('Arial', 30)

#setup moving box and a box in the middle
box_x = 0
box_y = 0
box_x2 = width // 2
box_y2 = height // 2
box_x_change = 0
box_y_change = 0

colour_list = [red, orange, yellow, green, blue, purple]
box_colour = pink
box2_colour = green

delta = 5

screen = pygame.display.set_mode((width, height))

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
    # drawing the boxes
    rect1 = pygame.Rect(box_x, box_y, boxwidth, boxheight)
    rect2 = pygame.Rect(box_x2, box_y2, boxwidth, boxheight)
    # check for collision and make sure the boxes do not overlap
    if rect1.colliderect(rect2):
        textsurface = myfont.render('Collision detected!', False, (255, 255, 255))
        screen.blit(textsurface, (0, 750))
        box2_colour = blue
        box_x = box_x - box_x_change
        box_y = box_y - box_y_change
    #change the colour of box2 back to green if no collision
    else:
        box2_colour = green
    pygame.draw.rect(screen, box2_colour, rect2)
    pygame.draw.rect(screen, box_colour, rect1)
    textsurface = myfont.render('Hit the box!', False, (255, 255, 255))
    screen.blit(textsurface, (335, 0))


    pygame.display.update()
    screen.fill(black)

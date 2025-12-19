import pygame
pygame.init()

red = (255, 0, 0)
black = (0, 0, 0)

width = 1000
height = 800

boxwidth = 30
boxheight = 30

box_x = 0
box_y = 0
box_x2 = 750
box_y2 = 0

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#make the box move with WASD keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box_x += 5
    if keys[pygame.K_a]:
        box_x -= 5
    if keys[pygame.K_w]:
        box_y -= 5
    if keys[pygame.K_s]:
        box_y += 5
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
    pygame.draw.rect(screen, red, rect1)
    pygame.display.update()
    screen.fill(black)

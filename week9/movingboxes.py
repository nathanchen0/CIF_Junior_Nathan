import pygame
pygame.init()

green = (0, 255, 0)  
purple = (255, 0, 255) 
black = (0, 0, 0)

width = 800
height = 600

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
    if box_x + 30 > width:
        box_x = width - 30

    if box_x < 0:
        box_x = 0
      
    box_x += 2
    box_x2 -= 2

    # drawing the boxes
    rect1 = pygame.Rect(box_x2, box_y, 30, 30)
    rect2 = pygame.Rect(box_x, box_y2, 30, 30)
    pygame.draw.rect(screen, purple, rect1)
    pygame.draw.rect(screen, green, rect2)
    pygame.display.update()
    screen.fill(black)

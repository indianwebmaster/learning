import time
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

r,g,b = 0,128,255
circleXY = (250,250)
circleRadius = 250
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    screen.fill((r, g, b))
    r,g,b = g,b,r

    pygame.draw.circle(screen, (r,g,b), circleXY, circleRadius)

    pygame.display.flip()
    time.sleep(1)

pygame.quit()

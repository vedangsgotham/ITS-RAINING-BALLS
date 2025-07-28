import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trynna do smth")


White = (100, 100, 100)
Red = (255, 0, 0)


Ball_x = 200
Ball_y = 000
Ball_radius = 20
Ball_v=0
Ball_a=0.2

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Ball_v+=Ball_a
    Ball_y+=Ball_v
    if Ball_y > 600:
        Ball_y = 0
        Ball_x = random.randint(0,800)
    

    screen.fill(White)
    pygame.draw.circle(screen, Red, (Ball_x, Ball_y), Ball_radius)  
    pygame.display.update()  
    clock.tick(80)

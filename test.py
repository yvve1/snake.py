import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
#pygame.display.set_mode((500,500), )
clock = pygame.time.Clock()
keys2 = 0

while True:
    screen.fill('black')
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            keys2 = 1
        if event.type == pygame.KEYUP:
            keys2 = 0
    
    if keys2:
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
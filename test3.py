import pygame
from sys import exit
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

item = pygame.image.load('box.png')
item = pygame.transform.scale(item,(150,150))
item_rect = item.get_rect(bottomright = (400, 300))

item3 = 0
x = 0
#pygame.display.set_mode()
while True:

        
        
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_UP:
                item_rect.top += -1
            if event.key == pygame.K_DOWN:
                item_rect.top += 1
            if event.key == pygame.K_RIGHT:
                item_rect.right += 1
            if event.key == pygame.K_LEFT:
                item_rect.right += -1 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        # Check for all your other relevant keys...

  #      elif event.key == pygame.K_w: # Or any key you need elsewhere
   #         pygame.event.post(event) # Put it back on the queue
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame:
            print('')
    screen.fill('black')
    pygame.FULLSCREEN
    x_pos = random.randint(1,800), 0
    keys = pygame.key.get_pressed()
  #  if keys[pygame.K_LEFT]:
 #       item_rect.right += -1
 #   if keys[pygame.K_RIGHT]:
  #      item_rect.right += 1               
  #  if keys[pygame.K_ESCAPE]:
   #     pygame.quit()
   #     exit()
  

    screen.blit(item, (item_rect) )
 #   screen.blit(item2, (200, 100 ))
    pygame.display.update()
    clock.tick(60)
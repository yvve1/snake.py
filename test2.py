import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400),pygame.RESIZABLE, pygame.FULLSCREEN)
clock = pygame.time.Clock()

sprite = pygame.image.load('sprite.jpg').convert_alpha()
sprite_rect = sprite.get_rect(bottomright = (400, 300))
dot = pygame.image.load('red_dot.png').convert_alpha()
dot_rect = dot.get_rect(bottomright = (1,1))
sprite = pygame.image.load('sprite.jpg').convert_alpha()
sprite_rect = sprite.get_rect(bottomright = (400, 300))
font_1 = pygame.font.Font('pixeltype.ttf', 100)

player = pygame.image.load('player_stand.png').convert_alpha()
player_rect = player.get_rect(bottomright = (100, 300))
ground = pygame.image.load('ground.png').convert_alpha()
sky = pygame.image.load('Sky.png').convert_alpha()
text = font_1.render('hello world', True, 'Black')
text.convert()

mouse = 0, 0
countdown = 0
mousebotton = 0
right = 0
left = 0
while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousebotton += 1 
        if event.type == pygame.MOUSEBUTTONUP:
            mousebotton =0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
             #   sprite_rect.right += -10
                left = 1
                right = 0
                print('left')
            if event.key == pygame.K_d:
               # sprite_rect.right += 10
                right = 1
                left = 0
                print('right')
            if event.type == pygame.KEYUP:
                print('up')
        if event.type == pygame.KEYUP:
            left = 0
            right = 0
            print('up')
    if left == 1:
        sprite_rect.left += -10
    if right == 1:
        sprite_rect.left += 10
    if event.type == pygame.KEYUP:
        left = 0
        right = 0

    #wprint(pygame.key.get_pressed())
    if mousebotton == 1:
        sprite_rect = mouse
        countdown = 60
        mouse2 = mouse
    if countdown >= 1:
        sprite_rect = mouse2
        countdown -= 1

     #   mousebotton += 1
        print(mouse)
    
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    screen.blit(text,( 400, 50))
    screen.blit(sprite,sprite_rect)
    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    clock.tick(60)
    
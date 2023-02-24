import pygame
from sys import exit
from math import trunc
from random import randint

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('cool')
clock = pygame.time.Clock()
font_1 = pygame.font.Font('pixeltype.ttf', 100)
game = True
start_time = 0
bakround_color =(94,129,162)

def display_score():
    
    time = str(trunc((pygame.time.get_ticks()- start_time ) / 1000))
    score_surf = font_1.render(time, True,(64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

def snail_movement(snail_list):
    if snail_list:
        for snail_rect in snail_list:
            snail_rect.x -= 5
            
            if snail_rect.bottom == 210:
                screen.blit(fly1, snail_rect)
            else: screen.blit(snail,snail_rect)
            
        snail_list = [snail for snail in snail_list if snail.x > -100 ]
        
        return snail_list
    else: return []
dot = pygame.image.load('red_dot.png').convert_alpha()
dot_rect = dot.get_rect(bottomright = (1,1))
sprite = pygame.image.load('player_stand.png').convert_alpha()
sprite_rect = sprite.get_rect(bottomright = (400, 300))
player = pygame.image.load('player_stand.png').convert_alpha()
player = pygame.transform.scale2x(player)
player_rect = player.get_rect(center = (400, 200))
ground = pygame.image.load('ground.png').convert_alpha()
sky = pygame.image.load('Sky.png').convert_alpha()
score = 0
text = font_1.render(str(score), True, 'Black').convert_alpha()
box = pygame.image.load('box.png')
box_rect = box.get_rect(center = (500, 200))
player_walk1 = pygame.image.load('jump.png').convert_alpha()
player_walk1_rect = player_walk1.get_rect(center = (400,200))
snail = pygame.image.load('snail.png').convert_alpha()
fly1 = pygame.image.load('fly1.png').convert_alpha()

my_game = font_1.render('my game', True, (111,196,169))
my_game_rect = my_game.get_rect(center = ( 400,75))

spacebar = font_1.render('press spacebar to play', True,(111,196,169))
spacebar_rect = spacebar.get_rect(center = (400, 350))

snail_rect_list = []

text_rect = text.get_rect(midbottom = (400, 200))
x = 1
y = 0
mousebotton = 0
vel = 10
sprite_gravity = 0
jump = 0

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1500)

while True:


    if game == True:
        text = font_1.render(str(score), True, 'Black').convert_alpha()
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        game = True
        
        #sprite
        sprite_rect.right += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
        sprite_rect.top += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        sprite_gravity += 1
        if jump == 0: 
            if keys[pygame.K_SPACE]:
                sprite_gravity = -20
                jump = 1
        sprite_rect.y += sprite_gravity
        if keys[pygame.K_ESCAPE]:
            #pygame.quit()
            #exit()
            game = False
        if sprite_rect.bottom >= 300:
            sprite_rect.bottom = 300
            jump = 0
    # if sprite_rect.bottom > 300:
        #    sprite_rect.bottom = 300
            
        
        screen.blit(player,player_rect)
        screen.blit(sprite,sprite_rect)
        screen.blit(dot, dot_rect)
        
        pygame.draw.line(screen,'black',(0,0), (800,400), )
        display_score()

        snail_rect_list = snail_movement(snail_rect_list)

    

        
 
            
    

        mouse = pygame.mouse.get_pos()

        if player_rect.collidepoint(mouse):
            score += 1




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == timer:
                if randint(0,2):
                    snail_rect_list.append(snail.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    snail_rect_list.append(fly1.get_rect(bottomright = (randint(900,1100),210)))

    else:
        screen.fill(bakround_color)
       # screen.blit(box, box_rect)
       # mouse = pygame.mouse.get_pos()
      #  if box_rect.collidepoint():
       #     pygame.quit() 
        #    exit()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game = True
            sprite_gravity = 0
            jump = 0
            sprite_rect.bottom = 300
            start_time = pygame.time.get_ticks()
            
        if keys[pygame.K_w]:
            pygame.quit()
            exit()
        screen.blit(spacebar,spacebar_rect) 
        screen.blit(player, player_rect)
        screen.blit(my_game,my_game_rect)

        
    pygame.display.update()
    clock.tick(60)
import pygame

pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

rect = pygame.image.load('sprite.jpg').convert_alpha()
rect_rect = rect.get_rect(bottomright = (400, 300))
vel = 10

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    
    rect_rect.right += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect_rect.top += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
        
        
  # rect.centerx = rect.centerx % window.get_width()
   # rect.centery = rect.centery % window.get_height()

    window.fill(0)
    window.blit(rect, rect_rect)
    pygame.display.flip()

pygame.quit()
exit()
import pygame
import os
pygame.init()
largura,altura = 800,680
screen = pygame.display.set_mode((largura,altura))
espaco_img = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
   
    screen.fill((0,0,0))
    screen.blit(espaco_img,(0,0))
    pygame.display.update()

pygame.quit()
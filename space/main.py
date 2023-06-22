import pygame, sys,os
from random import randint,uniform
from classes import Nave
#Configuração basica
width,height = 1200,720
display_surface = pygame.display.set_mode((width,height))   
pygame.display.set_caption("Tiros em Aerolitos")
FPS = pygame.time.Clock() 
#Criando a Sprite Group
group_sprite = pygame.sprite.Group()
#Criando a Nave
nave = Nave(group_sprite)

dt = FPS.tick(60) / 1000.0
bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()

# meteor
# meteoro_timer = pygame.event.custom_type()
# pygame.time.set_timer(meteoro_timer,400) 
# Carrehando a fonte
# Carrehando a fonte
# font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
while True:
    #Tratando Evento de loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == meteoro_timer:
            # meteoro_y_pos = randint(-150,-50)
            # meteoro_x_pos = randint(-100,width+100)
            # pos = (meteoro_x_pos,meteoro_y_pos)
            # Meteoro(pos,dt,groups=meteoro_group)
    #Calculo do delta time
    dt = FPS.tick(60) / 1000.0
    #incluido imagem de Fundo
    display_surface.blit(bg1,(0,0))
    
    group_sprite.update()
    group_sprite.draw(display_surface)
    # laser_group.update(meteoro_group)
    # laser_group.draw(display_surface)
    # group_sprite.draw(display_surface)
    # meteoro_group.update()
    # meteoro_group.draw(display_surface)

    # score.display(display_surface)

    pygame.display.update()
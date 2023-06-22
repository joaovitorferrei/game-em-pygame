import pygame,os,sys

class Nave(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(self,group)
        self.__image = pygame.image.load(os.path.join("assests","img","ship.png")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image,(45,40))
        self.image = self.__image
        self.__rect = self.image.get_rect(center=(1200/2, 650/2))
        self.rect = self.__rect
        #criação do timer para o disporo
        self.__pode_disparar = True
        self.__time_tito = None
        # mascara
        self.mascara = pygame.mask.from_surface(self.image)
        #saund
        # self.som_lase = pygame.mixer.Sound(os.path.join("assets","saund","lazer.ogg"))
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def update(self):
        self.input_position()

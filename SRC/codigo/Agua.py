import pygame
from Objetos import Objetos 


class Agua(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Objetos.AGUA
        self.velocidad = 0


    def getImage(self):
        return self.image
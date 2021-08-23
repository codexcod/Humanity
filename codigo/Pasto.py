import pygame
from Objetos import Objetos 


class Pasto(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Objetos.PASTO
        self.velocidad = 1


    def getImage(self):
        return self.image

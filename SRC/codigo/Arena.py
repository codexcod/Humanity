import pygame
from Objetos import Objetos 


class Arena(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Objetos.ARENA
        self.velocidad = 0.5


    def getImage(self):
        return self.image
import pygame 
from Objetos import Objetos


class Piedra(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Objetos.PIEDRA
        self.piedras = 0
        self.talado = False


    def getImage(self):
        return self.image


    def setPiedras(self,piedras):
        self.piedras = piedras
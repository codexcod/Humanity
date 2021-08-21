import pygame
from Objetos import Objetos


class Arbol(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Objetos.ARBOL
        self.troncos = 0
        self.talado = False


    def getImage(self):
        return self.image


    def setTroncos(self,troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            self.image = Objetos.ARBOL_GRANDE

        else:
            self.image = Objetos.ARBOL

    def getTroncos(self):
        return self.troncos
        
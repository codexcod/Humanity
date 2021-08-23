import pygame

from codigo.Isla.Helper import Helper


class Agua(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Helper.AGUA
        self.velocidad = 0


    def getImage(self):
        return self.image
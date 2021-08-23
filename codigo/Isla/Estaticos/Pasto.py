import pygame

from codigo.Isla.Helper import Helper


class Pasto(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Helper.PASTO
        self.velocidad = 1


    def getImage(self):
        return self.image

import pygame

from codigo.Isla.Helper import Helper


class Arena(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Helper.ARENA
        self.velocidad = 0.5


    def getImage(self):
        return self.image
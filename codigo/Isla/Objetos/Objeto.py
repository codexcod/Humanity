import pygame


class Objeto(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.nombre = ""

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image

    def onClick(self):
        return False

    def getInfoStr(self):
        return ""
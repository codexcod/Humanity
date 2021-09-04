from codigo.Isla.Helper import Helper
import pygame

class Tronco(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Helper.TRONCO
        self.nombre = "Tronco"
    
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image
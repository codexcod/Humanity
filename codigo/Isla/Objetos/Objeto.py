import pygame


class Objeto(pygame.sprite.Sprite):

    def __init__(self,x,y,isla):
        pygame.sprite.Sprite.__init__(self)
        self.nombre = ""
        self.caminable = False
        self.x = x
        self.y = y
        self.isla = isla

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

    def setCaminable(self,caminable):
        self.caminable = caminable

    def getCaminable(self):
        return self.caminable

    def getX(self):
        return self.x

    def getY(self):
        return self.y
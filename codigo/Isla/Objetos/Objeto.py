from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper
import pygame


class Objeto:

    def __init__(self,x,y,isla):
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

    def getUI(self):
        info = []
        fondo = pygame.surface.Surface((800, 500))
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(25)
        texto = self.getInfoStr()
        lineas = texto.splitlines()
        forI = 0 
        for i in lineas:
            textObject = font.render(i, True, (255, 255, 255), None)
            info.append(UIObject(textObject, 550, 250 + forI * 40))
            forI += 1
        
        image = pygame.transform.scale(self.getImage(), (200, 200))
        info.append(UIObject(image, 200, 200))
        
        return info

    def getTrabajo(self):
        return 0

    def getValor(self):
        return None
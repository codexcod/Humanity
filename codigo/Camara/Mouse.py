import pygame
import math


class Mouse:

    def __init__(self, camara):
        self.camara = camara
        self.camara.setMouse(self)

    def pedirInfoObjeto(self):
        posX = self.camara.getPosX() - math.floor(self.camara.getZoom().getLimiteXFloat())
        posY = self.camara.getPosY() - math.floor(self.camara.getZoom().getLimiteYFloat())

        mousePosition = pygame.mouse.get_pos()
        x = posX + math.floor(mousePosition[0] / self.camara.getZoom().getRangoZoom())
        y = posY + math.floor(mousePosition[1] / self.camara.getZoom().getRangoZoom())
        if not self.camara.getMapaObjetos()[y][x] is None:
            return self.camara.getMapaObjetos()[y][x]

        if not self.camara.getMapaMovible()[y][x] is None:
            return self.camara.getMapaMovible()[y][x]


    def clickearPorPoscicion(self,objetosClickeables):
        mousePosition = pygame.mouse.get_pos()
        x = math.ceil(mousePosition[0])
        y = math.ceil(mousePosition[1])
        for object in objetosClickeables:
            if x + 20 >= object.getPosX() >= x - 40:
                if y + 20 >= object.getPosY() >= y - 40:
                    object.onClick()
                    objetosClickeables.remove(object)

    def getObjectMousePosition(self):
        posX = self.camara.getPosX() - math.floor(self.camara.getZoom().getLimiteXFloat())
        posY = self.camara.getPosY() - math.floor(self.camara.getZoom().getLimiteYFloat())

        mousePosition = pygame.mouse.get_pos()
        x = posX + math.floor(mousePosition[0] / self.camara.getZoom().getRangoZoom())
        y = posY + math.floor(mousePosition[1] / self.camara.getZoom().getRangoZoom())

    
        
        return x,y

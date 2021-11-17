import pygame
import math


class Mouse:

    def __init__(self, camara):
        self.camara = camara
        self.camara.setMouse(self)

    def pedirInfoObjeto(self):
        x = self.getObjectMousePosition()[0]
        y = self.getObjectMousePosition()[1]
        if not self.camara.getMapaObjetos()[y][x] is None:
            return self.camara.getMapaObjetos()[y][x]

        if not self.camara.getMapaMovible()[y][x] is None:
            return self.camara.getMapaMovible()[y][x]

    def seleccionarMovible(self):
        x = self.getObjectMousePosition()[0]
        y = self.getObjectMousePosition()[1]

        return self.camara.getMapaMovible()[y][x]

    def clickearPorPoscicion(self, objetosClickeables):
        # Clickea 
        mousePosition = pygame.mouse.get_pos()
        x = math.ceil(mousePosition[0])
        y = math.ceil(mousePosition[1])
        for object in objetosClickeables:
            if x + 20 >= object.getPosX() >= x - 40:
                if y + 20 >= object.getPosY() >= y - 40:
                    objetosClickeables.clear()
                    object.onClick()

    def getObjectMousePosition(self):
        # Averigua donde esta el mouse en el mapa
        posX = self.camara.getPosX() - math.floor(self.camara.getZoom().getLimiteXFloat())
        posY = self.camara.getPosY() - math.floor(self.camara.getZoom().getLimiteYFloat())

        mousePosition = pygame.mouse.get_pos()
        x = posX + math.floor(mousePosition[0] / self.camara.getZoom().getRangoZoom())
        y = posY + math.floor(mousePosition[1] / self.camara.getZoom().getRangoZoom())

        return x, y

import pygame


class Zoom:

    MIN_ZOOM = 3
    NORMAL_ZOOM = 2
    MED_ZOOM = 1
    MAX_ZOOM = 0

    def __init__(self, zoom,maxX,maxY):
        self.zoom = zoom
        self.rangoZoom = [50, 40, 25, 20]
        self.maxX = maxX
        self.maxY = maxY


    def subirZoom(self):
        self.zoom += 1
        if self.zoom >= 3:
            self.zoom = 3
            return False

        if (1000 // self.rangoZoom[self.zoom]) >= self.maxX or (600 // self.rangoZoom[self.zoom]) >= self.maxY:
            self.zoom -= 1
            return False

        return True

    def bajarZoom(self):
        self.zoom -= 1
        if self.zoom <= 0:
            self.zoom = 0
            return False

        return True

    def getLimiteX(self):
        return (1000 // self.rangoZoom[self.zoom]) // 2

    def getLimiteY(self):
        return (600 // self.rangoZoom[self.zoom]) // 2

    def getLimiteXFloat(self):
        return (1000 // self.rangoZoom[self.zoom]) / 2

    def getLimiteYFloat(self):
        return (600 // self.rangoZoom[self.zoom]) / 2

    def getRangoZoom(self):
        return self.rangoZoom[self.zoom]

    def getMaxX(self):
        return self.maxX

    def getMaxY(self):
        return self.maxY


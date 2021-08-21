from Isla import Isla
import pygame
import math
from Zoom import Zoom


class Camara:

    def __init__(self, posX, posY, isla,zoom):
        self.mapa = isla.getMapaEstatico()
        self.isla = isla
        self.screen = pygame.display.set_mode((1000, 600))
        self.posX = posX
        self.posY = posY
        self.zoom = Zoom(zoom,isla.getAncho(),isla.getAltura())

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY    

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def moveX(self, posX):
        self.posX += posX

    def moveY(self, posY):
        self.posY += posY

    def chquearMaxX(self):
        if self.posX >= self.zoom.getMaxX() - self.zoom.getLimiteX():
            self.posX = self.zoom.getMaxX() - self.zoom.getLimiteX()

        if self.posX <= self.zoom.getLimiteX() + 1:
            self.posX = self.zoom.getLimiteX() + 1

    def chquearMaxY(self):
        if self.posY >= self.zoom.getMaxY() - self.zoom.getLimiteY():
            self.posY = self.zoom.getMaxY() - self.zoom.getLimiteY()

        if self.posY <= self.zoom.getLimiteY() + 1:
            self.posY = self.zoom.getLimiteY() + 1

    def actualizarPantalla(self):
        self.screen.fill((255, 255, 255))
        self.chquearMaxX()
        self.chquearMaxY()
        forY = 0
        for y in range(self.posY - math.floor(self.zoom.getLimiteYFloat()), self.posY + math.ceil(self.zoom.getLimiteYFloat())):
            forX = 0
            for x in range(self.posX - math.floor(self.zoom.getLimiteXFloat()), self.posX + math.ceil(self.zoom.getLimiteXFloat())):
                superficie = pygame.Surface((self.zoom.getRangoZoom(),self.zoom.getRangoZoom()))
                superficie.fill(self.mapa[y][x],None,0)
                self.screen.blit(superficie, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))
                forX += 1

            forY += 1

    def getZoom(self):
        return self.zoom
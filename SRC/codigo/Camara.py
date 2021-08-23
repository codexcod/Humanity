from Isla import Isla
import pygame
import math
from Zoom import Zoom


class Camara:

    def __init__(self, posX, posY, isla, zoom, ui):
        self.ui = ui
        self.mEstatico = isla.getMapaEstatico()
        self.mObjetos = isla.getMapaObjetos()
        self.isla = isla
        self.screen = pygame.display.set_mode((1000, 600))
        self.posX = posX
        self.posY = posY
        self.zoom = Zoom(zoom, isla.getAncho(), isla.getAltura())

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
        if self.posX >= self.zoom.getMaxX() - math.ceil(self.zoom.getLimiteXFloat()):
            self.posX = self.zoom.getMaxX() - math.ceil(self.zoom.getLimiteXFloat())

        if self.posX <= self.zoom.getLimiteX() + 1:
            self.posX = self.zoom.getLimiteX() + 1

    def chquearMaxY(self):
        if self.posY >= self.zoom.getMaxY() - math.ceil(self.zoom.getLimiteYFloat()):
            self.posY = self.zoom.getMaxY() - math.ceil(self.zoom.getLimiteYFloat())

        if self.posY <= self.zoom.getLimiteY() + 1:
            self.posY = self.zoom.getLimiteY() + 1

    def actualizarPantalla(self):
        self.screen.fill((255, 255, 255))
        self.chquearMaxX()
        self.chquearMaxY()
        forY = 0
        for y in range(self.posY - math.floor(self.zoom.getLimiteYFloat()),
                       self.posY + math.ceil(self.zoom.getLimiteYFloat())):
            forX = 0
            for x in range(self.posX - math.floor(self.zoom.getLimiteXFloat()),
                           self.posX + math.ceil(self.zoom.getLimiteXFloat())):
                superficie = pygame.transform.scale(self.mEstatico[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                self.screen.blit(superficie, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))
                if not self.mObjetos[y][x] is None:
                    objeto = pygame.transform.scale(self.mObjetos[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                forX += 1

            forY += 1

    def dibujarUI(self):
        for listaUI in self.ui.getUIList():
            for ui in listaUI:
                self.screen.blit(ui.getObjeto(), (ui.getPosX(), ui.getPosY()))

    def getZoom(self):
        return self.zoom

    def getMapaEstatico(self):
        return self.mEstatico

    def getMapaObjetos(self):
        return self.mObjetos

    def getUI(self):
        return self.ui

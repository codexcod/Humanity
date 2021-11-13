import pygame
import math

from codigo.Camara.Zoom import Zoom
from codigo.Isla.Helper import Helper


class Camara:

    def __init__(self, posX, posY, isla, zoom, ui):
        self.ui = ui
        self.mEstatico = isla.getMapaEstatico()
        self.mObjetos = isla.getMapaObjetos()
        self.mMovibles = isla.getMapaMovible()
        self.isla = isla
        self.screen = pygame.display.set_mode((1000, 600))
        self.posX = posX
        self.posY = posY
        self.zoom = Zoom(zoom, isla.getAncho(), isla.getAltura())
        self.mouse = None
        self.seleccionado = None
        self.controlador = None
        self.objetoMouse = None

    def getSeleccionado(self):
        return self.seleccionado

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
        # Si la camara se va afuera del mapa, en X, que vuelva
        if self.posX >= self.zoom.getMaxX() - math.ceil(self.zoom.getLimiteXFloat()):
            self.posX = self.zoom.getMaxX() - math.ceil(self.zoom.getLimiteXFloat())

        if self.posX <= self.zoom.getLimiteX() + 1:
            self.posX = self.zoom.getLimiteX() + 1

    def chquearMaxY(self):
        # Si la camara se va afuera del mapa, en Y, que vuelva
        if self.posY >= self.zoom.getMaxY() - math.ceil(self.zoom.getLimiteYFloat()):
            self.posY = self.zoom.getMaxY() - math.ceil(self.zoom.getLimiteYFloat())

        if self.posY <= self.zoom.getLimiteY() + 1:
            self.posY = self.zoom.getLimiteY() + 1

    def setMouse(self,mouse):
        self.mouse = mouse

    def getMouse(self):
        return self.mouse

    def setControlador(self,controlador):
        self.controlador = controlador
        self.ui.setControlador(controlador)

    def actualizarPantalla(self):
        # Actualiza la pantalla
        self.screen.fill((255, 255, 255))
        self.chquearMaxX()
        self.chquearMaxY()
        forY = 0
        # Va de Y a Y y de X a X dibujando
        for y in range(self.posY - math.floor(self.zoom.getLimiteYFloat()),
                       self.posY + math.ceil(self.zoom.getLimiteYFloat())):
            forX = 0
            for x in range(self.posX - math.floor(self.zoom.getLimiteXFloat()),
                           self.posX + math.ceil(self.zoom.getLimiteXFloat())):
                superficie = pygame.transform.scale(self.mEstatico[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                self.screen.blit(superficie, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                if self.mouse.getObjectMousePosition()[0] == x  and self.mouse.getObjectMousePosition()[1] == y:
                    recuadro = pygame.transform.scale(Helper.RECUADRO,(self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(recuadro, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))
                
                if not self.objetoMouse is None:
                    if self.mouse.getObjectMousePosition()[0] == x  and self.mouse.getObjectMousePosition()[1] == y:
                        objeto = pygame.transform.scale(self.objetoMouse.getImage(),(self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                        self.objetoMouse.setPosX(x)
                        self.objetoMouse.setPosY(y)
                        self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))    

                if not self.seleccionado is None:
                    if self.seleccionado.getX() == x and self.seleccionado.getY() == y:
                        select = pygame.transform.scale(Helper.SELECCIONADO,(self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                        self.screen.blit(select, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))


                if self.mEstatico[y][x].getVisibilidad():
                    if not self.mObjetos[y][x] is None:
                        objeto = pygame.transform.scale(self.mObjetos[y][x].getImage(),
                                                        (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                        self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                    if not self.mMovibles[y][x] is None:
                        objeto = pygame.transform.scale(self.mMovibles[y][x].getImage(),
                                                        (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                        self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                else:
                    objeto = pygame.transform.scale(Helper.NIEBLA,
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))





                forX += 1

            forY += 1


    def dibujarUI(self):
        for ui in self.ui.getAldeaUI():
            self.screen.blit(ui.getObjeto(), (ui.getPosX(), ui.getPosY()))
        for listaUI in self.ui.getUIList():
            for ui in listaUI:
                self.screen.blit(ui.getObjeto(), (ui.getPosX(), ui.getPosY()))

    def getZoom(self):
        return self.zoom

    def getMapaEstatico(self):
        return self.mEstatico

    def getMapaObjetos(self):
        return self.mObjetos

    def getMapaMovible(self):
        return self.mMovibles

    def getUI(self):
        return self.ui

    def setSeleccionado(self,seleccionado):
        self.seleccionado = seleccionado

    def setIsla(self,isla):
        self.isla = isla
        self.mEstatico = isla.getMapaEstatico()
        self.mObjetos = isla.getMapaObjetos()
        self.mMovibles = isla.getMapaMovible()

    def getIsla(self):
        return self.isla

    def getObjetoMouse(self):
        return self.objetoMouse

    def setObjetoMouse(self,objeto):
        self.objetoMouse = objeto

    def colocarObjeto(self):
        if not self.objetoMouse is None:
            if self.mObjetos[self.objetoMouse.getY()][self.objetoMouse.getX()] is None and self.mMovibles[self.objetoMouse.getY()][self.objetoMouse.getX()] is None:
                self.isla.agregarObjeto(self.objetoMouse.getX(),self.objetoMouse.getY(),self.objetoMouse)
                self.objetoMouse = None

            



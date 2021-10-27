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

    def setMouse(self, mouse):
        self.mouse = mouse

    def getMouse(self):
        return self.mouse

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
                # Aca va actualizando la superficie del mapa
                superficie = pygame.transform.scale(self.mEstatico[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                self.screen.blit(superficie, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                if self.mouse.getObjectMousePosition()[0] == x and self.mouse.getObjectMousePosition()[1] == y:
                    # Aca es cuando dibuja el recuadro del mouse gracias a la comparacion de la posicion del mouse en
                    # X e Y, con la posicion pro la que esta pasando el "programa"
                    recuadro = pygame.transform.scale(Helper.RECUADRO,
                                                      (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(recuadro, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                if not self.seleccionado is None:
                    # Esta parte dibuja encima del seleccionado en el caso de que la X y la Y del seleccionado sean
                    # Iguales a la X e Y del "programa", luego de esto se fija con el rango del zoom para determinar
                    # el tamaño del dibujo q tiene q hacer
                    if self.seleccionado.getX() == x and self.seleccionado.getY() == y:
                        select = pygame.transform.scale(Helper.SELECCIONADO,
                                                        (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                        self.screen.blit(select, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                if not self.mObjetos[y][x] is None:
                    # Aca actualiza el mapa de los objetos en el caso de que haya algo en la X e Y en el momento que
                    # Esta pasando el "programa", luego se fija el zoom para determinar el tamaño del dibujo.
                    objeto = pygame.transform.scale(self.mObjetos[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                if not self.mMovibles[y][x] is None:
                    # Aca actualiza el mapa de los movibles en el caso de que haya algo en la X e Y en el momento que
                    # Esta pasando el "programa", luego se fija el zoom para determinar el tamaño del dibujo.
                    objeto = pygame.transform.scale(self.mMovibles[y][x].getImage(),
                                                    (self.zoom.getRangoZoom(), self.zoom.getRangoZoom()))
                    self.screen.blit(objeto, (forX * self.zoom.getRangoZoom(), forY * self.zoom.getRangoZoom()))

                forX += 1

            forY += 1

    def dibujarUI(self):
        # Aca es cuando dibujan el UI gracias a la hora de saber el objeto que es, y su posicion
        for ui in self.ui.getAldeaUI():
            # Dentro de la aldea se va pasando por cada UI para ir actualizandolo
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

    def setSeleccionado(self, seleccionado):
        self.seleccionado = seleccionado

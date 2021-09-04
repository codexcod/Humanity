from math import inf
import pygame

from codigo.Camara.UI.BotonUI import BotonUI
from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class UI:

    def __init__(self):
        self.ui = []
        self.objetosClickeables = []
        self.aldeaUI = None


    def generarBoton(self):
        uiBoton = []
        boton = BotonUI(850,50)
        uiBoton.append(boton)
        self.objetosClickeables.append(boton)
        self.ui.append(uiBoton)

    def generarInfoObjeto(self, objeto):
        info = []
        fondo = pygame.surface.Surface((800, 500))
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(25)
        texto = objeto.getInfoStr()
        lineas = texto.splitlines()
        forI = 0 
        for i in lineas:
            textObject = font.render(i, True, (255, 255, 255), None)
            info.append(UIObject(textObject, 550, 250 + forI * 40))
            forI += 1
        
        image = pygame.transform.scale(objeto.getImage(), (200, 200))
        info.append(UIObject(image, 200, 200))
        close = pygame.transform.scale(Helper.CLOSE, (50, 50))
        info.append(UIObject(close, 840, 60))
        self.objetosClickeables.append(CloseUI(close, 840, 60, info, self.ui))
        self.ui.append(info)

    def generarAldeaUI(self, aldea):
        ui = []
        madera = pygame.surface.Surface((100, 30))
        madera.fill((128, 64, 0), None, 0)
        ui.append(UIObject(madera,200,25))
        font = Helper.FUENTE(10)
        textoMadera = font.render(f"{aldea.getMadera()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoMadera, 245, 35))

        piedra = pygame.surface.Surface((100, 30))
        piedra.fill((155, 155, 155), None, 0)
        ui.append(UIObject(piedra, 400, 25))
        font = Helper.FUENTE(10)
        textoPiedra = font.render(f"{aldea.getPiedra()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoPiedra, 445, 35))
        self.aldeaUI = ui

    def getUIList(self):
        return self.ui

    def getObjetosClickeables(self):
        return self.objetosClickeables

    def hayUIActivos(self):
        return len(self.ui) >= 1

    def getAldeaUI(self):
        return self.aldeaUI

import pygame


from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class UI:

    def __init__(self):
        self.ui = []
        self.objetosClickeables = []

    def generarInfoObjeto(self, objeto):
        info = []
        fondo = pygame.surface.Surface((800, 500))
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(32)
        text = font.render(objeto.getInfoStr(), True, (255, 255, 255), None)
        info.append(UIObject(text, 600, 250))
        image = pygame.transform.scale(objeto.getImage(), (200, 200))
        info.append(UIObject(image, 200, 200))
        close = pygame.transform.scale(Helper.CLOSE, (50, 50))
        info.append(UIObject(close, 840, 60))
        self.objetosClickeables.append(CloseUI(close, 840, 60, info, self.ui))
        self.ui.append(info)

    def getUIList(self):
        return self.ui

    def getObjetosClickeables(self):
        return self.objetosClickeables

    def hayUIActivos(self):
        return len(self.ui) >= 1

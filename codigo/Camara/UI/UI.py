from math import inf
import pygame


from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class UI:

    def __init__(self):
        self.ui = []
        self.objetosClickeables = []
        self.aldeaUI = None

    def generarInfoObjeto(self, objeto):
        # Genera el UI donde se guardara la informacion de un objeto
        info = (objeto.getUI())
        close = pygame.transform.scale(Helper.CLOSE, (50, 50))
        info.append(UIObject(close, 840, 60))
        self.objetosClickeables.append(CloseUI(close, 840, 60, info, self.ui))
        self.ui.append(info)



    def generarAldeaUI(self, aldea):
        # Genera el UI de la aldea
        ui = []
        madera = pygame.surface.Surface((100, 30))
        madera.fill((128, 64, 0), None, 0)
        ui.append(UIObject(madera,200,25))
        font = Helper.FUENTE(10)
        textoMadera = font.render(f"{aldea.getMadera()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoMadera, 245, 35))
        # Rellena el UI de la madera de la aldea

        piedra = pygame.surface.Surface((100, 30))
        piedra.fill((155, 155, 155), None, 0)
        ui.append(UIObject(piedra, 400, 25))
        font = Helper.FUENTE(10)
        textoPiedra = font.render(f"{aldea.getPiedra()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoPiedra, 445, 35))
        # Rellena el UI de la piedra de la aldea

        carne = pygame.surface.Surface((100, 30))
        carne.fill((249, 144, 111), None, 0)
        ui.append(UIObject(carne, 600, 25))
        font = Helper.FUENTE(10)
        textoCarne = font.render(f"{aldea.getCarne()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoCarne, 645, 35))
        self.aldeaUI = ui
        # Rellena el UI de la carne de la aldea

    def getUIList(self):
        return self.ui

    def getObjetosClickeables(self):
        return self.objetosClickeables

    def hayUIActivos(self):
        return len(self.ui) >= 1

    def getAldeaUI(self):
        return self.aldeaUI

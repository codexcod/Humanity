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
        self.controlador = None

    def generarInfoObjeto(self, objeto):
        # Genera el UI donde se guardara la informacion de un objeto
        info = []
        for objetoui in objeto.getUI(self.objetosClickeables, info, self.ui,self):
            info.append(objetoui)

        close = pygame.transform.scale(Helper.CLOSE, (50, 50))
        info.append(UIObject(close, 840, 60))
        self.objetosClickeables.append(CloseUI(close, 840, 60, info, self.ui))
        self.ui.append(info)

    def setControlador(self,controlador):
        self.controlador = controlador

    def generarAldeaUI(self, aldea):
        # Genera el UI de la aldea
        ui = []
        madera = pygame.surface.Surface((100, 30))
        madera.fill((128, 64, 0), None, 0)
        ui.append(UIObject(madera,200, 25))
        font = Helper.FUENTE(10)
        textoMadera = font.render(f"{aldea.getMadera()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoMadera, 245, 35))
        fondoObjeto = Helper.getImage(Helper.INVENTARIO, 30, 30)
        ui.append(UIObject(fondoObjeto, 16, 25))
        dibujoMadera = Helper.getImage(Helper.TRONCO, 20, 20)
        ui.append(UIObject(dibujoMadera, 170, 30))
        # Rellena el UI de la madera de la aldea

        piedra = pygame.surface.Surface((100, 30))
        piedra.fill((155, 155, 155), None, 0)
        ui.append(UIObject(piedra, 400, 25))
        font = Helper.FUENTE(10)
        textoPiedra = font.render(f"{aldea.getPiedra()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoPiedra, 445, 35))
        fondoObjeto = Helper.getImage(Helper.INVENTARIO, 30, 30)
        ui.append(UIObject(fondoObjeto, 365, 25))
        dibujoPiedra = Helper.getImage(Helper.ROCA_OBJETO, 20, 20)
        ui.append(UIObject(dibujoPiedra, 370, 30))
        # Rellena el UI de la piedra de la aldea

        carne = pygame.surface.Surface((100, 30))
        carne.fill((249, 144, 111), None, 0)
        ui.append(UIObject(carne, 600, 25))
        font = Helper.FUENTE(10)
        textoCarne = font.render(f"{aldea.getCarne()}", True, (255, 255, 255), None)
        ui.append(UIObject(textoCarne, 645, 35))
        fondoObjeto = Helper.getImage(Helper.INVENTARIO, 30, 30)
        ui.append(UIObject(fondoObjeto, 565, 25))
        dibujoCarne = Helper.getImage(Helper.CARNE, 20, 20)
        ui.append(UIObject(dibujoCarne, 570, 30))
         # Rellena el UI de la carne de la aldea}


        fondoPersonas = Helper.getImage(Helper.FONDO_BORDO,150, 52)
        ui.append(UIObject(fondoPersonas, 835, 13))

        cabeza = Helper.getImage(Helper.CABEZA_PERSONA,100,100)
        ui.append(UIObject(cabeza,820,-10))

        cantidadPersonas = len(aldea.getPersonas())
        cantidadMaxPersonas = len(aldea.getCasas()) * 3

        fuente = Helper.FUENTE(30)
        personas = fuente.render(f"{cantidadPersonas} / {cantidadMaxPersonas}", True, (255, 255, 255), None)
        ui.append(UIObject(personas,900,19))
         # Rellena el UI de la carne de la aldea

        fondoInteligencia = pygame.surface.Surface((800, 10))
        fondoInteligencia.fill((253,188,180),None,0)
        ui.append(UIObject(fondoInteligencia, 100, 550))

        rellenoInteligencia = pygame.surface.Surface((790, 4))
        rellenoInteligencia.fill((168,122,109),None,0)
        ui.append(UIObject(rellenoInteligencia, 105, 553))

        inteligencia = pygame.surface.Surface((aldea.getInteligencia() * 0.79, 4))
        inteligencia.fill((0,187,45),None,0)
        ui.append(UIObject(inteligencia, 105, 553))

        
        ui.append(UIObject(Helper.getImage(Helper.CEREBRO_DIMINUTO,70,70), 65, 515))

        ui.append(UIObject(Helper.getImage(Helper.CEREBRO_CHICO,70,70), 331.66, 520))

        ui.append(UIObject(Helper.getImage(Helper.CEREBRO_MEDIANO,70,70), 598.33, 520))

        ui.append(UIObject(Helper.getImage(Helper.CEREBRO,70,70), 865, 520))

        self.aldeaUI = ui
       



    def getUIList(self):
        return self.ui

    def getObjetosClickeables(self):
        return self.objetosClickeables

    def hayUIActivos(self):
        return len(self.ui) >= 1

    def getAldeaUI(self):
        return self.aldeaUI

    def getControlador(self):
        return self.controlador
import json
import os

from codigo.Camara.UI.ExploradorObjeto import ExploradorObjeto
from codigo.Isla import Isla

from codigo.Camara.UI.IslaObjeto import IslaObjeto
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Tronco import Tronco
import random


class Barco(Objeto):
    
    def __init__(self,x,y,isla):
        Objeto.__init__(self,x,y,isla)
        self.image = Helper.BARCO
        self.nombre = "Barco de travesias"
        self.roto = True
        self.explorador =  None

    def toJson(self):
        return {
            'objeto' : 'Barco',
            'name' : self.nombre,
            'x' : self.x,
            'y' : self.y
        }


    def arreglarBarco(self):
        self.roto = False

    def getInfoStr(self):
        return "Barco de traversias"

    def onClick(self,herramienta):
        return

    def getUI(self,clickeables,lista,listaUI,ui):
        info = []

        fondo = Helper.getSurface(800, 500)
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))

        font = Helper.FUENTE(30)
        textPrecio = font.render("Barco", True, (255, 255, 255), None)
        info.append(UIObject(textPrecio, 450,75))


        listaIslas = [[ui.getControlador().getIsla().getNombre(),0],["Isla Misteriosa",50],["Isla Desconocida",50]]

        forIsla = 0
        for isla in listaIslas:
            if forIsla < 2:
                botonActivaddo = isla[0] != self.isla.getNombre()
                islaObjeto = IslaObjeto(isla[0], isla[1],self.explorador,botonActivaddo)

                uiIsla = islaObjeto.getUI(150 + 235 * forIsla, 150,lista,ui,clickeables)
                for uiObject in uiIsla:
                    info.append(uiObject)

                forIsla += 1


        personas = []
        for persona in ui.getControlador().getIsla().getAldea().getPersonas():

            personas.append(persona)

        forExplorador = 0
        for explorador in personas:
            exploradorObjeto = ExploradorObjeto(explorador)

            uiExplorador = exploradorObjeto.getUI(600, 160 + 160 * forExplorador, lista, listaUI, ui, clickeables, self)
            for uiObject in uiExplorador:
                info.append(uiObject)

            forExplorador += 1

        return info

    def getExplorador(self):
        return self.explorador

    def setExplorador(self,explorador):
        self.explorador = explorador


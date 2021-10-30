from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class BotonIslaUI(UIObject):

    def __init__(self, objeto, posX, posY, lista,ui,isla,explorador):
        super().__init__(objeto, posX, posY)
        self.lista = lista
        self.ui = ui
        self.isla = isla
        self.explorador = explorador


    def onClick(self):
        self.ui.getControlador().cargarIsla(self.isla,self.explorador)
        self.ui.getUIList().remove(self.lista)

    def getUI(self,clickeables):
        ui = []
        boton = Helper.getSurface(150,50)
        boton.fill((0,190,57),None,0)
        ui.append(UIObject(boton,self.posX,self.posY))
        font = Helper.FUENTE(24)
        texto = font.render("Visitar", True, (255, 255, 255), None)
        visitar = UIObject(texto,self.posX + 30 ,self.posY + 10)
        ui.append(visitar)
        clickeables.append(self)
        return ui
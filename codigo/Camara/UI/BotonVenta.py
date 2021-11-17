from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class BotonVenta(UIObject):

    def __init__(self, objeto, posX, posY, lista, ui, venta, objetoActualizar):
        super().__init__(objeto, posX, posY)
        self.lista = lista
        self.ui = ui
        self.venta = venta
        self.aldea = ui.getControlador().getIsla().getAldea()
        self.objetoActualizar = objetoActualizar

    def onClick(self):
        if self.aldea.chequearVenta(self.venta):
            self.aldea.realizarVenta(self.venta, self.ui.getControlador().getCamara())
            self.ui.getUIList().remove(self.lista)

        else:
            self.ui.generarInfoObjeto(self.objetoActualizar)
            self.ui.getUIList().remove(self.lista)

    def getUI(self, clickeables):
        ui = []

        boton = Helper.getSurface(150, 50)

        if self.venta.getNivelNecesario() <= self.aldea.getInteligencia() and self.aldea.chequearVenta(self.venta):
            boton.fill((0, 190, 57), None, 0)

        else:
            boton.fill((243, 54, 54), None, 0)

        ui.append(UIObject(boton, self.posX, self.posY))

        font = Helper.FUENTE(24)
        texto = font.render("Comprar", True, (255, 255, 255), None)
        visitar = UIObject(texto, self.posX + 17, self.posY + 8)

        ui.append(visitar)
        clickeables.append(self)
        return ui

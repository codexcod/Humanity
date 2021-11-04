from codigo.Camara.UI.UIObject import UIObject


class BotonExplorador(UIObject):

    def __init__(self, objeto, posX, posY, lista, explorador, ui, objetoActualizar):
        super().__init__(objeto, posX, posY)
        self.lista = lista
        self.ui = ui
        self.explorador = explorador
        self.objetoActualizar = objetoActualizar

    def onClick(self):
        self.objetoActualizar.setExplorador(self.explorador)
        self.ui.generarInfoObjeto(self.objetoActualizar)
        self.ui.getUIList().remove(self.lista)


from codigo.Camara.UI.UIObject import UIObject


class FlechaUI(UIObject):

    def __init__(self, objeto, posX, posY, lista,ui,objetoActualizar,suma):
        super().__init__(objeto, posX, posY)
        self.lista = lista
        self.ui = ui
        self.objetoActualizar = objetoActualizar
        self.suma = suma

    def onClick(self):
        self.objetoActualizar.sumarListaObjetos(self.suma)
        self.ui.generarInfoObjeto(self.objetoActualizar)
        self.ui.getUIList().remove(self.lista)
        
from codigo.Camara.UI.UIObject import UIObject


class ActividadUI(UIObject):

    def __init__(self, objeto, posX, posY, lista, persona, ui, objetoActualizar):
        super().__init__(objeto, posX, posY)
        self.lista = lista
        self.ui = ui
        self.persona = persona
        self.objetoActualizar = objetoActualizar

    def onClick(self):
        self.persona.sumarBusqueda()
        self.ui.generarInfoObjeto(self.objetoActualizar)
        self.ui.getUIList().remove(self.lista)

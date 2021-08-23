from codigo.Camara.UI.UIObject import UIObject


class CloseUI(UIObject):

    def __init__(self, objeto, posX, posY, ui, listUI):
        super().__init__(objeto, posX, posY)
        self.ui = ui
        self.listUI = listUI

    def onClick(self):
        self.listUI.remove(self.ui)

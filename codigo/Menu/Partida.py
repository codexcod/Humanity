from Menu.buttom import Boton

class Partida(Boton):

    def __init__(self, pos, font, text, screen, color, colorRec, colorfondo,partida):
        Boton.__init__(self, pos, font, text, screen, color, colorRec, colorfondo)
        self.partida = partida

    def getPartida(self):
        return self.partida

    def setPartida(self,partida):
        self.partida = partida
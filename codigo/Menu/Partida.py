from codigo.Menu.Button import Button


class Partida(Button):

    def __init__(self, pos, font, text, screen, color, colorRec, colorfondo, partida):
        Button.__init__(self, pos, font, text, screen, color, colorRec, colorfondo)
        self.partida = partida
        self.borrar = None

    def getPartida(self):
        return self.partida

    def setPartida(self, partida):
        self.partida = partida

    def setBorrar(self, borrar):
        self.borrar = borrar

    def getBorrar(self):
        return self.borrar

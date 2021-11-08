from codigo.Isla.Objetos import Objeto


class Nodo:

    def __init__(self, y, x, padreMia=None):
        self.padreMia = padreMia
        self.x = x
        self.y = y
        self.caminable = True
        self.costo = 0
        self.valorProbable = 0
        self.total = self.valorProbable + self.costo

    def getPadreMia(self):
        return self.padreMia

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setCosto(self, costo):
        self.costo = costo

    def setValorProbable(self, valorProbable):
        self.valorProbable = valorProbable

    def setPadreMia(self, padre):
        self.padreMia = padre

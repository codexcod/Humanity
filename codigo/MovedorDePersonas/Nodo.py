from codigo.Isla.Objetos import Objeto

class nodo:

    def __init__(self, y, x, padreMia = None):

        self.padreMia = padreMia
        self.x = x
        self.y = y
        self.caminable = True
        self.costo = 0
        self.valorProbable = 0
        self.total = 0

    def getPadreMia(self):
        return self.padreMia
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
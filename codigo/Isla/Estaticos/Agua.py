from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Agua(Estatico):

    def __init__(self):
        Estatico.__init__(self)
        self.image = Helper.AGUA
        self.velocidad = 0


    def getImage(self):
        return self.image
from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Pasto(Estatico):

    def __init__(self):
        Estatico.__init__(self)
        self.image = Helper.PASTO
        self.velocidad = 1


    def getImage(self):
        return self.image

from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Arena(Estatico):

    def __init__(self):
        Estatico.__init__(self)
        self.image = Helper.ARENA
        self.velocidad = 0.5


    def getImage(self):
        return self.image
from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Pasto(Estatico):

    def __init__(self,x,y):
        Estatico.__init__(self,x,y)
        self.image = Helper.PASTO
        self.velocidad = 1


    def getImage(self):
        return self.image


    def toJson(self):
        return {
            'objeto' : 'Pasto',
            'x' : self.x,
            'y' : self.y,
            'visibilidad' : self.visible
        }
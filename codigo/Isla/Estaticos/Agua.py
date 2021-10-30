from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Agua(Estatico):

    def __init__(self,x,y):
        Estatico.__init__(self,x,y)
        self.image = Helper.AGUA
        self.velocidad = 0


    def getImage(self):
        return self.image

    def toJson(self):
        return {
            'objeto' : 'Agua',
            'x' : self.x,
            'y' : self.y,
            'visibilidad' : self.visible
        }
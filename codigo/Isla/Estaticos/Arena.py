from codigo.Isla.Estaticos.Estatico import Estatico
from codigo.Isla.Helper import Helper


class Arena(Estatico):

    def __init__(self,x,y):
        Estatico.__init__(self,x,y)
        self.image = Helper.ARENA
        self.velocidad = 0.5


    def getImage(self):
        return self.image

    def toJson(self):
        return {
            'objeto' : 'Arena',
            'x' : self.x,
            'y' : self.y,
            'visibilidad' : self.visible
        }
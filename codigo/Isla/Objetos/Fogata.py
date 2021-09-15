from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto


class Fogata(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.name = "Fogata de la " + aldea.getNombre()
        self.aldea = aldea
        self.image = Helper.FOGATA

    def toJson(self):
        return {
            'objeto' : 'Fogata',
            'name' : self.nombre,
            'aldea' : self.aldea.getNombre(),
            'x' : self.x,
            'y' : self.y
        }




    def getInfoStr(self):
        result = f"""{self.name}"""
        return result


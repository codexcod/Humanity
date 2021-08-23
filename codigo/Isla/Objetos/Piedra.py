from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto


class Piedra(Objeto):

    def __init__(self):
        Objeto.__init__(self)
        self.setNombre("Piedra")
        self.image = Helper.PIEDRA
        self.piedras = 0


    def setPiedras(self,piedras):
        self.piedras = piedras

    def getPiedras(self):
        return self.piedras

    def getInfoStr(self):
        result = f"""{self.nombre}
Piedras : {self.piedras}
"""
        return result






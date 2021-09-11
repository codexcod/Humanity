from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Baya import Baya


class Arbusto(Objeto):

    def __init__(self, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.setNombre("Arbusto")
        self.image = Helper.ARBUSTO
        self.bayas = 0
        self.talado = False
        self.tiempoCrecimiento = 0

 
    def setBayas(self, bayas):
        self.bayas = bayas

    def getBayas(self):
        return self.bayas

    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Bayas : {self.bayas}
"""
        return result

    def getTrabajo(self):
        return self.bayas * 5

    def getValor(self):
        valor = []
        for i in range(self.bayas):
            valor.append(Baya())

        return valor

    def sacarBayas(self):
        self.isla.getMapaObjetos()[self.y][self.x] = None


    def onClick(self):
        self.sacarBayas()
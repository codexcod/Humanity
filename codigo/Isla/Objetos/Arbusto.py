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

    def toJson(self):
        return {
            'objeto' : 'Arbusto',
            'name' : self.nombre,
            'bayas' : self.bayas,
            'talado' : self.talado,
            'tiempoCrecimiento' : self.tiempoCrecimiento,
            'x' : self.x,
            'y' : self.y
        }

    def setTiempoCrecimiento(self, tiempoCrecimiento):
        self.tiempoCrecimiento = tiempoCrecimiento

    def setTroncos(self, troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            self.setImage(Helper.ARBOL_GRANDE)

        else:
            self.setImage(Helper.ARBOL)

    def setTalado(self, talado):
        self.talado = talado

    def getTalado(self):
        return self.talado
 
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
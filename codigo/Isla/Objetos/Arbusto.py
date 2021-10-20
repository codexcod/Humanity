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
        self.caminable = True

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

    def setTalado(self, talado):
        self.talado = talado

    def getTalado(self):
        return self.talado
 
    def setBayas(self, bayas):
        if bayas < 5:
            self.bayas = 0

        else:
            self.bayas = bayas
            self.setImage(Helper.ARBUSTO_FRUTAL)
            self.setNombre("Arbbusto con bayas")


    def getBayas(self):
        return self.bayas

    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Bayas : {self.bayas}
"""
        return result

    def getTrabajo(self,herramienta):
        if herramienta.getDañoPlanta() > 0:
            return (self.bayas * 10) // herramienta.getDañoPlanta()

        return self.bayas * 10

    def getValor(self):
        valor = []
        for i in range(self.bayas):
            valor.append(Baya())

        return valor

    def sacarBayas(self):
        self.isla.getMapaObjetos()[self.y][self.x] = None


    def onClick(self,herramienta):
        self.sacarBayas()

    def isArbusto(self):
        return True
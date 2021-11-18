from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Roca import Roca


class Muro(Objeto):

    def __init__(self, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.setNombre("Muro")
        self.image = Helper.MURO
        self.vida = 50


    def toJson(self):
        return {
            'objeto': 'Muro',
            'name': self.nombre,
            'x': self.x,
            'y': self.y
        }

    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Vida : {self.vida}
"""
        return result

    def getTrabajo(self, herramienta):
        if herramienta.getDañoPiedra() > 0:
            return (self.vida * 10) // herramienta.getDañoPiedra()

    def destruirMuro(self):
        self.isla.getMapaObjetos()[self.y][self.x] = None

    def onClick(self, herramienta):
        self.getTrabajo(herramienta)
        self.destruirMuro()



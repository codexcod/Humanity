from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Roca import Roca


class Piedra(Objeto):

    def __init__(self,x,y,isla):
        Objeto.__init__(self,x,y,isla)
        self.setNombre("Piedra")
        self.image = Helper.PIEDRA
        self.piedras = 0
        self.oro = 0


    def toJson(self):
        return {
            'objeto' : 'Piedra',
            'name' : self.nombre,
            'piedras' : self.piedras,
            'oro' : self.oro,
            'x' : self.x,
            'y' : self.y
        }

    def setPiedras(self,piedras):
        self.piedras = piedras

    def getPiedras(self):
        return self.piedras

    
    def setOro(self,oro):
        self.oro = oro
        if self.oro > 0:
            self.setImage(Helper.PIEDRA_ORO)
            self.setNombre("Piedra de oro")

    def getOro(self):
        return self.oro

    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Piedras : {self.piedras}
"""
        return result

    def getTrabajo(self):
        return self.piedras * 5

    def getValor(self):
        valor = []
        for i in range(self.piedras):
            valor.append(Roca())

        return valor

    def picarPiedra(self):
        self.isla.getMapaObjetos()[self.y][self.x] = None


    def onClick(self):
        self.picarPiedra()




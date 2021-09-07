from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Roca import Roca


class Piedra(Objeto):

    def __init__(self,x,y,isla):
        Objeto.__init__(self,x,y,isla)
        self.setNombre("Piedra")
        self.image = Helper.PIEDRA
        self.piedras = 0
        self.Oro = 0

 
    def setPiedras(self,piedras):
        self.piedras = piedras

    def getPiedras(self):
        return self.piedras

    
    def setOro(self,oro):
        self.oro = oro
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




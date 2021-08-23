from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto


class Arbol(Objeto):

    def __init__(self):
        Objeto.__init__(self)
        self.setNombre("Arbol")
        self.setImage(Helper.ARBOL)
        self.troncos = 0
        self.talado = False

    def setTroncos(self,troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            self.setImage(Helper.ARBOL_GRANDE)

        else:
            self.setImage(Helper.ARBOL)

    def getTroncos(self):
        return self.troncos

    def onClick(self):
        if not self.talado:
            self.talarArbol()
        return super().onClick()

    def talarArbol(self):
        self.talado = True
        self.setImage(Helper.ARBOL_TALADO)
        self.setNombre("Arbol talado")

    def getInfoStr(self):
        result = f"""{self.nombre}
    Troncos : {self.troncos}
    Talado : {self.talado}
    """
        return result


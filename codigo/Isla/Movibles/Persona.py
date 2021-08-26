from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper

class Persona(Movible):

    def __init__(self,nombre,casa):
        Movible.__init__(self)
        self.edad = 0
        self.casa = casa
        self.nombre = nombre
        self.image = Helper.PERSONA

    def getCasa(self):
        return self.casa

    def getAldea(self):
        return self.casa.getAldea()

    def getInfoStr(self):
        result = self.nombre
 
        return result

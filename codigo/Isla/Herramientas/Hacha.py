from codigo.Isla.Herramientas.Herramienta import Herramienta
from codigo.Isla.Helper import Helper

class Hacha(Herramienta):


    def __init__(self):
        Herramienta.__init__(self)
        self.nombre = "Hacha"
        self.image = Helper.HACHA
        self.dañoPiedra = 1
        self.dañoArbol = 5
        self.dañoPersona = 4
        self.dañoAnimal = 4
        

    def restarUso(self):
        self.usos -= 1
        if self.usos == 0:
            self.rota = True
            self.image = Helper.HACHA

    def toJson(self):
        return {
            'objeto': 'Hacha',
            'usos' : self.usos,
            'rota' : self.rota
        }


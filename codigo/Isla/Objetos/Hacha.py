from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Herramienta import Herramienta

class Hacha(Herramienta):

    def __init__(self):
        self.image = Helper.HACHA
        self.nombre = "Hacha"
        self.daño = 5

    def toJson(self):
        return {
            'objeto' : 'Hacha',
            'name' : self.nombre,
        }

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image
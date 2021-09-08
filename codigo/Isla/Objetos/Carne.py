
from codigo.Isla.Helper import Helper

class Carne:

    def __init__(self):
        self.image = Helper.CARNE
        self.nombre = "Carne"
    
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image
from codigo.Isla.Helper import Helper

class Baya:

    def __init__(self):
        self.image = Helper.BAYA_OBJETO
        self.nombre = "Baya"
    
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image
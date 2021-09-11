from codigo.Isla.Helper import Helper


class Tronco():

    def __init__(self):
        self.image = Helper.TRONCO
        self.nombre = "Tronco"

    def toJson(self):
        return {
            'objeto' : 'Tronco',
            'name' : self.nombre,
        }
    
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image
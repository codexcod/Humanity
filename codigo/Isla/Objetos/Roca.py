from codigo.Isla.Helper import Helper

class Roca:

    def __init__(self):
        self.image = Helper.ROCA_OBJETO
        self.nombre = "Roca"

    def toJson(self):
        return {
            'objeto' : 'Roca',
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
class Herramienta:

    def __init__(self):
        self.nombre = ""
        self.usos = 0
        self.dañoArbol = 0
        self.dañoPiedra = 0
        self.dañoAnimal = 0
        self.dañoPlanta = 0
        self.dañoPersona = 0
        self.rota = False
        self.image = None

    def getDañoMuros(self):
        return self.dañoMuros

    def getDañoArbol(self):
        return self.dañoArbol

    def getDañoPiedra(self):
        return self.dañoPiedra

    def getDañoAnimal(self):
        return self.dañoAnimal

    def getDañoPlanta(self):
        return self.dañoPlanta
    
    def getDañoPersona(self):
        return self.dañoPersona

    def getUsos(self):
        return self.usos

    def getRota(self):
        return self.rota

    def setRota(self,rota):
        self.rota = rota

    def getNombre(self):
        return  self.nombre


    def restarUso(self):
        self.usos -= 1
        if self.usos == 0:
            self.rota = True


    def getImage(self):
        return self.image

    def setImage(self,image):
        self.image = image

    def setUsos(self,usos):
        self.usos = usos



    



from codigo.Isla.Helper import Helper


class Pasto:

    def __init__(self):
        
        self.image = Helper.PASTO
        self.velocidad = 1


    def getImage(self):
        return self.image

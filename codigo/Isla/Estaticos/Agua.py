from codigo.Isla.Helper import Helper


class Agua:

    def __init__(self):
        
        self.image = Helper.AGUA
        self.velocidad = 0


    def getImage(self):
        return self.image
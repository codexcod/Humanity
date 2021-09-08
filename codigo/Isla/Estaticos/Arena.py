from codigo.Isla.Helper import Helper


class Arena:

    def __init__(self):
        
        self.image = Helper.ARENA
        self.velocidad = 0.5


    def getImage(self):
        return self.image
class UIObject:

    def __init__(self, objeto, posX, posY):
        self.objeto = objeto
        self.posX = posX
        self.posY = posY
        

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getObjeto(self):
        return self.objeto
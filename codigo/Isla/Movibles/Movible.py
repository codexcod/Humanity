from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto

class Movible(Objeto):

    def __init__(self,x,y,isla):
        Objeto.__init__(self)
        self.isla = isla
        self.mObjetos = isla.getMapaObjetos()
        self.mMovibles = isla.getMapaMovible()
        self.x = x
        self.y = y
        self.moves = []

    def move(self,x,y):
        if self.mObjetos[self.y + y][self.x + x] is None and self.mMovibles[self.y + y][self.x + x] is None:
            self.mMovibles[self.y + y][self.x + x] = self
            self.mMovibles[self.y][self.x] = None
            self.x += x
            self.y += y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
            
    def moveToPosition(self,posX,posY):
        self.moves.clear()
        for y in range(self.y,self.y + posY):
            for x in range(self.x,self.x + posX):
                if self.x < self.x + posX:
                    self.moves.append([1,0])

                elif self.x > self.x + posX:
                    self.moves.append([-1,0])

        if self.y < self.y + posY:
            self.moves.append([0,1])

        elif self.y > self.y + posY:
            self.moves.append([0,-1])

    def makeMoves(self):
        if len(self.moves) > 0:
            self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])





    
    
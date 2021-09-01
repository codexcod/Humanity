from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
import math

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
            return True
        
        return False

    def getX(self):
        return self.x

    def getY(self):
        return self.y
            
    def moveToPosition(self,posX,posY):
        self.moves.clear()
        
    
        for y in range(abs(posY - self.y)):
            
            if posY - self.y > 0:
                self.moves.append([0,1])

            elif posY - self.y < 0:
                self.moves.append([0,-1])

        for x in range(abs(posX - self.x)):
            if posX - self.x > 0:
                self.moves.append([1,0])

            elif posX - self.x < 0:
                self.moves.append([-1,0])


    def makeMoves(self):
        if len(self.moves) > 0:
            if self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1]):
                self.moves.pop(len(self.moves) - 1)

            else:
                if self.moves[len(self.moves) - 1][0] == 0:
                    self.moves.append([1,0])

                else:
                    self.moves.append([0,1])
            





    
    
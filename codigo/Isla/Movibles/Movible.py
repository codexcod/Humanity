from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
import math
import random 

class Movible(Objeto):

    def __init__(self, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.mObjetos = self.isla.getMapaObjetos()
        self.mMovibles = self.isla.getMapaMovible()
        self.moves = []
        self.directionX = 0
        self.directionY = 0
        
 

    def move(self, x, y):
        if not (self.x + x + 1 >= self.isla.getAncho() or self.x + x  - 1 <= 0) and not (self.y + y  + 1 >= self.isla.getAltura() or self.y + y - 1 <= 0):
        # Si el movimiento no lo lleva afuera del mapa 
            if self.mObjetos[self.y + y][self.x + x] is None and self.mMovibles[self.y + y][self.x + x] is None:
                
                    self.mMovibles[self.y + y][self.x + x] = self
                    self.mMovibles[self.y][self.x] = None
                    self.x += x
                    self.y += y
                    return True

            elif not self.mObjetos[self.y + y][self.x + x] is None and self.mObjetos[self.y + y][self.x + x].getCaminable():
                    self.mMovibles[self.y + y][self.x + x] = self
                    self.mMovibles[self.y][self.x] = None
                    self.x += x
                    self.y += y
                    return True
        
        return False

    
            
    def moveToPosition(self, posX, posY):
        # Se mueve a la posicion deseada a traves de varios pasos
        self.moves.clear()
        
        for y in range(abs(posY - self.y)):
            # Agrega movimientos en Y
            if posY - self.y > 0:
                self.moves.append([0, 1])
            # Agrega movimientos en Y
            elif posY - self.y < 0:
                self.moves.append([0, -1])

        for x in range(abs(posX - self.x)):
            # Agrega movimientos en X
            if posX - self.x > 0:
                self.moves.append([1, 0])
            # Agrega movimientos en X
            elif posX - self.x < 0:
                self.moves.append([-1, 0])

        self.directionX = 0
        self.directionY = 0
        for move in self.moves:
            self.directionX += move[0]
            self.directionY += move[1]
                

    def agregarMovimientos(self, movimientos):
        # Agrega movimientos 
        for i in range(movimientos):
                if random.choice([0, 1]) == 0:
                    self.moves.append([0, random.choice([-1, 1])])

                else:
                    self.moves.append([random.choice([-1, 1]), 0])
            

    def makeMoves(self):
        # Averigua si tiene movimientos
        if len(self.moves) > 0:
            if self.move(self.moves[len(self.moves) - 1][0], self.moves[len(self.moves) - 1][1]):
                self.moves.pop(len(self.moves) - 1)
                

            else:
                
                if self.moves[len(self.moves) - 1][0] == 0:

            
                    if self.directionX > 0:
                        self.moves.append([1, 0])
                        self.moves.insert(0, [-1, 0])

                    else:
                        self.moves.append([-1, 0])
                        self.moves.insert(0, [1, 0])

                else:
                    
                    if self.directionY > 0:
                        self.moves.append([0, 1])
                        self.moves.insert(0, [0, -1])

                    else:
                        self.moves.append([0, -1])
                        self.moves.insert(0, [0, 1])

    def tieneAlLado(self, x, y):
        return (self.getX() == x - 1  and self.getY() == y) or (self.getX() == x + 1 and self.getY() == y) or (self.getX() == x  and self.getY() == y - 1) or (self.getX() == x and self.getY() == y + 1) 
                    
            





    
    
from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper
import random 

class Animal(Movible):

    def __init__(self, x, y, isla,vida):
        Movible.__init__(self, x, y, isla)
        self.ticks = 0  
        self.vida = vida
        self.muerto = False
        

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

        self.directionX = 0
        self.directionY = 0
        for move in self.moves:
            self.directionX += move[0]
            self.directionY += move[1]


    def makeMoves(self):
        self.ticks += 1
        if self.ticks == 10:
            self.ticks = 0
        
            self.agregarMovimientos(4)

        if len(self.moves) > 0:
            self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])
            self.moves.pop(len(self.moves) - 1)
                

    def agregarMovimientos(self,movimientos):
        for i in range(movimientos):
                if random.choice([0,1]) == 0:
                    self.moves.append([0,random.choice([-1,1])])

                else:
                    self.moves.append([random.choice([-1,1]),0])
            


    def getInfoStr(self):
        result = f"""Nombre : {self.nombre}"""
        return resultç

    def getVida(self):
        return self.vida
    
    def setVida(self,vida):
        self.vida = vida

    def restarVida(self,resta):
        self.vida -= resta
    
    def sumarVida(self,suma):
        self.vida += suma
        
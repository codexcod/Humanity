from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper
import random 

class Conejo(Movible):

    def __init__(self, x, y, isla):
        Movible.__init__(self, x, y, isla)
        self.animacion = 0
        self.image = Helper.CONEJO(self.animacion)
        self.carne = 0
        self.nombre = "conejo" 
        self.ticks = 0  
        
    
    def setCarne(self,troncos):
        self.carne = carne
    
    def getCarne(self):
        return self.carne



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
        self.animacion += 1
        if self.animacion == 14:
            self.animacion = 0
        self.setImage(Helper.CONEJO(self.animacion))
        if self.ticks == 10:
            self.ticks = 0
        
            for i in range(4):
                if random.choice([0,1]) == 0:
                    self.moves.append([0,random.choice([-1,1])])

                else:
                    self.moves.append([random.choice([-1,1]),0])

        if len(self.moves) > 0:
            self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])
            self.moves.pop(len(self.moves) - 1)
                

        
            


    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Carne : {self.carne}"""
        return result
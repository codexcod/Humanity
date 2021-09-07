from codigo.Isla.Movibles.Animal import Animal
from codigo.Isla.Helper import Helper
import random 

class Vaca(Animal):

    def __init__(self, x, y, isla, vida):
        Animal.__init__(self, x, y, isla,vida)
        self.animacion = 0
        self.image = Helper.VACA(self.animacion)
        self.carne = 0
        self.nombre = "Vaca" 
        self.ticks = 0  
        
    
    def setCarne(self,troncos):
        self.carne = carne
    
    def getCarne(self):
        return self.carne

    def makeMoves(self):
        self.ticks += 1
        if self.animacion == 3:
            self.animacion = 0
        self.setImage(Helper.VACA(self.animacion))
        if self.ticks == 20:
            self.ticks = 0
        
            for i in range(4):
                if random.choice([0,1]) == 0:
                    self.moves.append([0,random.choice([-1,1])])

                else:
                    self.moves.append([random.choice([-1,1]),0])

        if len(self.moves) > 0:
            self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])
            self.moves.pop(len(self.moves) - 1)
            self.animacion += 1
                

    def getInfoStr(self):
        result = f"""Nombre : {self.nombre}
Carne : {self.carne}
Vida : {self.vida}"""
        return result
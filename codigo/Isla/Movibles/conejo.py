from codigo.Isla.Movibles.Animal import Animal
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Carne import Carne
import random 

class Conejo(Animal):

    def __init__(self, x, y, isla, vida):
        Animal.__init__(self, x, y, isla,vida)
        self.animacion = 0
        self.image = Helper.CONEJO(self.animacion)
        self.carne = 10
        self.nombre = "Conejo" 
        self.ticks = 0  
        
    
    def setCarne(self,troncos):
        self.carne = carne
    
    def getCarne(self):
        return self.carne

    def makeMoves(self):
        if not self.muerto:
            self.ticks += 1
            self.animacion += 1
            if self.animacion == 14:
                self.animacion = 0
            self.setImage(Helper.CONEJO(self.animacion))
            if self.ticks == 10:
                self.ticks = 0
            
                self.agregarMovimientos(4)

            if len(self.moves) > 0:
                self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])
                self.moves.pop(len(self.moves) - 1)
                

    def getInfoStr(self):
        result = f"""Nombre : {self.nombre}
Carne : {self.carne}
Vida : {self.vida}"""
        return result

    def getTrabajo(self):
        if not self.muerto:
            return 1
        
        return self.carne * 5

    def onClick(self):
        self.sacarVida(1)
        self.agregarMovimientos(6)

    def sacarVida(self,vida):
        self.vida -= vida
        if self.vida <= 0:
            self.matar()
            

    def getValor(self):
        if self.muerto == True:
            valor = []
            for i in range(self.carne):
                valor.append(Carne())

            self.isla.getAnimales().remove(self)
            self.isla.getMapaMovible()[self.y][self.x] = None
            return valor

    def matar(self):
        self.muerto = True
        self.setImage(Helper.CONEJO(14))
        self.setNombre("Conejo Muerto")
        
from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper
import random 

class Animal(Movible):

    def __init__(self, x, y, isla, vida):
        Movible.__init__(self, x, y, isla)
        self.ticks = 0  
        self.vida = vida
        self.muerto = False
        

    def moveToPosition(self,posX,posY):
        # Se mueve a la posicion deseada a traves de varios pasos
        self.moves.clear()
        
        for y in range(abs(posY - self.y)):
            
            if posY - self.y > 0:
                # Si la posicion de Y del animal es mayor a la posicion de Y del objetivo
                self.moves.append([0, 1])

            elif posY - self.y < 0:
                # Si la posicion de Y del animal es menor a la posicion de Y del objetivo
                self.moves.append([0, -1])

        for x in range(abs(posX - self.x)):

            if posX - self.x > 0:
                # Si la posicion de X del animal es mayor a la posicion de X del objetivo
                self.moves.append([1, 0])

            elif posX - self.x < 0:
                # Si la posicion de X del animal es menor a la posicion de X del objetivo
                self.moves.append([-1, 0])

        self.directionX = 0
        self.directionY = 0
        for move in self.moves:
            self.directionX += move[0]
            self.directionY += move[1]


    def makeMoves(self):
        # Cada cierta cantidad de tiempo genera 4 movimientos alelatorios
        self.ticks += 1
        if self.ticks == 10:
            self.ticks = 0
        
            self.agregarMovimientos(4)

        if len(self.moves) > 0:
            # Hace el movimiento que se encuentra para hacer
            self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1])
            self.moves.pop(len(self.moves) - 1)
                



    def getInfoStr(self):
        result = f"""Nombre : {self.nombre}"""
        return result

    def getVida(self):
        return self.vida
    
    def setVida(self, vida):
        self.vida = vida

    def restarVida(self, vida):
        self.vida -= vida
        if self.vida <= 0:
            self.matar()
    
    def sumarVida(self, suma):
        self.vida += suma

    def matar(self):
        self.muerto = True
        self.setNombre(f"{self.nombre} Muerto")

    def getMuerto(self):
        return self.muerto

    def setMuerto(self, muerto):
        self.muerto = muerto
        
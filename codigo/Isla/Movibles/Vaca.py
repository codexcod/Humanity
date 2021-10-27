from codigo.Isla.Movibles.Animal import Animal
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Carne import Carne
import random 

class Vaca(Animal):

    def __init__(self, x, y, isla, vida):
        Animal.__init__(self, x, y, isla, vida)
        self.animacion = 0
        self.image = Helper.VACA(self.animacion)
        self.carne = 20
        self.nombre = "Vaca" 
        self.ticks = 0
        self.maxTick = random.randrange(18,23)

    def toJson(self):
        return {
            'objeto' : 'Vaca',
            'name' : self.nombre,
            'vida' : self.vida,
            'muerto' : self.muerto,
            'x' : self.x,
            'y' : self.y
        }
        
    
    def setCarne(self, carne):
        self.carne = carne
    
    def getCarne(self):
        return self.carne

    def makeMoves(self):
        if not self.muerto:
            self.ticks += 1
            if self.animacion == 3:
                self.animacion = 0
                # Que vaya avanzando la animacion de acuerdo a los ticks
            self.setImage(Helper.VACA(self.animacion))
            if self.ticks == self.maxTick:
                self.ticks = 0
                # Agrega moves alelatorios tanto en X como en Y, de acuerdo a los ticks
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

    def onClick(self):
        # en el caso que le peguen, que le reste vida y que se mueva
        self.restarVida(1)
        self.agregarMovimientos(6)


    def getValor(self):
        # En el caso de que este muerto y se le haya pegado
        if self.muerto == True:
            valor = []
            # Que se le agregue carne al inventario
            for i in range(self.carne):
                valor.append(Carne())

            self.isla.getAnimales().remove(self)
            # Que saque a la vaca de la lista de animales
            self.isla.getMapaMovible()[self.y][self.x] = None
            # Que desaparezca del mapa
            return valor

    def getTrabajo(self):
        if not self.muerto:
            return 1
        
        return self.carne * 5

    def matar(self):
        self.muerto = True
        self.setImage(Helper.VACA(4))
        self.setNombre("Vaca Muerta")
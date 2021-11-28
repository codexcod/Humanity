from codigo.Isla.Movibles.Animal import Animal
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Carne import Carne
import random


class Jabali(Animal):

    def __init__(self, x, y, isla, vida):
        Animal.__init__(self, x, y, isla, vida)
        self.image = Helper.JABALI
        self.carne = 20
        self.nombre = "Vaca"
        self.ticks = 0
        self.maxTick = random.randrange(18, 23)

    def toJson(self):
        return {
            'objeto': 'Jabali',
            'name': self.nombre,
            'vida': self.vida,
            'muerto': self.muerto,
            'x': self.x,
            'y': self.y
        }

    def setCarne(self, carne):
        self.carne = carne

    def getCarne(self):
        return self.carne

    def makeMoves(self):
        if not self.muerto:
            for i in range(4):
                if random.choice([0, 1]) == 0:
                    self.moves.append([0, random.choice([-1, 1])])

                else:
                    self.moves.append([random.choice([-1, 1]), 0])

            if len(self.moves) > 0:
                self.move(self.moves[len(self.moves) - 1][0], self.moves[len(self.moves) - 1][1])
                self.moves.pop(len(self.moves) - 1)
                self.animacion += 1

    def getInfoStr(self):
        result = f"""Nombre : {self.nombre}
Carne : {self.carne}
Vida : {self.vida}"""
        return result

    def onClick(self, herramienta):
        # en el caso que le peguen, que le reste vida y que se mueva
        self.restarVida(herramienta)
        self.agregarMovimientos(6)

    def getValor(self):
        if self.muerto == True:
            valor = []
            for i in range(self.carne):
                valor.append(Carne())

            self.isla.getAnimales().remove(self)
            self.isla.getMapaMovible()[self.y][self.x] = None
            return valor

    def getTrabajo(self, herramienta):
        if not self.muerto:
            return 1

        return self.carne * 5

    def matar(self):
        self.muerto = True
        self.setImage(Helper.VACA(4))
        self.setNombre("Jabali Muerta")

    def buscarPersonas(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isPersona():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

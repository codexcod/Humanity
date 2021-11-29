from codigo.Isla.Movibles.Animal import Animal
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Carne import Carne
import random

from codigo.MovedorDePersonas.Asterisco import Asterisco


class Jabali(Animal):

    def __init__(self, x, y, isla, vida):
        Animal.__init__(self, x, y, isla, vida)
        self.image = Helper.JABALI(1)
        self.carne = 15
        self.nombre = "Jabali"
        self.ticks = 0
        self.animacion = 1
        self.maxTick = random.randrange(12, 23)
        self.accionar = [False, None]

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
            self.ticks += 1
            self.animacion += 1
            if self.animacion >= 6:
                self.animacion = 1

            self.setImage(Helper.JABALI(self.animacion))
            if self.ticks == self.maxTick:
                self.ticks = 0
                self.agregarMovimientos(4)
                self.accionar = [False, None]

            self.debeAtacar()

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
        self.buscarPersonas()

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
        self.setImage(Helper.JABALI(4))
        self.setNombre("Jabali Muerto")

    def buscarPersonas(self):
        for y in range(self.y - 5, self.y + 5):
            for x in range(self.x - 5, self.x + 5):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isPersona():
                                self.accionarObjeto(self.isla.getMapaMovible()[y][x])

                                return True

        return False

    def accionarObjeto(self, objeto):
        self.moveToPosition(objeto.getX(), objeto.getY())
        self.accionar = [True, objeto]


    def moveToPosition(self, posX, posY):
        self.moves.clear()
        asterisco = Asterisco(self.isla)
        asterisco.empiezaElCodiguito(self.x, self.y, posX, posY)
        listaDeMovimientos = asterisco.getCaminito()

        # La lista te llegara con los nodos por los cuales tenes que pasar para poder llegar al objetivo
        for nodo in listaDeMovimientos:

            if nodo.getPadreMia() is None:
                pass
            # En el caso que no tenga padre, entonces estaras en el nodo incial, por ende no habra que
            # caminar hacia ese nodo

            else:
                # Al pasar por cada nodo en la lista, buscas su posicion en X e Y, de tal manera que
                # se puedan comparar con la X e Y del nodo en el que estabas, osea su padre
                if nodo.getX() > nodo.getPadreMia().getX():
                    self.moves.append([1, 0])
                if nodo.getX() < nodo.getPadreMia().getX():
                    self.moves.append([-1, 0])
                if nodo.getY() > nodo.getPadreMia().getY():
                    self.moves.append([0, 1])
                if nodo.getY() < nodo.getPadreMia().getY():
                    self.moves.append([0, -1])

    def debeAtacar(self):
        if self.accionar[0]:
            if self.tieneAlLado(self.accionar[1].getX(), self.accionar[1].getY()):
                self.accionar[1].dañar(5)

            elif len(self.moves) == 1:
                if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    self.accionarObjeto(self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()])

                else:
                    self.accionarObjeto(self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()])

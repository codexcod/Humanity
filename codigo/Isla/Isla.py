import random

from codigo.Isla.Estaticos.Agua import Agua
from codigo.Isla.Estaticos.Arena import Arena
from codigo.Isla.Estaticos.Pasto import Pasto
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.NoiseGenerator import NoiseGenerator
from codigo.Isla.Objetos.Arbol import Arbol
from codigo.Isla.Objetos.Casa import Casa
from codigo.Isla.Objetos.Fogata import Fogata
from codigo.Isla.Objetos.Piedra import Piedra


class Isla:

    def __init__(self, ancho, altura):
        self.mEstatico = []
        self.mMovible = []
        self.mObjetos = []
        self.ancho = ancho
        self.altura = altura
        self.generarMapaObjetos()
        self.generarMapaEstatico()
        self.generarMapaMovible()

    def generarMapaEstatico(self):
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if x == 1 or y == 1 or x == self.ancho - 1 or y == self.altura - 1:
                    fila.append(Agua())
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None

                elif x == 2 or x == 3 or y == 2 or y == 3 or x == self.ancho - 2 or y == self.altura - 2 or x == self.ancho - 3 or y == self.altura - 3:

                    fila.append(Arena())
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None


                else:
                    fila.append(Pasto())

            self.mEstatico.append(fila)

    def generarMapaObjetos(self):
        arboles = NoiseGenerator(self.ancho, self.altura, None, Arbol())
        mArboles = arboles.getNoise()

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if not mArboles[y][x] is None:
                    mArboles[y][x] = Arbol()
                    mArboles[y][x].setTroncos(random.randrange(5, 20))
                    fila.append(mArboles[y][x])

                elif random.randrange(1, 50) == 1:
                    piedra = Piedra()
                    piedra.setPiedras(random.randrange(5, 20))
                    if random.randrange(1, 5) == 1:
                        piedra.setOro(random.randrange(1, 3))

                    fila.append(piedra)


                else:
                    fila.append(mArboles[y][x])

            self.mObjetos.append(fila)

    def generarMapaMovible(self):
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mMovible.append(fila)

    def getMapaEstatico(self):
        return self.mEstatico

    def getMapaObjetos(self):
        return self.mObjetos

    def getMapaMovible(self):
        return self.mMovible

    def getAncho(self):
        return self.ancho

    def getAltura(self):
        return self.altura

    def agregarObjeto(self, x, y, objeto):
        """
        if not self.mObjetos[y][x] is None:
            
            return True
        
        return False"""
        self.mObjetos[y][x] = objeto

    def agregarMovible(self, x, y, objeto):
        """
        if not self.mObjetos[y][x] is None:

            return True

        return False"""
        self.mMovible[y][x] = objeto

    def moverMovible(self, x, y, difX, difY):
        self.mMovible[y + difY][x + difX] = self.mMovible[y][x]
        self.mMovible[y][x] = None

    def agregarAldea(self, aldea, posX, posY):
        for y in range(posY - 5, posY + 5):
            for x in range(posX - 5, posX + 5):
                self.mObjetos[y][x] = None

        casa = Casa(aldea)
        self.agregarObjeto(posX, posY - 2, casa)
        aldea.agregarCasa(casa)
        juan = Persona("Juan", casa)
        self.agregarMovible(posX - 3, posY, juan)
        casa.agregarPersona(juan)
        tuke = Persona("Tuke", casa)
        self.agregarMovible(posX + 3, posY, tuke)
        casa.agregarPersona(tuke)
        gonza = Persona("Gonza", casa)
        self.agregarMovible(posX, posY - 4, gonza)
        casa.agregarPersona(gonza)
        fogata = Fogata(aldea)
        self.agregarObjeto(posX, posY, fogata)
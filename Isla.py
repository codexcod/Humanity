import random
import pygame

from Objeto import Objeto
from Objetos import Objetos
from Arbol import Arbol
from Piedra import Piedra
from Pasto import Pasto
from Arena import Arena
from Agua import Agua
from NoiseGenerator import NoiseGenerator


class Isla:

    def __init__(self, ancho, altura):
        self.mEstatico = []
        self.mMovible = []
        self.mObjetos = []
        self.ancho = ancho
        self.altura = altura
        self.generarMapaObjetos()
        self.generarMapaEstatico()
    
        
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
        arboles = NoiseGenerator(self.ancho,self.altura,None,Arbol())
        mArboles = arboles.getNoise()

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if not mArboles[y][x] is None:
                    mArboles[y][x] = Arbol()
                    mArboles[y][x].setTroncos(random.randrange(5,20))
                    fila.append(mArboles[y][x])
                
                elif random.randrange(1,50) == 1:
                    piedra = Piedra()
                    piedra.setPiedras(random.randrange(5,20))
                    fila.append(piedra)

                else:
                    fila.append(mArboles[y][x])


            self.mObjetos.append(fila)


        

    def getMapaEstatico(self):
        return self.mEstatico
    
    def getMapaObjetos(self):
        return self.mObjetos

    def getAncho(self):
        return self.ancho

    def getAltura(self):
        return self.altura

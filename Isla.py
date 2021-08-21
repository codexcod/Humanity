import random
import pygame
from Objetos import Objetos


class Isla:

    def __init__(self, ancho, altura):
        self.mEstatico = []
        self.mMovible = []
        self.mObjetos = []
        self.ancho = ancho
        self.altura = altura

    def generarMapaEstatico(self):
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if x == 1 or y == 1 or x == self.ancho - 1 or y == self.altura - 1:
                    fila.append(Objetos.AGUA)

                elif x == 2 or x == 3 or y == 2 or y == 3 or x == self.ancho - 2 or y == self.altura - 2 or x == self.ancho - 3 or y == self.altura - 3:
                    if random.randrange(1, 10) < 9:
                        fila.append(Objetos.ARENA)
                    else:
                        fila.append(Objetos.PASTO)

                else:
                    fila.append(Objetos.PASTO)

            self.mEstatico.append(fila)

    def getMapaEstatico(self):
        return self.mEstatico

    def getAncho(self):
        return self.ancho

    def getAltura(self):
        return self.altura

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
            lista = []
            for x in range(self.ancho):
                if x == 1 or y == 1 or x == self.ancho - 1 or y == self.altura - 1:
                    lista.append(Objetos.AGUA)
                else:
                    lista.append(Objetos.PASTO)

            self.mEstatico.append(lista)

    def getMapaEstatico(self):
        return self.mEstatico

    def getAncho(self):
        return self.ancho

    def getAltura(self):
        return self.altura





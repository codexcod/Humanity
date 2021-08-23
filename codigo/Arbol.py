import pygame
from Objetos import Objetos
from Objeto import Objeto


class Arbol(Objeto):

    def __init__(self):
        Objeto.__init__(self)
        self.setNombre("Arbol")
        self.setImage(Objetos.ARBOL)
        self.troncos = 0
        self.talado = False

    def setTroncos(self,troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            self.setImage(Objetos.ARBOL_GRANDE)

        else:
            self.setImage(Objetos.ARBOL)

    def getTroncos(self):
        return self.troncos

    def onClick(self):
        if not self.talado:
            self.talarArbol()
        return super().onClick()

    def talarArbol(self):
        self.talado = True
        self.setImage(Objetos.ARBOL_TALADO)
        self.setNombre("Arbol talado")


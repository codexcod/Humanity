import pygame 
from Objetos import Objetos
from Objeto import Objeto


class Piedra(Objeto):

    def __init__(self):
        Objeto.__init__(self)
        self.setNombre("Piedra")
        self.image = Objetos.PIEDRA
        self.piedras = 0
        self.talado = False

    def setPiedras(self,piedras):
        self.piedras = piedras

    def getPiedras(self):
        return self.piedras
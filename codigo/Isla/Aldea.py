import pygame

class Aldea:

    def __init__(self,nombre):
        self.nombre = nombre
        self.troncos = 0
        self.piedras = 0
        self.oro = 0
        self.casas = []
        self.personas = []

    def getNombre(self):
        return self.nombre

    def getMadera(self):
        return self.troncos

    def agregarTroncos(self,troncos):
        self.troncos += 10

    def getPiedra(self):
        return self.piedras

    def agregarPiedras(self,piedras):
        self.piedras += 10

    def agregarCasa(self,casa):
        self.casas.append(casa)

    def agregarPersona(self,persona):
        self.personas.append(persona)

    
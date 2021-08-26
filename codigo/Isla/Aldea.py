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

    def agregarCasa(self,casa):
        self.casas.append(casa)

    def agregarPersona(self,persona):
        self.personas.append(persona)

    
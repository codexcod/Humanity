from codigo.Isla.Helper import Helper


class Herramienta:

    def __init__(self):
        self.nombre = ""
        self.daño = 0


    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
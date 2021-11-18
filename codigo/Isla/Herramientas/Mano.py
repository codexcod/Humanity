from codigo.Isla.Herramientas.Herramienta import Herramienta

class Mano(Herramienta):


    def __init__(self):
        Herramienta.__init__(self)
        self.dañoPiedra = 10
        self.dañoArbol = 0
        self.dañoPersona = 1
        self.dañoAnimal = 1
        

    def restarUso(self):
        self.usos -= 1
        if self.usos == 0:
            self.rota = True
            
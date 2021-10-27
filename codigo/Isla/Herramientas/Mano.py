from codigo.Isla.Herramientas.Herramienta import Herramienta

class Mano(Herramienta):


    def __init__(self):
        # Es la herramienta base, o la FALTA de herramienta
        Herramienta.__init__(self)
        self.dañoPiedra = 0
        self.dañoArbol = 0
        self.dañoPersona = 0
        self.dañoAnimal = 0
        

    def restarUso(self):
        self.usos -= 1
        if self.usos == 0:
            self.rota = True
            
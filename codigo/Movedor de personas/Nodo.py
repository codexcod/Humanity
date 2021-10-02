from codigo.Isla.Objetos import Objeto

class nodo:

    def _init_(self, padreMia = None, posicion = None):
        self.padreMia = padreMia
        self.posicion = posicion
        self.caminable = True
        self.costo = 0
        self.valorProbable = 0
        self.total = 0
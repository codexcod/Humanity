from codigo.MovedorDePersonas.Nodo import Nodo


class Asterisco:

    def __init__(self, isla):
        self.isla = isla
        self.abierta = []
        self.caminito = []

    def agregarACaminito(self, Nodo):
        self.caminito.append(Nodo)

    def getNodoAnterior(self):
        return self.caminito[len(self.caminito) - 1]

    def agregar(self, Nodo):
        self.abierta.append(Nodo)

    def empiezaElCodiguito(self, inicioX, inicioY, finalX, finalY):
        inicioNodo = Nodo(inicioY, inicioX, None)
        self.agregarACaminito(inicioNodo)
        for y in range(abs(finalY - self.getNodoAnterior().getY())):

            if finalY - inicioY > 0:
                self.agregarACaminito(
                    Nodo(self.getNodoAnterior().getY() + 1, self.getNodoAnterior().getX(), self.getNodoAnterior()))

            elif finalY - inicioY < 0:
                self.agregarACaminito(
                    Nodo(self.getNodoAnterior().getY() - 1, self.getNodoAnterior().getX(), self.getNodoAnterior()))

        for x in range(abs(finalX - self.getNodoAnterior().getX())):
            if finalX - inicioX > 0:
                self.agregarACaminito(
                    Nodo(self.getNodoAnterior().getY(), self.getNodoAnterior().getX() + 1, self.getNodoAnterior()))

            elif finalX - inicioX < 0:
                self.agregarACaminito(
                    Nodo(self.getNodoAnterior().getY(), self.getNodoAnterior().getX() - 1, self.getNodoAnterior()))

        '''
        inicioNodo = Nodo(inicioY, inicioX, None)
        objetivoNodo = Nodo(finalY, finalX, None)
        limite = 512
        vecesQueSeHizo = 0
        self.agregar(inicioNodo)

        while len(self.abierta) > 0:
            vecesQueSeHizo += 1
            nodoActual = self.caminito[1]
            self.agregarACaminito(nodoActual)
            self.caminito.pop[nodoActual]

            if nodoActual == objetivoNodo:
                exit()

            for nodo in vecinos():
                if nodo.caminable:
                    if not nodo in self.abierta():
                        nodo.setCosto("algo")
                        nodo.setValorProbable("otroAlgo")
                        nodo.setPadreMia(nodoActual)
                        self.abierta.append(nodo)

        if vecesQueSeHizo > limite:
            self.abierta = []
            self.caminito = []
            return "No se encontraron arboles cercanos"
    
    def devuelveCaminito(self, nodoFinal):
        nodo = nodoFinal
        while nodo is not None:

            caminito.append.(nodoFinal.posicion)
        nodoFinal = nodoFinal.padreMia

        return caminito
    '''

    # Generalmente se le da vuelta pero en nuestro codigo como lo tendriamos que dar
    def getCaminito(self):
        return self.caminito

from codigo.MovedorDePersonas.Nodo import nodo


class Asterisco():

    def __init__(self, isla):
        self.isla = isla
        self.abierta = []
        self.cerrada = []
        self.caminito = []

    def agregarACaminito(self, nodo):
        self.caminito.append(nodo)

    def getNodoAnterior(self):
        return self.caminito[len(self.caminito) - 1]

    def agregar(self, nodo):
        self.abierta.append(nodo)

    def empiezaElCodiguito(self, inicioX, inicioY, finalX, finalY):
        inicioNodo = nodo(inicioY, inicioX, None)
        self.caminito.append(inicioNodo)

        for y in range(abs(finalY - self.getNodoAnterior().getY())):

            if finalY - inicioY > 0:
                self.agregarACaminito(
                    nodo(self.getNodoAnterior().getY() + 1, self.getNodoAnterior().getX(), self.getNodoAnterior()))

            elif finalY - inicioY < 0:
                self.agregarACaminito(
                    nodo(self.getNodoAnterior().getY() - 1, self.getNodoAnterior().getX(), self.getNodoAnterior()))

        for x in range(abs(finalX - self.getNodoAnterior().getX())):
            if finalX - inicioX > 0:
                self.agregarACaminito(
                    nodo(self.getNodoAnterior().getY(), self.getNodoAnterior().getX() + 1, self.getNodoAnterior()))

            elif finalX - inicioX < 0:
                self.agregarACaminito(
                    nodo(self.getNodoAnterior().getY(), self.getNodoAnterior().getX() - 1, self.getNodoAnterior()))
        '''
            inicioNodo = nodo(inicioY, inicioX, None)
            inicioNodo.costo = 0
            inicioNodo.valorProbable = 0
            inicioNodo.total = 0
            objetivoNodo = nodo(finalY, inicioX, None)
            objetivoNodo.costo = 0
            objetivoNodo.valorProbable = 0
            objetivoNodo.total = 0
            limite = 1000
            vecesQueSeHizo = 0
            self.abierta.append(inicioNodo)

            while len(self.abierta) > 0:
                vecesQueSeHizo += 1
                nodoActual = self.abierta[1]
                self.cerrada.append(nodoActual)

                if nodoActual == objetivoNodo:
                    return (devuelveCaminito(nodoActual))

            if vecesQueSeHizo > limite:
                return "No se encontraron arboles cercanos" 
        '''

    '''                
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

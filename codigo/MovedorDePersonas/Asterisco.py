from Nodo import nodo

class Asterisco():

    def __init__(self, isla):
        self.isla = isla
        self.abierta = []
        self.cerrada = []
        self.caminito = []

    def agregar(self, nodo):
        self.abierta.append(nodo)

    def empiezaElCodiguito(self, inicioX, inicioY, finalX, finalY):
        for y in range(abs(finalY - self.y)):
            # Agrega movimientos en Y
            if finalY - self.y > 0:
                self.moves.append([0, 1])
            # Agrega movimientos en Y
            elif finalY - self.y < 0:
                self.moves.append([0, -1])

        for x in range(abs(finalX - self.x)):
            # Agrega movimientos en X
            if finalX - self.x > 0:
                self.moves.append([1, 0])
            # Agrega movimientos en X
            elif finalX - self.x < 0:
                self.moves.append([-1, 0])

        self.directionX = 0
        self.directionY = 0
        for move in self.moves:
            self.directionX += move[0]
            self.directionY += move[1]
       ''' inicioNodo = nodo(None, inicio)
        inicioNodo.costo = 0
        inicioNodo.valorProbable = 0
        inicioNodo.total = 0
        objetivoNodo = nodo(None, final)
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
    def devuelveCaminito(self, nodoFinal):
        nodo = nodoFinal
        while nodo is not None:

            caminito.append.(nodoFinal.posicion)
        nodoFinal = nodoFinal.padreMia

        return caminito'''
        # Generalmente se le da vuelta pero en nuestro codigo como lo tendriamos que dar 

    def getCaminito(self):
        return self.caminito
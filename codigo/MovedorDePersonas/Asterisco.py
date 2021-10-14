from codigo.MovedorDePersonas.Nodo import nodo

class Asterisco():

    def __init__(self, isla):
        self.isla = isla
        self.abierta = []
        self.cerrada = []
        self.caminito = []

    def agregar(self, nodo):
        self.abierta.append(nodo)

    def empiezaElCodiguito(self, inicioX, inicioY, finalX, finalY):
        inicioNodo = nodo(inicioY, inicioX, None)
        self.caminito.append(inicioNodo)
        for y in range(abs(finalY - inicioY)):
            
            # Agrega movimientos en Y
            if finalY - inicioY > 0:
                self.caminito.append(nodo(inicioY + 1, inicioX, self.caminito[-1]))
            # Agrega movimientos en Y
            elif finalY - inicioY < 0:
                self.caminito.append([nodo(inicioY - 1, inicioX,self.caminito[-1]])

        for x in range(abs(finalX - inicioX)):
            # Agrega movimientos en X
            if finalX - inicioX > 0:
                self.caminito.append([nodo(inicioY, inicioX + 1,self.caminito[-1]])
            # Agrega movimientos en X
            elif finalX - inicioX < 0:
                self.caminito.append([nodo(inicioY, inicioX - 1,self.caminito[-1]])
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
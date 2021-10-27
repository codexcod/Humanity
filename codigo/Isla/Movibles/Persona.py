from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper
from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper
from codigo.Isla.Herramientas.Mano import Mano
from codigo.MovedorDePersonas.Asterisco import Asterisco
from codigo.MovedorDePersonas.Nodo import nodo


class Persona(Movible):

    def __init__(self, nombre, casa, x, y, isla):
        Movible.__init__(self, x, y, isla)
        self.edad = 0
        self.casa = casa
        self.nombre = nombre
        self.image = Helper.PERSONA
        self.inventario = []
        self.accionar = [False, 0, 0]
        self.trabajando = False
        self.tiempoTrabajando = 0
        self.herramienta = None
        self.vision = 5
        self.busqueda = 0

    def toJson(self):
        jsonText = {
            'objeto': 'Persona',
            'name': self.nombre,
            'edad': self.edad,
            'x': self.x,
            'y': self.y,
            'inventario': []
        }

        for objeto in self.inventario:
            jsonText['inventario'].append(objeto.toJson())

        return jsonText

    def setHerramienta(self, numInventario):
        self.herramienta = self.inventario[numInventario]

    def getHerramienta(self):
        return self.herramienta

    def getCasa(self):
        return self.casa

    def getAldea(self):
        return self.casa.getAldea()

    def getInfoStr(self):
        result = self.nombre
        return result

    def setEdad(self, edad):
        self.edad = edad

    def agregarInventario(self, objeto):
        # Agrega un objeto al inventario
        if not self.tieneInventarioLleno():
            self.inventario.append(objeto)

    def getInventario(self):
        return self.inventario

    def getUI(self, clickeables, lista, listaUI, ui):
        # Crea un UI para las personas
        info = []
        fondo = Helper.getSurface(800, 500)
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(25)
        texto = self.getInfoStr()
        lineas = texto.splitlines()
        forI = 0
        for i in lineas:
            textObject = font.render(i, True, (255, 255, 255), None)
            info.append(UIObject(textObject, 550, 70 + forI * 40))
            forI += 1

        image = Helper.getImage(self.getImage(), 200, 200)
        info.append(UIObject(image, 200, 200))

        forPosX = 0
        forPosY = 0
        for objeto in self.inventario:
            # Dibujan los objetos del inventario
            fondoObjeto = Helper.getImage(Helper.INVENTARIO, 40, 40)
            info.append(UIObject(fondoObjeto, 550 + 40 * forPosX, 120 + 40 * forPosY))
            # Dibuja primero el fondo del item
            imagenObjeto = Helper.getImage(objeto.getImage(), 30, 30)
            # Luego dibuja el item en si, encima del fondo
            info.append(UIObject(imagenObjeto, 550 + 40 * forPosX + 5, 120 + 40 * forPosY + 5))
            if forPosX == 7:
                forPosX = 0
                forPosY += 1

            else:

                forPosX += 1
        # Dibuja el fondo de la herramienta
        fondoHerramienta = Helper.getImage(Helper.INVENTARIO, 60, 60)
        info.append(UIObject(fondoHerramienta, 150, 100))

        if not self.herramienta is None:
            # Dibuja la herramienta en el caso de que tenga una
            imagenHerramienta = Helper.getImage(self.herramienta.getImage(), 40, 40)
            info.append(UIObject(imagenHerramienta, 160, 110))

        return info

    def moveToPosition(self, posX, posY):

        self.moves.clear()
        self.accionar[0] = False
        asterisco = Asterisco(self.isla)
        asterisco.empiezaElCodiguito(self.x, self.y, posX, posY)
        listaDeMovimientos = asterisco.getCaminito()
        # La lista te llegara con los nodos por los cuales tenes que pasar para poder llegar al objetivo
        for nodo in listaDeMovimientos:

            if nodo.getPadreMia() is None:
                pass
            # En el caso que no tenga padre, entonces estaras en el nodo incial, por ende no habra que 
            # caminar hacia ese nodo

            else:
                # Al pasar por cada nodo en la lista, buscas su posicion en X e Y, de tal manera que
                # se puedan comparar con la X e Y del nodo en el que estabas, osea su padre
                if nodo.getX() > nodo.getPadreMia().getX():
                    self.moves.append([1, 0])
                if nodo.getX() < nodo.getPadreMia().getX():
                    self.moves.append([-1, 0])
                if nodo.getY() > nodo.getPadreMia().getY():
                    self.moves.append([0, 1])
                if nodo.getY() < nodo.getPadreMia().getY():
                    self.moves.append([0, -1])
                print(self.moves)

    def accionarObjeto(self, objeto):
        if not self.trabajando:
            self.moveToPosition(objeto.getX(), objeto.getY())
            self.accionar = [True, objeto]

    def makeMoves(self):
        if not self.trabajando:
            if len(self.moves) > 0:
                if self.accionar[0]:
                    if self.tieneAlLado(self.accionar[1].getX(), self.accionar[1].getY()):
                        self.definirTrabajo(self.accionar[1])

                    elif len(self.moves) == 1:
                        if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                            self.accionarObjeto(
                                self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()])

                        else:
                            self.accionarObjeto(
                                self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()])

                if self.move(self.moves[len(self.moves) - 1][0], self.moves[len(self.moves) - 1][1]):
                    self.moves.pop(len(self.moves) - 1)

            else:
                if not self.busqueda == 0:
                    # Si tiene que buscar algo
                    if not self.accionar[0]:
                        if not self.tieneInventarioLleno():
                            if self.busqueda == 2:
                                # En el caso que este buscando piedras, que se agreguen 5 movimientos
                                if not self.buscarPiedras():
                                    self.agregarMovimientos(5)

                            elif self.busqueda == 1:
                                # En el caso que este buscando arboles, que se agreguen 5 movimientos
                                if not self.buscarArboles():
                                    self.agregarMovimientos(5)

                            elif self.busqueda == 4:
                                # En el caso que este buscando arbustos, que se agreguen 5 movimientos
                                if not self.buscarArbustos():
                                    self.agregarMovimientos(5)

                            elif self.busqueda == 3:
                                # En el caso que este buscando animales, que se agreguen 5 movimientos
                                if not self.buscarAnimales():
                                    self.agregarMovimientos(5)

                        else:
                            # En el caso que tenga el inventario lleno que vaya a guardar los recursos
                            self.guardarRecursos()


        else:
            self.trabajar()

    def guardarRecursos(self):
        self.accionarObjeto(self.getCasa())

    def puedeAgregarAlInventario(self):
        return len(self.inventario) > 80

    def tieneInventarioLleno(self):
        return len(self.inventario) >= 80

    def definirTrabajo(self, objeto):

        if not self.herramienta is None:
            # Si tiene herramienta
            herramienta = self.herramienta

        else:
            # Si no tiene su herramienta es la mano
            herramienta = Mano()

        # Si esta trabajando que le modifiquen la imagen
        if objeto.getNombre()[:4] == "Casa":
            if self.tieneAlgoEnElInventario():
                self.trabajando = True
                self.tiempoTrabajando = len(self.inventario)
                self.setImage(Helper.PERSONA_TRABAJANDO)


        elif not objeto.getTrabajo(herramienta) == 0:
            self.trabajando = True
            self.tiempoTrabajando = objeto.getTrabajo(herramienta)

            self.setImage(Helper.PERSONA_TRABAJANDO)

    def trabajar(self):
        if not self.herramienta is None:
            # Si tiene herramienta
            herramienta = self.herramienta

        else:
            # Si no tiene su herramienta es la mano
            herramienta = Mano()
        if self.trabajando:
            # Si esta trabajando, que le reste un poco de tiempo de trabajo, 
            self.tiempoTrabajando -= 1
            if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                if self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].getNombre()[
                   :4] == "Casa":
                    # Si esta "trabajando" en la aldea, que guarde su inventario en la aldea
                    self.isla.getMapaObjetos()[self.accionar[1].getY()][
                        self.accionar[1].getX()].getAldea().añadirObjeto(self.inventario[len(self.inventario) - 1])
                    self.inventario.pop(len(self.inventario) - 1)

            if self.tiempoTrabajando == 0:
                # Si termino de trabajar
                self.trabajando = False
                self.setImage(Helper.PERSONA)
                if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    if not self.isla.getMapaObjetos()[self.accionar[1].getY()][
                               self.accionar[1].getX()].getValor() is None:
                        # se fija si la X y la Y del accionar tengan un valor
                        for objeto in self.isla.getMapaObjetos()[self.accionar[1].getY()][
                            self.accionar[1].getX()].getValor():
                            # Si era un objeto en el que estaba trabajando, que agregue sus items en el inventario
                            self.agregarInventario(objeto)
                    self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].onClick(herramienta)

                elif not self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    valor = self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()].getValor()
                    # Si era un movible en el que estaba trabajando, que agregue sus valores en el inventario
                    if not valor is None:
                        for objeto in valor:
                            self.agregarInventario(objeto)

                    else:
                        self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()].onClick(
                            herramienta)

                self.accionar[0] = False
                self.moves.clear()

    def tieneAlgoEnElInventario(self):
        return len(self.inventario) > 0

    def buscarArboles(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            # Se fija dentro de su vision( cantidad de bloques que puede ver) en Y
            for x in range(self.x - self.vision, self.x + self.vision):
                # Como en X
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    # ( Obviamente si estan dentro de la X
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        # Como de la Y del mapa)
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbol():
                                # Si hay un arbol dentro de ahi, en ese caso que lo vaya a talar
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarPiedras(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            # Se fija dentro de su vision( cantidad de bloques que puede ver) en Y
            for x in range(self.x - self.vision, self.x + self.vision):
                # Como en X
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    # ( Obviamente si estan dentro de la X
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        # Como de la Y del mapa)
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isPiedra():
                                # Si hay una piedra dentro de ahi, en ese caso que lo vaya a minar
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarArbustos(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            # Se fija dentro de su vision( cantidad de bloques que puede ver) en Y
            for x in range(self.x - self.vision, self.x + self.vision):
                # Como en X
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    # ( Obviamente si estan dentro de la X
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        # Como de la Y del mapa)
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbusto():
                                # Si hay un arbusto dentro de ahi, en ese caso que lo vaya a talar?(no se como se llama lo que se le hace al arbusto)
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarAnimales(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            # Se fija dentro de su vision( cantidad de bloques que puede ver) en Y
            for x in range(self.x - self.vision, self.x + self.vision):
                # Como en X
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    # ( Obviamente si estan dentro de la X
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        # Como de la Y del mapa)
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isAnimal():
                                # Si hay un animal dentro de ahi, en ese caso que lo vaya a acariciar :)
                                self.accionarObjeto(self.isla.getMapaMovible()[y][x])

                                return True

        return False

    def getBusqueda(self):
        return self.busqueda

    def sumarBusqueda(self):
        self.busqueda += 1
        if self.busqueda == 5:
            self.busqueda = 0

        self.accionar = [False, 0, 0]
        self.moves.clear()

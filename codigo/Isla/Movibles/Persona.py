import math

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
        self.accionar = [False, None]
        self.trabajando = False
        self.tiempoTrabajando = 0
        self.herramienta = None
        self.vision = 4
        self.busqueda = 0
        self.busquedas = [None, self.buscarArboles, self.buscarPiedras, self.buscarAnimales, self.buscarArbustos]
        self.hambre = 100
        self.vida = 70
        self.tiempoMovimiento = 1
        self.puedeTrabajar = True

    def toJson(self):
        jsonText = {
            'objeto': 'Persona',
            'name': self.nombre,
            'edad': self.edad,
            'hambre': self.hambre,
            'vida': self.vida,
            'x': self.x,
            'y': self.y,
            'inventario': [],
            'herramienta': self.herramienta
        }

        for objeto in self.inventario:
            jsonText['inventario'].append(objeto.toJson())

        return jsonText

    def setHerramienta(self, numInventario):
        self.herramienta = numInventario

    def getHerramienta(self):
        return self.inventario[self.herramienta]

    def getPuedeTrabajar(self):
        return self.puedeTrabajar

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
            info.append(UIObject(textObject, 500, 70 + forI * 40))
            forI += 1

        image = Helper.getImage(self.getImage(), 200, 200)
        info.append(UIObject(image, 200, 200))

        for y in range(10):
            for x in range(8):
                fondoObjeto = Helper.getImage(Helper.INVENTARIO, 40, 40)
                info.append(UIObject(fondoObjeto, 500 + 40 * x, 120 + 40 * y))

        fondoHambre = Helper.getSurface(200, 15)
        fondoHambre.fill((102, 51, 0), None, 0)
        info.append(UIObject(fondoHambre, 200, 450))

        rellenoHambre = Helper.getSurface(180, 5)
        rellenoHambre.fill((128, 64, 0), None, 0)
        info.append(UIObject(rellenoHambre, 210, 455))

        hambre = Helper.getSurface(self.hambre * 1.8, 5)
        hambre.fill((250, 128, 114), None, 0)
        info.append(UIObject(hambre, 210, 455))

        fuente = Helper.FUENTE(14)
        textoHambre = fuente.render("Hambre :", True, (255, 255, 255), None)
        info.append(UIObject(textoHambre, 130, 447))

        fondoVida = Helper.getSurface(200, 15)
        fondoVida.fill((102, 51, 0), None, 0)
        info.append(UIObject(fondoVida, 200, 420))

        rellenoVida = Helper.getSurface(180, 5)
        rellenoVida.fill((128, 64, 0), None, 0)
        info.append(UIObject(rellenoVida, 210, 425))

        vida = Helper.getSurface(self.vida * 1.8, 5)
        vida.fill((0, 187, 45), None, 0)
        info.append(UIObject(vida, 210, 425))

        textoVida = fuente.render("Vida :", True, (255, 255, 255), None)
        info.append(UIObject(textoVida, 140, 417))

        forPosX = 0
        forPosY = 0
        for objeto in self.inventario:
            # Dibujan los objetos del inventario

            imagenObjeto = Helper.getImage(objeto.getImage(), 30, 30)
            info.append(UIObject(imagenObjeto, 500 + 40 * forPosX + 5, 120 + 40 * forPosY + 5))

            if forPosX == 7:
                forPosX = 0
                forPosY += 1

            else:

                forPosX += 1

        fondoHerramienta = Helper.getImage(Helper.INVENTARIO, 60, 60)
        info.append(UIObject(fondoHerramienta, 150, 100))

        if not self.herramienta is None:
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

    def accionarObjeto(self, objeto):
        if not self.trabajando:
            self.moveToPosition(objeto.getX(), objeto.getY())
            self.accionar = [True, objeto]

    def isTrabajando(self):
        return self.trabajando

    def hasMoves(self):
        return len(self.moves) > 0

    def debeAccionar(self):
        if self.accionar[0]:
            if self.tieneAlLado(self.accionar[1].getX(), self.accionar[1].getY()):
                self.definirTrabajo(self.accionar[1])

            elif len(self.moves) == 1:
                if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    self.accionarObjeto(self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()])

                else:
                    self.accionarObjeto(self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()])

    def esquivarObjeto(self):
        if self.moves[len(self.moves) - 1][0] == 0:
            if self.directionX > 0:
                self.moves.append([1, 0])
                self.moves.insert(0, [-1, 0])

            else:
                self.moves.append([-1, 0])
                self.moves.insert(0, [1, 0])

        else:

            if self.directionY > 0:
                self.moves.append([0, 1])
                self.moves.insert(0, [0, -1])

            else:
                self.moves.append([0, -1])
                self.moves.insert(0, [0, 1])

    def makeMoves(self):
        if not self.isTrabajando():
            self.setImage(Helper.PERSONA)
            if self.hasMoves():
                if not self.isla.getMapaObjetos()[self.y][self.x] is None:
                    if self.tiempoMovimiento == self.isla.getMapaObjetos()[self.y][self.x].getVelocidad():
                        self.debeAccionar()

                        if self.move(self.moves[len(self.moves) - 1][0], self.moves[len(self.moves) - 1][1]):
                            self.moves.pop(len(self.moves) - 1)

                        else:
                            self.esquivarObjeto()

                        self.descubrir()

                        self.tiempoMovimiento = 1

                    else:
                        self.tiempoMovimiento += 1

                else:
                    self.debeAccionar()

                    if self.move(self.moves[len(self.moves) - 1][0], self.moves[len(self.moves) - 1][1]):
                        self.moves.pop(len(self.moves) - 1)

                    else:
                        self.esquivarObjeto()

                    self.descubrir()


            else:
                if not self.getTarea() is None:
                    if not self.accionar[0]:
                        if not self.tieneInventarioLleno():
                            self.buscarRecursos()

                        else:
                            self.guardarRecursos()

                        if self.tieneHambre() and self.getAldea().tieneComida():
                            self.guardarRecursos()

        else:
            self.trabajar()


    def getTarea(self):
        return self.busquedas[self.busqueda]

    def buscarRecursos(self):
        if not self.getTarea()():
            self.agregarMovimientos(5)

    def guardarRecursos(self):
        self.accionarObjeto(self.getCasa())

    def tieneInventarioLleno(self):
        return len(self.inventario) >= 80

    def tieneHambre(self):
        return self.hambre <= 20

    def getTarea(self):
        return self.busquedas[self.busqueda]

    def guardarRecursos(self):
        self.accionarObjeto(self.getCasa())

    def tieneInventarioLleno(self):
        return len(self.inventario) >= 80

    def definirTrabajo(self, objeto):
        if not self.herramienta is None:
            herramienta = self.getHerramienta()

        else:
            herramienta = Mano()

        # Si esta trabajando que le modifiquen la imagen
        if objeto.isCasa():
            if self.tieneAlgoEnElInventario():
                self.trabajando = True
                self.tiempoTrabajando = len(self.inventario)
                self.setImage(Helper.PERSONA_TRABAJANDO)

            if self.hambre < 100:
                self.trabajando = True
                if self.tieneAlgoEnElInventario():
                    self.tiempoTrabajando += math.ceil((100 - self.hambre) / 10)

                else:
                    self.tiempoTrabajando = math.ceil((100 - self.hambre) / 10)

                self.setImage(Helper.PERSONA_TRABAJANDO)



        elif not objeto.getTrabajo(herramienta) == 0:
            self.trabajando = True
            self.tiempoTrabajando = objeto.getTrabajo(herramienta)

            self.setImage(Helper.PERSONA_TRABAJANDO)

    def trabajar(self):
        if self.puedeTrabajar:
            if not self.herramienta is None:
                herramienta = self.herramienta

            else:
                herramienta = Mano()

            # En el caso que este trabajando
            if self.trabajando:
                # Si esta trabajando, que le reste un poco de tiempo de trabajo,
                self.tiempoTrabajando -= 1

                objetoTrabajado = self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()]

                movibleTrabajado = self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()]

                if not objetoTrabajado is None:
                    if objetoTrabajado.isCasa():
                        # Si esta "trabajando" en la aldea, que guarde su inventario en la aldea
                        if self.tieneAlgoEnElInventario():
                            if objetoTrabajado.getAldea().anadirObjeto(self.inventario[len(self.inventario) - 1]):
                                self.inventario.pop(len(self.inventario) - 1)

                        elif self.hambre < 100 and objetoTrabajado.getAldea().tieneComida():
                            objetoTrabajado.getAldea().conseguirComida()
                            self.sumarHambre(10)

                if self.tiempoTrabajando == 0:
                    # Si termino de trabajar

                    self.trabajando = False
                    self.setImage(Helper.PERSONA)

                    if not objetoTrabajado is None:
                        valor = objetoTrabajado.getValor()
                        if not valor is None:
                            for objeto in valor:
                                # Si era un objeto en el que estaba trabajando, que agregue sus items en el inventario

                                self.agregarInventario(objeto)

                            self.getAldea().sumarInteligencia(5)
                            self.restarHambre(10)

                        objetoTrabajado.onClick(herramienta)

                    elif not movibleTrabajado is None:

                        valor = movibleTrabajado.getValor()
                        # Si era un movible en el que estaba trabajando, que agregue sus valores en el inventario
                        if not valor is None:
                            for objeto in valor:
                                self.agregarInventario(objeto)

                            self.getAldea().sumarInteligencia(10)
                            self.restarHambre(10)

                        else:

                            movibleTrabajado.onClick(herramienta)

                    self.accionar[0] = False
                    self.moves.clear()
        else:
            return

    def tieneAlgoEnElInventario(self):
        return len(self.inventario) > 0

    def buscarArboles(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbol():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarPiedras(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isPiedra():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarArbustos(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbusto():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarAnimales(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isAnimal():
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

        return False

    def buscarAnimales(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isAnimal():
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

    def restarHambre(self, hambre):
        self.hambre -= hambre
        if self.hambre < 1:
            self.restarVida(hambre)
            self.hambre = 1

    def sumarVida(self, vida):
        self.vida += vida
        if self.vida > 100:
            self.vida = 100

    def cicloVida(self):
        if self.hambre > 70:
            self.sumarVida(10)

        self.restarHambre(5)

    def buscarArboles(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbol():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarPiedras(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isPiedra():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarArbustos(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaObjetos()[y][x] is None:
                            if self.isla.getMapaObjetos()[y][x].isArbusto():
                                self.accionarObjeto(self.isla.getMapaObjetos()[y][x])

                                return True

        return False

    def buscarAnimales(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            for x in range(self.x - self.vision, self.x + self.vision):
                if not x > self.isla.getAncho() or not x < self.isla.getAncho():
                    if not y > self.isla.getAltura() or not y < self.isla.getAltura():
                        if not self.isla.getMapaMovible()[y][x] is None:
                            if self.isla.getMapaMovible()[y][x].isAnimal():
                                self.accionarObjeto(self.isla.getMapaMovible()[y][x])

                                return True

        return False

    def getBusqueda(self):
        return self.busqueda

    def sumarBusqueda(self):
        if not self.trabajando:
            self.busqueda += 1
            if self.busqueda == 5:
                self.busqueda = 0

            self.accionar = [False, 0, 0]
            self.moves.clear()

    def getHambre(self):
        return self.hambre

    def setHambre(self, hambre):
        self.hambre = hambre

    def cicloVida(self):
        self.restarHambre(1)

    def descubrir(self):
        for y in range(self.y - self.vision, self.y + self.vision):
            if y > 0 and y < self.isla.getAltura():
                for x in range(self.x - self.vision, self.x + self.vision):
                    if x > 0 and x < self.isla.getAncho():
                        if not self.isla.getMapaEstatico()[y][x].getVisibilidad():
                            self.isla.getMapaEstatico()[y][x].setVisivilidad(True)

    def restarVida(self, vida):
        self.vida -= vida
        if self.vida <= 0:
            self.muerto = True

    def setVida(self, vida):
        self.vida = vida

    def getVida(self):
        return self.vida

    def sumarHambre(self, hambre):
        self.hambre += hambre
        if self.hambre > 100:
            self.hambre = 100

    def dañar(self,daño):
        self.restarVida(daño)
        self.setImage(Helper.PERSONA_DAÑADA)


    def isPersona(self):
        return True

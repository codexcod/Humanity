import pygame
import os
from codigo.Isla.Helper import Helper
from codigo.Menu.Partida import Partida
from codigo.Menu.Button import Button
from codigo.Menu.popUp import PopUp
from codigo.Controlador import Controlador
from codigo.Isla.Isla import Isla
from codigo.Camara.Zoom import Zoom
from codigo.Camara.UI.UI import UI
from codigo.Camara.Camara import Camara
from codigo.Camara.Mouse import Mouse
from codigo.MenuControlador import ControladorMenu
from os import remove


class CargarPartidaControlador:

    def __init__(self):
        self.ancho = 640
        self.alto = 480
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.clock = pygame.time.Clock()
        self.partidas = []
        self.nuevasPartidas = 0
        self.partida = None

    def degradado(self):
        # Pantalla para el FADE de cambio de pantalla
        pantallaNegra = pygame.Surface((self.ancho, self.alto))
        pantallaNegra.fill((0, 0, 0))
        # Cambia rapidamente entre la pantalla y la pantalla negra cada vez mas lento
        # hasta quedar todo negro
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            self.dibujarMenu()
            self.screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    def conseguirPartidas(self):
        slotsPartidas = 3
        # Meter los archivos de "Info" en "archivos"
        archivos = os.listdir("Info")
        # Buscar las partidas que hay
        for partida in archivos:
            partes = partida.split(".")
            self.partidas.append(partes[0])

        # Definir los slots vacios de partidas
        self.nuevasPartidas = slotsPartidas
        for partida in self.partidas:
            self.nuevasPartidas -= 1

    def crearObjetos(self):
        self.botonesIniciar = []
        self.botonesNew = []
        self.botonesBorrar = []
        self.botones = []
        i = 0
        for partida in self.partidas:
            i += 1
            # Por cada partida que haya crear sus respectivos botones iniciar y borrar
            self.botonesIniciar.append(
                Partida((self.ancho - 150, (i * 155)), 20, "  Elegir Isla  ", self.screen, "white", "black", "brown",
                        partida))
            self.botonesBorrar.append(
                Partida((self.ancho - 10, (i * 155)), 20, "  Borrar Isla  ", self.screen, "white", "black", "brown",
                        partida))

        # Por cada slot de partida vacio crear un boton "Nueva Partida"
        for i in range(3 - self.nuevasPartidas + 1, 3 + 1):
            self.botonesNew.append(
                Button((self.ancho - 10, (i * 155)), 20, "Nueva Partida", self.screen, "white", "black", "brown"))

        # Ordenar los tipos de botones en una lista para que sean mas faciles de dibujar
        self.botones = [self.botonesIniciar, self.botonesBorrar, self.botonesNew]

        # Crear el cuadro de la advertencia de Borrar
        self.advertencia = PopUp(self.ancho, self.alto)

        # Crear los botones para la advertencia de Borrar
        self.botonAceptar = Button((self.ancho / 2, self.alto / 2 + 45), 24, "   Si   ", self.screen, "black", "black",
                                   "grey")
        self.botonRechazar = Button((self.ancho / 2 + 85, self.alto / 2 + 45), 24, "   No   ", self.screen, "black",
                                    "black", "grey")

        # Crear los recuadros para las islas
        self.recuadrosIslas = []
        for i in range(0, 3):
            self.recuadrosIslas.append(pygame.Rect((10, 10 + (155 * i)), (self.ancho - 20, 150)))

    def dibujarMenu(self):
        orange = (210, 137, 8)

        # Tiempo para fondo
        timerFondo = 5
        pygame.time.set_timer(timerFondo, 1000)

        for recuadro in self.recuadrosIslas:
            pygame.draw.rect(self.screen, orange, recuadro)

        nombrePartida = []
        for partida in self.partidas:
            nombrePartida.append(Helper.FUENTE(30).render(partida, True, "black"))

        for i in range(self.nuevasPartidas):
            nombrePartida.append(Helper.FUENTE(30).render("No hay partida creada", True, "black"))

        i = 0
        # Dibujar los nombres de las partidas
        for nombre in nombrePartida:
            self.screen.blit(nombre, (20, 50 + (i * 155) + 10))
            i += 1

        # Dibujar los botones de cada tipo
        for listas in self.botones:
            for boton in listas:
                boton.dibujarBoton(1)

        # Dibujar la advertencia si se clickeo borrar
        if self.confirmarBor == True:
            popArriba = "Seguro que desea eliminar"
            popAbajo = "Esta isla"
            popPosArriba = (self.ancho / 2 - 90, self.alto / 2 - 40)
            popPosAbajo = (self.ancho / 2 - 30, self.alto / 2 - 20)
            self.advertencia.dibujarCuadro(popArriba, popAbajo, self.screen, popPosArriba, popPosAbajo)
            self.botonAceptar.dibujarBoton(1)
            self.botonRechazar.dibujarBoton(1)

    def run(self):
        self.confirmarBor = False
        islas = True
        self.conseguirPartidas()
        self.crearObjetos()
        while islas:
            for event in pygame.event.get():
                # Salir
                if event.type == pygame.QUIT:
                    islas = False

            # Por cada boton "Iniciar" checkear si clickean en el
            if self.confirmarBor == False:
                for boton in self.botonesIniciar:
                    if boton.click(event):
                        # Iniciar la partida asociada al boton
                        self.degradado()
                        isla = Isla()
                        isla.cargarMapa(boton.getPartida())
                        ancho = isla.getAncho()
                        altura = isla.getAltura()
                        aldea = isla.getAldea()

                        # Camara para controlar el zoom
                        camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
                        mouse = Mouse(camara)

                        controlador = Controlador(isla, camara, boton.getPartida())
                        controlador.run()
                        islas = False

            # Por cada boton "Borrar" checkear si clickean en el
            for boton in self.botonesBorrar:
                if boton.click(event):
                    # se debera llamar a la advertencia
                    self.confirmarBor = True
                    # Crear un holder para la info de ese boton
                    botonHolder = boton

            if self.botonAceptar.click(event):
                self.confirmarBor = False
                botonHolder.setBorrar(True)

            if self.botonRechazar.click(event):
                self.confirmarBor = False

            # Por cada boton "Nueva partida" checkear si clickean en el
            if not self.confirmarBor:
                for boton in self.botonesNew:
                    if boton.click(event):
                        # salir de esta pantalla e ir al menu de creacion
                        self.degradado()
                        islas = False
                        controladorMenu = ControladorMenu()
                        controladorMenu.run()

            try:
                # Si se confirma que se quiere borrar borrara
                if botonHolder.getBorrar() == True:
                    remove(f'info/{botonHolder.getPartida()}.json')

                    islas = False
                    return True




            except:
                pass

            # Dibujar todo
            self.clock.tick(60)
            self.screen.fill("black")
            self.dibujarMenu()
            pygame.display.update()

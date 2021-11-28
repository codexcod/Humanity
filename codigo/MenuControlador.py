import pygame
from codigo.Isla.Helper import Helper
from codigo.Menu.InputBox import InputBox
from codigo.Menu.fondo import Fondo
from codigo.Menu.Button import Button
from codigo.Menu.popUp import PopUp
from codigo.Isla.Isla import Isla
from codigo.Isla.Aldea import Aldea
from codigo.Camara.UI.UI import UI
from codigo.Controlador import Controlador
from codigo.Camara.Zoom import Zoom
from codigo.Camara.Camara import Camara
from codigo.Camara.Mouse import Mouse


class ControladorMenu:

    def __init__(self):
        self.ancho = 640
        self.alto = 480
        self.screen = pygame.display.set_mode((self.ancho, self.alto))

    def crearObjetos(self):
        ancho = self.getAncho()
        alto = self.getAlto()
        screen = self.getScreen()
        # Creacion de input boxes
        self.input_box1 = InputBox(100, 100, 100, 32, "Nombre de aldea")
        self.input_box2 = InputBox(100, 200, 100, 32, "Heroe")
        self.input_box3 = InputBox(100, 300, 100, 32, "Explorador")
        self.input_box4 = InputBox(100, 400, 100, 32, "Partida")
        self.input_boxes = [self.input_box1, self.input_box2, self.input_box3, self.input_box4]

        # Creacion de botones
        self.botonEmpezar = Button((ancho, alto), 30, "Empezar", screen, "black", "black", (62, 62, 62))
        self.botonMusicaOn = Button((ancho, 40), 24, "On", screen, "black", (Helper.COLORACTIVO), "green")
        self.botonMusicaOff = Button((ancho - 30, 40), 24, "Off", screen, "black", (Helper.COLORACTIVO), (12, 109, 0))
        self.botones = [self.botonEmpezar, self.botonMusicaOn, self.botonMusicaOff]

        # Boton de error
        self.botonAceptar = Button((ancho / 2 + 45, alto / 2 + 45), 24, "Aceptar", self.getScreen(), "black", "black",
                                   "grey")

        self.popUp = PopUp(ancho, alto)
        self.fondo = Fondo(ancho, alto)

    def dibujarMenu(self):

        """ Dibuja el menu """

        screen = self.getScreen()

        screen.blit(self.fondo.getfirstImage(), (0, 0))
        screen.blit(self.fondo.getSecondImage(), (0, 0))
        for box in self.input_boxes:
            box.dibujarCaja(screen)
        for boton in self.botones:
            boton.dibujarBoton(3)

    def dibujarError(self, botonAceptar, popUp):

        """ Dibuja un popUp de error """
        ancho = self.getAncho()
        alto = self.getAlto()

        popArriba = "Debe completar todos los campos "
        popAbajo = "Pulsa el boton aceptar para continuar"
        popPosArriba = (ancho / 2 - 128, alto / 2 - 40)
        popPosAbajo = (ancho / 2 - 128, alto / 2 - 20)
        popUp.dibujarCuadro(popArriba, popAbajo, self.getScreen(), popPosArriba, popPosAbajo)
        botonAceptar.dibujarBoton(2)

    def getAlto(self):
        return self.alto

    def getAncho(self):
        return self.ancho

    def getScreen(self):
        return self.screen

    def getInputBoxes(self):
        return self.input_boxes

    def degradado(self):
        """ Fade out visual para el cambio de pantalla """
        screen = self.getScreen()
        pantallaNegra = pygame.Surface((self.getAncho(), self.getAlto()))
        pantallaNegra.fill((0, 0, 0))
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            self.dibujarMenu()
            screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    def run(self):
        self.crearObjetos()
        alto = self.getAlto
        ancho = self.getAncho()
        Helper.playMusic('menu', 0.5)
        fondo = self.fondo
        menu = True
        clock = pygame.time.Clock()
        error = False
        timerFondo = 4
        pygame.time.set_timer(timerFondo, 1000)

        while menu:
            for event in pygame.event.get():

                # Salir
                if event.type == pygame.QUIT:
                    menu = False

                # Funcionamiento de los inputs llamando a un evento interno
                for box in self.getInputBoxes():
                    box.InputEventos(event, self.getScreen())

                if event.type == timerFondo:
                    fondo.cambiarAnimacion()

                    # Hacer que los inputs se hagan mas grandes
            for box in self.getInputBoxes():
                box.update(ancho)

            # Dibujar todo
            pygame.display.update()
            clock.tick(60)

            self.dibujarMenu()
            if error:
                self.dibujarError(self.botonAceptar, self.popUp)

            if self.botonAceptar.click(event):
                error = False
                # Musica
            if self.botonMusicaOn.click(event):
                if Helper.pauseMusic():
                    self.botonMusicaOn.setcolorFondo("green")
                    self.botonMusicaOff.setcolorFondo((12, 109, 0))
                    Helper.unpauseMusic()
            if self.botonMusicaOff.click(event):
                if Helper.pauseMusic():
                    self.botonMusicaOff.setcolorFondo("green")
                    self.botonMusicaOn.setcolorFondo((12, 109, 0))
                    Helper.pauseMusic()

            # al clickear boton empezar
            if self.botonEmpezar.click(event):
                aldea = self.input_box1.getText()
                heroe = self.input_box2.getText()
                explorador = self.input_box3.getText()
                partida = self.input_box4.getText()
                self.botonEmpezar.setRecuadro(Helper.COLORACTIVO)

                # dato1 = aldea/ dato2 = heroe/ dato3 = explorador/ dato4 = partida 
                if aldea == "" or heroe == "" or explorador == "" or partida == "":
                    error = True
                    self.botonEmpezar.setRecuadro("black")
                else:
                    if not error:
                        ancho = 400
                        alto = 400
                        Helper.fadeMusic(3000)
                        self.degradado()
                        # dato1 = aldea/ dato2 = heroe/ dato3 = explorador/ dato4 = partida 
                        isla = Isla()
                        isla.generarIsla(ancho, alto)
                        isla.setNombre(partida)
                        aldea = Aldea(aldea)
                        isla.agregarAldea(aldea, ancho // 2, alto // 2, heroe, explorador)

                        # Camara para controlar el zoom
                        camara = Camara(ancho // 2, alto // 2, isla, Zoom.NORMAL_ZOOM, UI())
                        mouse = Mouse(camara)

                        controlador = Controlador(isla, camara, partida)
                        controlador.run()

                        menu = False

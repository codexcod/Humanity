import pygame
from codigo.Isla.Helper import Helper
from codigo.Menu.InputBox import InputBox
from codigo.Menu.fondo import Fondo
from codigo.Menu.buttom import Boton
from codigo.Menu.popUp import PopUp
from codigo.Menu.Partida import Partida


class ControladorMenu():

    def __init__(self):
        self.ancho: 640
        self.alto: 480
        self.screen
        self.screen = pygame.display.set_mode((self.ancho, self.alto))


    def crearObjetos(self):
        # Creacion de input boxes
        input_box1 = InputBox(100, 100, 100, 32, "Nombre de aldea")
        input_box2 = InputBox(100, 200, 100, 32, "Heroe")
        input_box3 = InputBox(100, 300, 100, 32, "Explorador")
        input_box4 = InputBox(100, 400, 100, 32, "Partida")
        self.input_boxes = [input_box1, input_box2, input_box3, input_box4]

        # Creacion de botones
        self.botonEmpezar = Buttom((ancho, alto), 30, "Empezar", screen, "black", "black", (62, 62, 62))
        self.botonMusicaOn = Buttom((ancho, 40), 24, "On", screen, "black", (Helper.COLORACTIVO), "green")
        self.botonMusicaOff = Buttom((ancho - 30, 40), 24, "Off", screen, "black", (Helper.COLORACTIVO), (12, 109, 0))
        self.botones = [self.botonEmpezar, self.botonMusicaOn, self.botonMusicaOff]

        # Boton de error
        self.botonAceptar = Buttom((ancho / 2 + 45, alto / 2 + 45), 24, "Aceptar", self.getScreen(), "black", "black", "grey")

        self.popUp = PopUp(ancho, alto)
        self.fondo = Fondo(ancho, alto)

        



    def dibujarMenu(self, input_boxes, botones, fondo):
        
        """ Dibuja el menu """
        ancho = self.getAncho()
        alto = self.getAlto()
        screen = self.getScreen()

        screen.blit(fondo.getfirstImage(), (0, 0))
        screen.blit(fondo.getSecondImage(), (0, 0))
        for box in input_boxes:
            box.dibujarCaja(screen)
        for boton in botones:
            boton.dibujarBoton(3)
    




    def dibujarError(self, botonAceptar, popUp): 

        """ Dibuja un popUp de error """
        ancho = self.getAncho()
        alto = self.getAlto()

        popArriba = "Debe completar todos los campos "
        popAbajo = "Pulsa el boton aceptar para continuar"
        popPosArriba = (ancho/ 2 - 128, alto/ 2 - 40)
        popPosAbajo = (ancho/ 2 - 128, alto/ 2 - 20)
        popUp.dibujarCuadro(popArriba, popAbajo, self.getScreen(), popPosArriba, popPosAbajo)
        botonAceptar.dibujarBoton(2)



    def getAlto():
        return self.alto
    
    def getAncho():
        return self.ancho

    def getScreen():
        return self.screen

    def getInputBoxes():
        return self.input_boxes

    def degradado(self, self.input_boxes, self.botones, self.fondo):
        """ Fade out visual para el cambio de pantalla """
        pantallaNegra = pygame.Surface((self.getAncho(), self.getAlto()))
        pantallaNegra.fill((0, 0, 0))
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            dibujarMenu(self.input_boxes, self.botones, self.fondo)
            screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)


    
    def run(self):
        Helper.playMusic('menu', 0.5)
        reproducirMusica = True
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
                    box.InputEventos(event, screen)

                if event.type == timerFondo:
                    fondo.cambiarAnimacion()

                    # Hacer que los inputs se hagan mas grandes
            for box in self.getInputBoxes():
                box.update(ancho)

            # Dibujar todo
            pygame.display.update()
            clock.tick(60)

            dibujarMenu(self.input_boxes, self.botones, self.fondo)
            if error:
                self.dibujarError(self.botonAceptar, self.popUp)

            if botonAceptar.click(event):
                error = False
                # Musica
            if botonMusicaOn.click(event):
                if Helper.pauseMusic():
                    self.botonMusicaOn.setcolorFondo("green")
                    self.botonMusicaOff.setcolorFondo((12, 109, 0))
                    Helper.unpauseMusic()
            if botonMusicaOff.click(event):
                if Helper.pauseMusic():
                    self.botonMusicaOff.setcolorFondo("green")
                    self.botonMusicaOn.setcolorFondo((12, 109, 0))
                    Helper.pauseMusic()

            # al clickear boton empezar
            if botonEmpezar.click(event):
                x = 1
                for box in self.getInputBoxes():
                    dato{x} = box.getText()
                    x += 1

                botonEmpezar.setRecuadro(Helper.COLORACTIVO)

                # dato1 = aldea/ dato2 = heroe/ dato3 = explorador/ dato4 = partida 
                if dato1 == "" or dato2 == "" or dato3 == "" or dato4 == "":
                    error = True
                    botonEmpezar.setRecuadro("black")
                else:
                    if error == False:
                        Helper.fadeMusic(3000)
                        self.degradado(self.input_boxes, self.botones, self.fondo)
                        # dato1 = aldea/ dato2 = heroe/ dato3 = explorador/ dato4 = partida 
                        Juego(dato1, dato2, dato3,  dato4)
                        menu = False
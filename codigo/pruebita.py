import sys
from typing import Text

# Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH
from codigo.Controlador import Controlador

path = sys.path[0]
sys.path.append(path[:len(path) - 7])

import pygame
import time
from pygame import mixer
from codigo.Isla.Isla import Isla
from codigo.Camara.Camara import Camara
from codigo.Camara.UI.UI import UI
from codigo.Camara.Zoom import Zoom
from codigo.Camara.Mouse import Mouse
from codigo.Menu.InputBox import InputBox
from codigo.Menu.fondo import Fondo
from codigo.Menu.buttom import Boton
from codigo.Menu.popUp import PopUp
from codigo.Isla.Helper import Helper
from codigo.Isla.Aldea import Aldea
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.Objetos.Casa import Casa

pygame.init()
mixer.init()


def Juego(nombreAldea, heroe, explorador, partida):
    ancho = 400
    altura = 400
    isla = Isla()
    isla.generarIsla(ancho, altura)
    aldea = Aldea(nombreAldea)
    isla.agregarAldea(aldea, ancho // 2, altura // 2, heroe, explorador)

    # Camara para controlar el zoom
    camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)

    controlador = Controlador(isla, camara, partida)
    controlador.run()


def cargarJuego(partida):
    isla = Isla()
    isla.cargarMapa(partida)
    ancho = isla.getAncho()
    altura = isla.getAltura()
    aldea = isla.getAldea()

    # Camara para controlar el zoom
    camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)

    controlador = Controlador(isla, camara, partida)
    controlador.run()


def menu():
    ancho = 640
    alto = 480
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()

    # Pantalla para el degradado
    pantallaNegra = pygame.Surface((ancho, alto))
    pantallaNegra.fill((0, 0, 0))

    # Creacion de input boxes
    input_box1 = InputBox(100, 100, 100, 32, "Nombre de aldea")
    input_box2 = InputBox(100, 200, 100, 32, "Heroe")
    input_box3 = InputBox(100, 300, 100, 32, "Explorador")
    input_box4 = InputBox(100, 400, 100, 32, "Partida")
    input_boxes = [input_box1, input_box2, input_box3, input_box4]

    # Crear objeto boton
    # ((posx,posy)),fuente,texto,screen,colordeletra, color de recuadro,colordefondo
    botonEmpezar = Boton((ancho, alto), 30, "Empezar", screen, "black", "black", (62, 62, 62))
    botonAceptar = Boton((ancho / 2 + 45, alto / 2 + 45), 24, "Aceptar", screen, "black", "black", "grey")
    botonMusicaOn = Boton((ancho, 40), 24, "On", screen, "black", (Helper.COLORACTIVO), "green")
    botonMusicaOff = Boton((ancho - 30, 40), 24, "Off", screen, "black", (Helper.COLORACTIVO), (12, 109, 0))

    Menu = True
    error = False
    popUp = PopUp(ancho, alto)
    music = 'menu'
    fondo = Fondo(ancho, alto)
    reproducirMusica = True

    # Dibujar
    def dibujarMenu(error):
        screen.blit(fondo.getfirstImage(), (0, 0))
        screen.blit(fondo.getSecondImage(), (0, 0))
        for box in input_boxes:
            box.dibujarCaja(screen)
        botonEmpezar.dibujarBoton(3)
        botonMusicaOn.dibujarBoton(3)
        botonMusicaOff.dibujarBoton(3)

        if error == True:
            popArriba = "Debe completar todos los campos "
            popAbajo = "Pulsa el boton aceptar para continuar"

            popUp.dibujarCuadro(popArriba, popAbajo, screen)
            botonAceptar.dibujarBoton(2)

    # Fade out visual
    def degradado():
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            dibujarMenu(error)
            screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    # Poner musica
    Helper.playMusic(music, 0.5)

    # Tiempo para fondo
    timerFondo = 4
    pygame.time.set_timer(timerFondo, 1000)

    # Cerrar
    while Menu:

        for event in pygame.event.get():

            # Salir
            if event.type == pygame.QUIT:
                Menu = False

            # Funcionamiento de los inputs llamando a un evento interno
            for box in input_boxes:
                box.InputEventos(event, screen)

            if event.type == timerFondo:
                fondo.cambiarAnimacion()

                # Hacer que los inputs se hagan mas grandes
        for box in input_boxes:
            box.update(ancho)

        # Dibujar todo
        pygame.display.update()
        clock.tick(60)
        dibujarMenu(error)

        if botonAceptar.click(event):
            error = False
            # Musica
        if botonMusicaOn.click(event):
            if Helper.pauseMusic():
                botonMusicaOn.setcolorFondo("green")
                botonMusicaOff.setcolorFondo((12, 109, 0))
                Helper.unpauseMusic()
        if botonMusicaOff.click(event):
            if Helper.pauseMusic():
                botonMusicaOff.setcolorFondo("green")
                botonMusicaOn.setcolorFondo((12, 109, 0))
                Helper.pauseMusic()

        # al clickear boton empezar
        if botonEmpezar.click(event):
            aldea = input_box1.getText()
            heroe = input_box2.getText()
            explorador = input_box3.getText()
            partida = input_box4.getText()
            botonEmpezar.setRecuadro(Helper.COLORACTIVO)

            if aldea == "" or heroe == "" or explorador == "" or partida == "":
                error = True
                botonEmpezar.setRecuadro("black")
            else:
                if error == False:
                    Helper.fadeMusic(3000)
                    degradado()
                    Juego(aldea, heroe, explorador,  partida)
                    Menu = False


def Islasini():
    ancho = 640
    alto = 480
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    brown = (112,140,104)
    #Crear objeto boton
    #((posx,posy)),fuente,texto,screen,colordeletra, color de recuadro,colordefondo
    Iniciar1 = Boton((ancho-120,155),20,"  Elegir Isla  ",screen,"white","black","brown")
    Borrar1 = Boton((ancho-10,155),20,"  Borrar Isla  ",screen,"white","black","brown")
    Menu = True


    #Tiempo para fondo
    timerFondo = 4
    pygame.time.set_timer(timerFondo,1000)
    #Dibujar fondo
        
    cuadro = Helper.CUADRO
    cuadro = pygame.transform.scale(cuadro, (ancho,150))

    recuadroIsla = pygame.Rect((10, 10), (ancho- 20, 150))
    recuadroIsla1 = pygame.Rect((10, 165), (ancho- 20, 150))
    recuadroIsla2 = pygame.Rect((10, 320), (ancho- 20, 150))
    
   
    
    while Menu:

        for event in pygame.event.get():
            # Salir
            if event.type == pygame.QUIT:
                Menu = False

        # Dibujar todo
        pygame.display.update()
        clock.tick(60)     
        screen.fill("black")
        
        pygame.draw.rect(screen, brown, recuadroIsla)
        pygame.draw.rect(screen, brown, recuadroIsla1)
        pygame.draw.rect(screen, brown, recuadroIsla2)
        # screen.blit(cuadro,(10,10))
        # screen.blit(cuadro,(10, 165))
        # screen.blit(cuadro,(10, 320))
        Iniciar1.dibujarBoton(1)
        Borrar1.dibujarBoton(1)        
        
            
Islasini()

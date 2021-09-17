import sys
from typing import Text

# Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH


path = sys.path[0]
sys.path.append(path[:len(path) - 7])

import pygame
import time
import os
from os import remove
from pygame import mixer
from codigo.Controlador import Controlador
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
from codigo.Menu.Partida import Partida

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
            popPosArriba = (ancho/ 2 - 128, alto/ 2 - 40)
            popPosAbajo = (ancho/ 2 - 128, alto/ 2 - 20)
            popUp.dibujarCuadro(popArriba, popAbajo, screen, popPosArriba, popPosAbajo)
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
    confirmarBor = False
    islas = True

    #Tiempo para fondo
    timerFondo = 4
    pygame.time.set_timer(timerFondo,1000)


    partida = None
    start= ""
    
    def degradado():
        # Pantalla para el FADE de cambio de pantalla
        pantallaNegra = pygame.Surface((ancho, alto))
        pantallaNegra.fill((0, 0, 0))
        #Cambia rapidamente entre la pantalla y la pantalla negra cada vez mas lento
        #hasta quedar todo negro
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            dibujarMenu()
            screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)


    partidas = []
    slotsPartidas = 3
    #Meter los archivos de "Info" en "archivos"
    archivos = os.listdir("Info")
    #Buscar las partidas que hay
    for partida in archivos:
        partes = partida.split(".")
        partidas.append(partes[0])

    #Definir los slots vacios de partidas
    nuevasPartidas = slotsPartidas
    for partida in partidas:
        nuevasPartidas -= 1


    #Crear los recuadros para las islas
    recuadrosIslas = []
    for i in range(0,3):
        recuadrosIslas.append(pygame.Rect((10, 10 + (155*i)), (ancho- 20, 150)))


    botonesIniciar = []
    botonesNew = []
    botonesBorrar = []
    botones = []
    i = 0
    for partida in partidas:
        i += 1
        #Por cada partida que haya crear sus respectivos botones iniciar y borrar
        botonesIniciar.append(Partida((ancho-150,(i*155)),20,"  Elegir Isla  ",screen,"white","black","brown",partida))
        botonesBorrar.append(Partida((ancho-10,(i*155)),20,"  Borrar Isla  ",screen,"white","black","brown",partida))
    
    #Por cada slot de partida vacio crear un boton "Nueva Partida"
    for i in range(3-nuevasPartidas+1, 3+1):
        botonesNew.append(Boton((ancho-10,(i*155)),20,"Nueva Partida",screen,"white","black","brown"))

    #Ordenar los tipos de botones en una lista para que sean mas faciles de dibujar
    botones = [botonesIniciar , botonesBorrar, botonesNew]

    #Crear el cuadro de la advertencia de Borrar
    advertencia = PopUp(ancho, alto)

    #Crear los botones para la advertencia de Borrar
    botonAceptar = Boton((ancho / 2 , alto / 2 + 45), 24, "   Si   ", screen, "black", "black", "grey")
    botonRechazar = Boton((ancho / 2 + 85 , alto / 2 + 45), 24, "   No   ", screen, "black", "black", "grey")
    

    def dibujarMenu():
        orange = (210,137,8)
        for recuadro in recuadrosIslas:
            pygame.draw.rect(screen, orange, recuadro)

        nombrePartida = []
        for partida in partidas:
            nombrePartida.append(Helper.FUENTE(30).render(partida, True, "black"))

        for i in range(nuevasPartidas):
            nombrePartida.append(Helper.FUENTE(30).render("No hay partida creada", True, "black"))

        i = 0
        #Dibujar los nombres de las partidas
        for nombre in nombrePartida:
            screen.blit(nombre,(20, 50 + (i*155) + 10)) 
            i += 1

        #Dibujar los botones de cada tipo
        for listas in botones:
            for boton in listas:  
                boton.dibujarBoton(1)

        #Dibujar la advertencia si se clickeo borrar
        if confirmarBor == True:
            popArriba = "Seguro que desea eliminar"
            popAbajo = "Esta isla"
            popPosArriba = (ancho/ 2 - 90, alto/ 2 - 40)
            popPosAbajo = (ancho/ 2 - 30, alto/ 2 - 20)
            advertencia.dibujarCuadro(popArriba, popAbajo, screen, popPosArriba, popPosAbajo)
            botonAceptar.dibujarBoton(1)
            botonRechazar.dibujarBoton(1)

                
    while islas:
        for event in pygame.event.get():
            # Salir
            if event.type == pygame.QUIT:
                islas = False


        #Por cada boton "Iniciar" checkear si clickean en el
        if confirmarBor == False:
            for boton in botonesIniciar:      
                if boton.click(event):
                    #Iniciar la partida asociada al boton
                    degradado()
                    cargarJuego(boton.getPartida())
                    islas = False


        #Por cada boton "Borrar" checkear si clickean en el
        for boton in botonesBorrar:
            if boton.click(event):
                #se debera llamar a la advertencia
                confirmarBor = True
                #Crear un holder para la info de ese boton
                botonHolder = boton

        
        if botonAceptar.click(event):
            confirmarBor = False
            botonHolder.setBorrar(True)


        if botonRechazar.click(event):
            confirmarBor = False

        #Por cada boton "Nueva partida" checkear si clickean en el
        if confirmarBor == False:
            for boton in botonesNew:
                if boton.click(event):
                    #salir de esta pantalla e ir al menu de creacion
                    degradado()
                    islas = False
                    menu()


        try:
            #Si se confirma que se quiere borrar borrara
            if botonHolder.getBorrar() == True:
                remove(f'info/{partida}.json')
                islas = False
                Islasini()
        except:
            pass


        # Dibujar todo
        clock.tick(60)     
        screen.fill("black")
        dibujarMenu()   
        pygame.display.update()



Islasini()
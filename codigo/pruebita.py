import sys
from typing import Text

# Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH
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



def Juego(nombreAldea, heroe, explorador, mascota):
    ancho = 400
    altura = 400
    isla = Isla (ancho, altura)
    aldea = Aldea (nombreAldea)
    isla.agregarAldea (aldea, ancho // 2, altura // 2,heroe,explorador,mascota)

    # Camara para controlar el zoom
    camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)
    
    # Controlar tiempo en el juego
    clock = pygame.time.Clock()
    screenUpdate = 1
        # Tiempo para personas
    pygame.time.set_timer(screenUpdate, 250)
        # Tiempo para arboles
    arboles = 2
    pygame.time.set_timer(arboles, 10000)



    running = True
    while running:
        # Checkea todos los eventos
        for event in pygame.event.get():
            #Cerrar juego
            if event.type == pygame.QUIT:
                running = False
            
            # Checkea si algun boton del mouse es presionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    
                    # En el caso que sea el izquierdo se fija si hay UI´s
                    if not camara.getUI().hayUIActivos():
                        if not mouse.seleccionarMovible() is None:

                            camara.getUI().generarInfoObjeto(mouse.seleccionarMovible())

                        elif not mouse.pedirInfoObjeto() is None:
                            camara.getUI().generarInfoObjeto(mouse.pedirInfoObjeto())

                    else:
                        mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())
                        
                # En el caso que sea derecha checkea si esta seleccionado
                if right:
                        # Si esta seleccionado y no es una persona, y trata de seleccionar una persona, la selecciona.
                    if not mouse.seleccionarMovible() is None:
                        if not camara.getSeleccionado() ==  mouse.seleccionarMovible():
                            if mouse.seleccionarMovible() in aldea.getPersonas():
                                camara.setSeleccionado(mouse.seleccionarMovible())

                        else:
                            # Si tiene algo seleccionado y es una persona, la deselecciona
                            camara.setSeleccionado(None)
                    
                    if not camara.getSeleccionado() is None:
                        if  mouse.pedirInfoObjeto() is None:
                            # Si lo seleccionado es una persona, y selecciona al piso, lo mueve al lugar
                            camara.getSeleccionado().moveToPosition(mouse.getObjectMousePosition()[0], mouse.getObjectMousePosition()[1])
                            

                        else:
                            if mouse.seleccionarMovible() is None:
                                # Si selecciona un objeto se fija si no es movible, hacerle algo al objeto
                                camara.getSeleccionado().accionarObjeto(mouse.pedirInfoObjeto())
                                
                            else:
                                # Si selecciona a un movible, desde una persona, se fija de poder hacerle algo al movile
                                if not mouse.seleccionarMovible() in aldea.getPersonas():
                                    camara.getSeleccionado().accionarObjeto(mouse.seleccionarMovible())
                                    
                                

                if event.button == 4:
                    # Baja el zoom
                    camara.getZoom().bajarZoom()

                if event.button == 5:
                    # Aumenta el zoom
                    camara.getZoom().subirZoom()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    camara.moveX(2)

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    camara.moveX(-2)

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    camara.moveY(-2)

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    camara.moveY(2)

                if event.key == pygame.K_z:
                    camara.getZoom().subirZoom()

                if event.key == pygame.K_x:
                    camara.getZoom().bajarZoom()

                if event.key == pygame.K_SPACE: 
                    # Mueve la camara para volver a la aldea
                    camara.setPosY(altura // 2)
                    camara.setPosX(ancho // 2)

            if event.type == screenUpdate:
                # Cuando se actualiza la pantalla, se movera todas las personas y animales
                for persona in aldea.getPersonas():
                    persona.makeMoves()

                for animal in isla.getAnimales():
                    animal.makeMoves()

            if event.type == arboles:
                # Dentro de los arboles talados, se suma el tiempo para que vuelva a crecer
                for arbol in isla.getArbolesTalados():
                    arbol.avanzarTiempo()
            

            
        

        camara.actualizarPantalla()
        camara.getUI().generarAldeaUI(aldea)
        camara.dibujarUI()
        pygame.display.update()

        clock.tick(60)
        # El reloj por el cual todos los eventos se actualizan

def menu():
    ancho = 640
    alto = 480
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()

    # Pantalla para el degradado
    pantallaNegra = pygame.Surface((ancho, alto))
    pantallaNegra.fill((0, 0, 0))

    # Creacion de input boxes
    input_box1 = InputBox(100, 100, 100, 32,"Nombre de aldea")
    input_box2 = InputBox(100, 200, 100, 32,"Heroe")
    input_box3 = InputBox(100, 300, 100, 32,"Explorador")
    input_box4 = InputBox(100, 400, 100, 32,"Mascota")
    input_boxes = [input_box1, input_box2, input_box3,input_box4]

    # Crear objeto boton
    # ((posx,posy)),fuente,texto,screen,colordeletra, color de recuadro,colordefondo
    botonEmpezar = Boton((ancho, alto) , 30, "Empezar", screen, "black", "black",(62, 62, 62))
    botonAceptar = Boton((ancho/ 2 + 45 , alto/ 2 + 45) , 24, "Aceptar", screen, "black", "black", "grey")
    botonMusicaOn = Boton((ancho,40 ), 24, "On", screen, "black", (Helper.COLORACTIVO), "green")
    botonMusicaOff = Boton((ancho - 30, 40 ), 24, "Off", screen, "black", (Helper.COLORACTIVO),(12, 109, 0))

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
            
            
            popUp.dibujarCuadro(popArriba,popAbajo,screen)
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
                




        #al clickear boton empezar
        if botonEmpezar.click(event):  
            aldea = input_box1.getText()
            heroe = input_box2.getText()
            explorador = input_box3.getText()
            mascota = input_box4.getText()
            botonEmpezar.setRecuadro(Helper.COLORACTIVO)
                
        
            if aldea == "" or heroe == "" or explorador == "" or mascota == "": 
                    error = True
                    botonEmpezar.setRecuadro("black")
            else:
                if error == False:
                    Helper.fadeMusic(3000)
                    degradado()
                    Juego(aldea, heroe, explorador, mascota)
                    Menu = False

def Islasini():
    ancho = 640
    alto = 480
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()

    #Crear objeto boton
    #((posx,posy)),fuente,texto,screen,colordeletra, color de recuadro,colordefondo
    botonEmpezar = Boton((ancho, alto) , 30, "Empezar", screen, "black", "black", (62, 62, 62))

    Menu = True


    



    #Tiempo para fondo
    timerFondo = 4
    pygame.time.set_timer(timerFondo, 1000)

    while Menu:
        
        for event in pygame.event.get():
            #Salir
            if event.type == pygame.QUIT:
                Menu = False


        #Dibujar todo
        pygame.display.update()
        clock.tick(60)     
        screen.fill((255, 255, 255))

                
        
            
menu()
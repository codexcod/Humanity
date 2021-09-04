import time
import sys

# Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH
path = sys.path[0]
sys.path.append(path[:len(path) - 7])

import pygame
from codigo.Isla.Isla import Isla
from codigo.Camara.Camara import Camara
from codigo.Camara.UI.UI import UI
from codigo.Camara.Zoom import Zoom
from codigo.Camara.Mouse import Mouse
from codigo.Menu.InputBox import InputBox
from codigo.Menu.buttom import Boton
from codigo.Menu.popUp import PopUp
from codigo.Isla.Helper import Helper

from codigo.Isla.Aldea import Aldea
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.Objetos.Casa import Casa

pygame.init()
def Juego(nombreAldea):
    ancho = 100
    altura = 100
    isla = Isla(ancho, altura)
    aldea = Aldea(nombreAldea)
    isla.agregarAldea(aldea, ancho // 2, altura // 2)

    #Camara para controlar el zoom
    camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)

    #Controlar tiempo en el juego
    clock = pygame.time.Clock()
    screenUpdate = 1
        #Tiempo para personas
    pygame.time.set_timer(screenUpdate,250)
        #Tiempo para arboles
    arboles = 2
    pygame.time.set_timer(arboles,10000)

    running = True
    while running:
<<<<<<< HEAD
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    if not camara.getUI().hayUIActivos():
                        if not mouse.seleccionarMovible() is None:
                            camara.getUI().generarInfoObjeto(mouse.seleccionarMovible())

                        elif not mouse.pedirInfoObjeto() is None:
                            camara.getUI().generarInfoObjeto(mouse.pedirInfoObjeto())

                    else:
                        mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())
                        
=======
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
>>>>>>> a1ff44f8086d06eca0785c3b77d43cb61adaef32

                if event.type == pygame.MOUSEBUTTONDOWN:
                    left, middle, right = pygame.mouse.get_pressed()
                    if left:
                        if not camara.getUI().hayUIActivos():
                            if not mouse.pedirInfoObjeto() is None:
                                camara.getUI().generarInfoObjeto(mouse.pedirInfoObjeto())

                        else:
                            mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())
                            

                    if right:
                        if not mouse.pedirInfoObjeto() is None:
                            """mouse.pedirInfoObjeto().onClick()"""
                            
                        if not mouse.seleccionarMovible() is None:
                            if not camara.getSeleccionado() ==  mouse.seleccionarMovible():
                                camara.setSeleccionado(mouse.seleccionarMovible())

                            else:
                                camara.setSeleccionado(None)
                        else:
                            if not camara.getSeleccionado() is None:
                                if  mouse.pedirInfoObjeto() is None:
                                    camara.getSeleccionado().moveToPosition(mouse.getObjectMousePosition()[0],mouse.getObjectMousePosition()[1])
                                
                                else:
                                    camara.getSeleccionado().accionarObjeto(mouse.getObjectMousePosition()[0],mouse.getObjectMousePosition()[1])




                    if event.button == 4:
                        camara.getZoom().bajarZoom()

                    if event.button == 5:
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
                        camara.setPosY(altura // 2)
                        camara.setPosX(ancho // 2)

                if event.type == screenUpdate:
                    for persona in aldea.getPersonas():
                        persona.makeMoves()

                if event.type == arboles:
                    for arbol in isla.getArbolesTalados():
                        arbol.avanzarTiempo()
                
                        
            camara.actualizarPantalla()
            camara.getUI().generarAldeaUI(aldea)
            camara.dibujarUI()
            pygame.display.update()

            clock.tick(60)


def menu():
    ancho = 640
    alto = 480
    screen = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    #Pantalla para el degradado
    pantallaNegra = pygame.Surface((ancho, alto))
    pantallaNegra.fill((0,0,0))
    #Creacion de input boxes
    input_box1 = InputBox(100, 100, 100, 32,"Nombre de aldea")
    input_box2 = InputBox(100, 200, 100, 32,"Heroe")
    input_box3 = InputBox(100, 300, 100, 32,"Explorador")
    input_boxes = [input_box1, input_box2, input_box3]

    #Crear objeto boton
    botonEmpezar = Boton((ancho,alto) ,30,"Empezar",screen,"gold")
    botonAceptar = Boton((ancho/2 + 45 , alto/2 + 45) ,24,"Aceptar",screen,"black")
    Menu = True
    error = False
    popUp = PopUp(ancho,alto)

    #dibujar
    def dibujarMenu(error):
        screen.fill((128,0,0))
        for box in input_boxes:
            box.dibujarCaja(screen)
        botonEmpezar.dibujarBoton((255,69,0),"black",1)
        if error == True:
            popArriba = "Debe completar todos los campos "
            popAbajo = "Pulsa el boton aceptar para continuar"
            
            
            popUp.dibujarCuadro(popArriba,popAbajo,screen)
            botonAceptar.dibujarBoton("grey","black",1)
            
            

                
    #Cerrar
    while Menu:
        
        for event in pygame.event.get():
            #Salir
            if event.type == pygame.QUIT:
                Menu = False
            #Funcionamiento de los inputs llamando a un evento interno
            for box in input_boxes:
                box.InputEventos(event,screen)
            
            
        #Hacer que los inputs se hagan mas grandes
        for box in input_boxes:
            box.update(ancho)

        #Dibujar todo
        def degradado():
            for alpha in range(0, 300):
                pantallaNegra.set_alpha(alpha)
                dibujarMenu(error)
                screen.blit(pantallaNegra, (0,0))
                pygame.display.update()
                pygame.time.delay(5)

        

        pygame.display.update()
        clock.tick(60)           
        dibujarMenu(error)
        
        if botonAceptar.click(event):
            error = False
            
        
        if botonEmpezar.click(event):  
            aldea = input_box1.getText()
            heroe = input_box2.getText()
            explorador = input_box3.getText()

        

        #   Guardado para cuando lo optimicemos
                
        
            if aldea == "" or heroe == "" or explorador == "": 
                    error = True
                   
            else:
                if error == False:
                    degradado()
                    aldea = input_box1.getText()
                    Juego(aldea)
                    Menu = False
            
                

<<<<<<< HEAD
Juego("down")
=======
menu()
>>>>>>> a1ff44f8086d06eca0785c3b77d43cb61adaef32

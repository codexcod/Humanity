import sys
from typing import Text

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
from codigo.Isla.Aldea import Aldea
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.Objetos.Casa import Casa

pygame.init()



def Juego():
    ancho = 400
    altura = 410
    isla = Isla(ancho, altura)
    aldea = Aldea("Aldea de tuke")
    isla.agregarAldea(aldea, ancho // 2, altura // 2)

    clock = pygame.time.Clock()

    #Camara para controlar el zoom
    camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)

    #Controlar tiempo en el juego
    
    screenUpdate = 1
        #Tiempo para personas
    pygame.time.set_timer(screenUpdate,250)
        #Tiempo para arboles
    arboles = 2
    pygame.time.set_timer(arboles,10000)

    running = True
    while running:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    if not camara.getUI().hayUIActivos():
                        if not mouse.pedirInfoObjeto() is None:
                            camara.getUI().generarInfoObjeto(mouse.pedirInfoObjeto())
                        
                        else:
                            mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())

                    else:
                        mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())
                        

                if right:
                    if not mouse.pedirInfoObjeto() is None:
                        mouse.pedirInfoObjeto().onClick()
                        
                    if not mouse.seleccionarMovible() is None:
                        if not camara.getSeleccionado() ==  mouse.seleccionarMovible():
                            camara.setSeleccionado(mouse.seleccionarMovible())

                        else:
                            camara.setSeleccionado(None)
                    else:
                        if not camara.getSeleccionado() is None:
                            camara.getSeleccionado().moveToPosition(mouse.getObjectMousePosition()[0],mouse.getObjectMousePosition()[1])




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

    #Creacion de input boxes
    input_box1 = InputBox(100, 100, 100, 32,"Aldea")
    input_box2 = InputBox(100, 200, 100, 32,"Amigos")
    input_box3 = InputBox(100, 300, 100, 32,"Campo vacio")
    input_boxes = [input_box1, input_box2, input_box3]
    #Crear objeto boton
    boton = Boton((ancho-150, alto-40),font=30)

    Menu = True
    while Menu:
        for event in pygame.event.get():
            #Salir
            if event.type == pygame.QUIT:
                Menu = False
            #Funcionamiento de los inputs llamando a un evento interno
            for box in input_boxes:
                box.InputEventos(event)
        #Hacer que los inputs se hagan mas grandes
        for box in input_boxes:
            box.update(ancho)

        #Dibujar todo
        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.dibujarCaja(screen)

        boton.dibujarBoton("Empezar",screen)
        pygame.display.flip()
        clock.tick(60)

        #Conseguir datos de input boxes
        # input1 = input_box1.getText()
        # input2 = input_box1.getText()
        # input3 = input_box1.getText()


        #Boton empezar
        if boton.click(event):
            Juego()
            Menu= False

menu()

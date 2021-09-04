
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
from codigo.Isla.Helper import Helper

from codigo.Isla.Aldea import Aldea
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.Objetos.Casa import Casa

pygame.init()

ancho = 400
altura = 410
isla = Isla(ancho, altura)
aldea = Aldea("Aldea de tuke")
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
                        

def Juego(nombreAldea):
    ancho = 400
    altura = 410
    isla = Isla(ancho, altura)
    aldea = Aldea(nombreAldea)
    isla.agregarAldea(aldea, ancho // 2, altura // 2)

                    else:
                        camara.setSeleccionado(None)
                else:
                    if not camara.getSeleccionado() is None:
                        camara.getSeleccionado().moveToPosition(mouse.getObjectMousePosition()[0],mouse.getObjectMousePosition()[1])




            if event.button == 4:
                camara.getZoom().bajarZoom()

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
    input_box2 = InputBox(100, 200, 100, 32,"Explorador requete lindo")
    input_box3 = InputBox(100, 300, 100, 32,"Campo vacio")
    input_boxes = [input_box1, input_box2, input_box3]

    #Crear objeto boton
    botonEmpezar = Boton((ancho,alto) ,30)
    botonAceptar = Boton((ancho/2 + 55, alto/2 + 60) ,24)
    Menu = True
    error = False
    

    #dibujar
    def dibujarMenu(error):
        screen.fill((178,34,34))
        
        if error == False:
            for box in input_boxes:
                box.dibujarCaja(screen)
            botonEmpezar.dibujarBoton("Empezar",screen,"gold","brown","black",1)
            pygame.display.update()
            clock.tick(60)
            
        if error == True:
            pygame.draw.circle(screen, "white", (ancho/2, alto/2), 100)
            pygame.draw.circle(screen, "red", (ancho/2, alto/2), 100,10)
            pygame.draw.circle(screen, "grey", (ancho/2 + 45, alto/2 + 42), 15)
            pygame.draw.circle(screen, "grey", (ancho/2 - 45, alto/2 + 42), 15)
            
            Aviso1 = Helper.FUENTE(13).render("Debe completar ", True, "black")
            Aviso2 = Helper.FUENTE(13).render("todos los campos", True, "black")
            screen.blit(Aviso1,(ancho/2 - 50, alto/2 - 40))
            screen.blit(Aviso2,(ancho/2 - 50, alto/2 - 20))
            botonAceptar.dibujarBoton("Aceptar",screen,"black","grey","red",0)
            pygame.display.update()
            if botonAceptar.click(event):
                error = False
                
    #Cerrar
    while Menu:
        print(error)
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
        # def degradado():
        #     for alpha in range(0, 300):
        #         pantallaNegra.set_alpha(alpha)
        #         dibujarMenu()
        #         screen.blit(pantallaNegra, (0,0))
        #         pygame.display.update()
        #         pygame.time.delay(5)

        
        
        
        dibujarMenu(error)
        if botonEmpezar.click(event):
            
            aldea = input_box1.getText()
            input2 = input_box2.getText()
            input3 = input_box3.getText()
        #   Guardado para cuando lo optimicemos
        #   degradado()
            if aldea is None or input2 is None or input3 is None: 
                aldea = input_box1.getText()
                Juego(aldea)
                Menu= False
            else:
                error = True
                
                

menu()

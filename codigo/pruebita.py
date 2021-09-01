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

from codigo.Isla.Aldea import Aldea
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.Objetos.Casa import Casa

pygame.init()

ancho = 400
altura = 410
isla = Isla(ancho, altura)
aldea = Aldea("Aldea de tuke")
isla.agregarAldea(aldea, ancho // 2, altura // 2)

camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
mouse = Mouse(camara)


clock = pygame.time.Clock()
screenUpdate = pygame.USEREVENT
pygame.time.set_timer(screenUpdate,250)

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
                

            if right:
                if not mouse.pedirInfoObjeto() is None:
                    mouse.pedirInfoObjeto().onClick()
                
                if not mouse.seleccionarMovible() is None:
                    camara.setSeleccionado(mouse.seleccionarMovible())

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

            
        

    camara.actualizarPantalla()
    camara.getUI().generarAldeaUI(aldea)
    camara.dibujarUI()
    pygame.display.update()

    clock.tick(60)

import sys
#Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH
path = sys.path[0] 
sys.path.append(path[:len(path) - 7] )


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

ancho = 60
altura = 50
isla = Isla(ancho, altura)
aldea = Aldea("Aldea de tuke")
casa = Casa(aldea)
aldea.agregarCasa(casa)
juan = Persona("Juan",casa)
tuke = Persona("Tuke",casa)
gonza = Persona("Gonza",casa)
casa.agregarPersona(juan)
casa.agregarPersona(tuke)
casa.agregarPersona(gonza)

isla.agregarObjeto(ancho // 2,altura // 2,casa)
isla.agregarObjeto(ancho // 2 + 2,altura // 2,tuke)
isla.agregarObjeto(ancho // 2 - 2,altura // 2,juan)
isla.agregarObjeto(ancho // 2,altura // 2 +2,gonza)

camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM,UI())
mouse = Mouse(camara)

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


            if event.button == 4:
                camara.getZoom().bajarZoom()

            if event.button == 5:
                camara.getZoom().subirZoom()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                camara.moveX(1)

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                camara.moveX(-1)

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                camara.moveY(-1)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                camara.moveY(1)

            if event.key == pygame.K_z:
                camara.getZoom().subirZoom()

            if event.key == pygame.K_x:
                camara.getZoom().bajarZoom()

    camara.actualizarPantalla()
    camara.dibujarUI()
    pygame.display.update()

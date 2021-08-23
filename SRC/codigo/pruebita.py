import pygame
from Isla import Isla
from Camara import Camara
from UI import UI
from Zoom import Zoom
from Mouse import Mouse

pygame.init()

ancho = 60
altura = 50
isla = Isla(ancho, altura)

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
                        mouse.pedirInfoObjeto().onClick()

                else:
                    mouse.clickearPorPoscicion(camara.getUI().getObjetosClickeables())

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

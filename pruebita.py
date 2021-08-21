import pygame
from Isla import Isla
from Camara import Camara
from Zoom import Zoom

pygame.init()

ancho = 60
altura = 50
isla = Isla(ancho, altura)

camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM)



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                camara.moveX(1)

            if event.key == pygame.K_LEFT:
                camara.moveX(-1)


            if event.key == pygame.K_UP:
                camara.moveY(-1)

            if event.key == pygame.K_DOWN:
                camara.moveY(1)

            if event.key == pygame.K_z:
                camara.getZoom().subirZoom()

            if event.key == pygame.K_x:
                camara.getZoom().bajarZoom()

    camara.actualizarPantalla()
    pygame.display.update()

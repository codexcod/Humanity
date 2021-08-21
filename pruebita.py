import pygame
from Isla import Isla
from Camara import Camara
from Zoom import Zoom

pygame.init()

ancho = 60
altura = 50
isla = Isla(ancho, altura)
isla.generarMapaEstatico()
camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM)

fuente = pygame.font.Font(None, 60)

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

    texto = fuente.render(f"x : {camara.getPosX()}  y :  {camara.getPosY()} ", False, (250, 100, 100))
    camara.actualizarPantalla()
    camara.screen.blit(texto, (40, 40))
    pygame.display.update()

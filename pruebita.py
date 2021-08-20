import pygame
from Isla import Isla
from Camara import Camara

pygame.init()

ancho = 40
altura = 25
isla = Isla(ancho, altura)
isla.generarMapaEstatico()
camara = Camara(round(ancho / 2), round(altura / 2), isla)

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

    camara.actualizarPantalla()
    pygame.display.update()

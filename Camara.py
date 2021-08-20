import pygame


class Camara:

    def __init__(self, posX, posY, isla):
        self.mapa = isla.getMapaEstatico()
        self.screen = pygame.display.set_mode((1000, 600))
        self.posX = posX
        self.posY = posY
        self.maxX = isla.getAncho()
        self.maxY = isla.getAltura()

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def moveX(self, posX):
        self.posX += posX

    def moveY(self, posY):
        self.posY += posY

    def chquearMaxX(self):
        if self.posX >= self.maxX - 13:
            self.posX = self.maxX - 13

        if self.posX <= 13:
            self.posX = 13

    def chquearMaxY(self):
        if self.posY >= self.maxY - 8:
            self.posY = self.maxY - 8

        if self.posY <= 8:
            self.posY = 8

    def actualizarPantalla(self):
        self.screen.fill((255, 255, 255))
        self.chquearMaxX()
        self.chquearMaxY()
        forY = 0
        for y in range(self.posY - 7, self.posY + 8):
            forX = 0
            for x in range(self.posX - 12, self.posX + 13):
                self.screen.blit(self.mapa[y][x], (forX * 40, forY * 40))
                forX += 1

            forY += 1

from Isla import Isla
import pygame
import math


class Camara:

    def __init__(self, posX, posY, isla,zoom):
        self.mapa = isla.getMapaEstatico()
        self.isla = isla
        self.screen = pygame.display.set_mode((1000, 600))
        self.posX = posX
        self.posY = posY
        self.maxX = isla.getAncho()
        self.maxY = isla.getAltura()
        self.zoom = zoom
        self.rangoZoom = [50,40,25,20]
    



    def subirZoom(self):
        self.zoom += 1
        if self.zoom >= 3:
            self.zoom = 3
            return False

        if (1000 // self.rangoZoom[self.zoom]) >= self.isla.getAncho() or (600 // self.rangoZoom[self.zoom]) >= self.isla.getAltura():
            self.zoom -= 1
            return False

        return True


    def bajarZoom(self):
        self.zoom -= 1
        if self.zoom <= 0:
            self.zoom = 0
            return False

        return True    
        

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY    

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def moveX(self, posX):
        self.posX += posX

    def moveY(self, posY):
        self.posY += posY

    def chquearMaxX(self):
        if self.posX >= self.maxX - ((1000 // self.rangoZoom[self.zoom]) // 2):
            self.posX = self.maxX - ((1000 // self.rangoZoom[self.zoom]) // 2)

        if self.posX <= (1000 // self.rangoZoom[self.zoom] // 2) + 1:
            self.posX = (1000 // self.rangoZoom[self.zoom] // 2) + 1

    def chquearMaxY(self):
        if self.posY >= self.maxY - ((600 // self.rangoZoom[self.zoom]) // 2):
            self.posY = self.maxY - ((600 // self.rangoZoom[self.zoom]) // 2)

        if self.posY <= (600 // self.rangoZoom[self.zoom] // 2) + 1:
            self.posY = (600 // self.rangoZoom[self.zoom] // 2) + 1

    def actualizarPantalla(self):
        self.screen.fill((255, 255, 255))
        self.chquearMaxX()
        self.chquearMaxY()
        forY = 0
        for y in range(self.posY - math.floor((600 // self.rangoZoom[self.zoom]) / 2), self.posY + math.ceil((600 // self.rangoZoom[self.zoom]) / 2)):
            forX = 0
            for x in range(self.posX - math.floor((1000 // self.rangoZoom[self.zoom]) / 2), self.posX + math.ceil((1000 // self.rangoZoom[self.zoom]) / 2)):
                superficie = pygame.Surface((self.rangoZoom[self.zoom],self.rangoZoom[self.zoom]))
                superficie.fill(self.mapa[y][x],None,0)
                self.screen.blit(superficie, (forX * self.rangoZoom[self.zoom], forY * self.rangoZoom[self.zoom]))
                forX += 1

            forY += 1

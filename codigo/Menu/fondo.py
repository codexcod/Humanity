import pygame
from codigo.Isla.Helper import Helper

class Fondo:
    def __init__(self,ancho,alto): 
        self.animacion = 1
        self.secondImage = Helper.FONDOANIMACION(self.animacion)
        self.firstImage = pygame.transform.scale(Helper.FONDO, (ancho, alto))
        self.ancho = ancho
        self.alto = alto
        

    def getfirstImage(self):
        return self.firstImage

    def cambiarAnimacion(self):
        self.animacion += 1
        if self.animacion == 17:
            self.animacion = 1
        self.secondImage = pygame.transform.scale(Helper.FONDOANIMACION(self.animacion), (self.ancho, self.alto))

        
    def getSecondImage(self):
        return self.secondImage
    

        

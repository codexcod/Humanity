import pygame
from codigo.Menu.buttom import Boton
from codigo.Isla.Helper import Helper

class PopUp:
    def __init__(self, ancho, alto):
        self.rect = pygame.Rect(ancho/ 2 - 150, alto/2 - 50, 300, 100)
        self.ancho = ancho
        self.alto = alto

    def getAlto(self):
        return self.alto

    def getAncho(self):
        return self.ancho

    def getRect(self):
        return self.rect

    def dibujarCuadro(self, Aviso1, Aviso2, screen):
            # Dibuja el cuadrado
            Aviso1 = Helper.FUENTE(13).render("Debe completar todos los campos ", True, "black")
            Aviso2 = Helper.FUENTE(13).render("Pulsa el boton aceptar para continuar", True, "black")
            pygame.draw.rect(screen, "white", self.getRect())
            pygame.draw.rect(screen, "red", self.getRect(), 5)
            screen.blit(Aviso1, (self.getAncho()/ 2 - 120, self.getAlto()/ 2 - 40))
            screen.blit(Aviso2, (self.getAncho()/ 2 - 128, self.getAlto()/ 2 - 20))
            
            


    
    
import pygame
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

    def dibujarCuadro(self, Aviso1, Aviso2, screen, posArriba, posAbajo):
            # Dibuja el cuadrado
            Aviso1 = Helper.FUENTE(13).render(Aviso1, True, "black")
            Aviso2 = Helper.FUENTE(13).render(Aviso2, True, "black")
            pygame.draw.rect(screen, "white", self.getRect())
            pygame.draw.rect(screen, "red", self.getRect(), 5)
            screen.blit(Aviso1, (posArriba))
            screen.blit(Aviso2, (posAbajo))
            
            


    
    
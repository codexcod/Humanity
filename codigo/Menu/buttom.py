import pygame

pygame.init()


class Boton:
    #Crear el boton, despues dibujarlo

    def __init__(self,  pos, font):
        self.x, self.y = pos
        self.pos = (self.x,self.y)
        self.font = pygame.font.SysFont("Arial", font)

    def dibujarBoton(self, text,screen,color,colorfondo,colorRec,recuadro):
        self.text = self.font.render(text, 1, pygame.Color(color))
        self.size = self.text.get_size()
        rectX = (self.x - (self.size[0] + 6)) - (self.size[0]/10)
        rectY = (self.y -(self.size[1]+3)) - (self.size[1]/10)
        self.rect = pygame.Rect(rectX, rectY, self.size[0] + 6, self.size[1]+3) 

        #Dibujar fondo de boton
        pygame.draw.rect(screen,(colorfondo),self.rect)

        #Dibujar recuadro     
        if not recuadro == 0:
            pygame.draw.rect(screen,(colorRec),self.rect,2)

        #Dibujar el texto
        screen.blit(self.text,(rectX + 3,rectY))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = pygame.mouse.get_pressed()[0]
            if self.rect.collidepoint(x, y) and left:
                return True

    def getPos(self):
        return self.pos


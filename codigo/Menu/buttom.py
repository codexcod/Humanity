import pygame

pygame.init()


class Boton:
    #Crear el boton, despues dibujarlo

    def __init__(self,  pos, font,text,screen,color):
        self.x, self.y = pos
        self.screen = screen
        self.pos = (self.x,self.y)
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.getFont().render(text, 1, pygame.Color(color))
        self.size = self.text.get_size()
        rectX = (self.x - (self.getTSize()[0] + 6)) - (self.getTSize()[0]/10)
        rectY = (self.y -(self.getTSize()[1]+3)) - (self.getTSize()[1]/10)
        self.rect = pygame.Rect(rectX, rectY, self.getTSize()[0] + 6, self.getTSize()[1]+3) 

    
    def dibujarBoton(self, colorfondo,colorRec,recuadro):
        rectX = (self.getX() - (self.getTSize()[0] + 6)) - (self.getTSize()[0]/10)
        rectY = (self.getY() -(self.getTSize()[1]+3)) - (self.getTSize()[1]/10)
        #Dibujar fondo de boton
        screen = self.getScreen()
        pygame.draw.rect(screen,(colorfondo),self.getRect())

        #Dibujar recuadro     
        if not recuadro == 0:
            pygame.draw.rect(screen,(colorRec),self.rect,2)

        #Dibujar el texto
        screen.blit(self.getText(),(rectX + 3,rectY))


    def click(self, event):
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            seleccionado = pygame.mouse.get_pos()
            if  self.getRect().collidepoint(seleccionado):
                return True
        else:
            return False

    def getRect(self):
        return self.rect

    def getFont(self):
        return self.font

    def getTSize(self):
        return self.size

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getText(self):
        return self.text

    def getScreen(self):
        return self.screen
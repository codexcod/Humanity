import pygame

pygame.init()


class Boton:
    #Crear el boton, despues dibujarlo

    def __init__(self, pos, font, text, screen, color, colorRec, colorfondo):
        self.x, self.y = pos
        self.screen = screen
        self.pos = (self.x, self.y)
        self.font = pygame.font.SysFont("Arial", font)
        self.text = self.getFont().render(text, 1, pygame.Color(color))
        self.size = self.text.get_size()
        rectX = (self.x - (self.getTSize()[0] + 6)) - (self.getTSize()[0] / 10)
        rectY = (self.y - (self.getTSize()[1] + 3)) - (self.getTSize()[1] / 10)
        self.rect = pygame.Rect(rectX, rectY, self.getTSize()[0] + 6, self.getTSize()[1] + 3) 
        self.colorRec = colorRec
        self.colorfondo = colorfondo
    
    def dibujarBoton(self, recuadro):
        rectX = (self.getX() - (self.getTSize()[0] + 6)) - (self.getTSize()[0] / 10)
        rectY = (self.getY() - (self.getTSize()[1] + 3)) - (self.getTSize()[1] / 10)
        #Dibujar fondo de boton
        screen = self.getScreen()
        pygame.draw.rect(screen, (self.getcolorFondo()) ,self.getRect())

        #Dibujar recuadro     
        if not recuadro == 0:
            pygame.draw.rect(screen, (self.getColorRecuadro()), self.rect,recuadro)

        #Dibujar el texto
        screen.blit(self.getText(), (rectX + 3,rectY))

    def setRecuadro(self, color):
        self.colorRec = color

    def setcolorFondo(self, color):
        self.colorfondo = color


    def click(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
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
    
    def getColorRecuadro(self):
        return self.colorRec
    
    def getcolorFondo(self):
        return self.colorfondo
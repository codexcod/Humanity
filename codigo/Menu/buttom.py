import pygame

pygame.init()


class Boton:
    #Crear el boton, despues dibujarlo

    def __init__(self,  pos, font):
        self.x, self.y = pos
        self.pos = (self.x,self.y)
        self.font = pygame.font.SysFont("Arial", font)

    def dibujarBoton(self, text,screen):
        self.text = self.font.render(text, 1, pygame.Color("gold"))
        self.size = self.text.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        pygame.draw.rect(screen,("brown"),self.rect)
        screen.blit(self.text,(self.x,self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True

    def getPos(self):
        return self.pos


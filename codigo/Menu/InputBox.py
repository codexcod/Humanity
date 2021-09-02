from typing import Text
import pygame

COLORINACTIVO = pygame.Color('lightskyblue3')
COLORACTIVO = pygame.Color('dodgerblue2')
class InputBox:

    def __init__(self, x, y, w, h,header, show=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.header = header
        self.color = COLORINACTIVO
        self.show = show
        self.text = ""
        self.fuente = pygame.font.Font(None, 32)
        self.txt_surface = self.fuente.render(show, True, self.color)
        self.active = False
        
    def InputEventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario clickea en el input box, Activarse.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

            # Marcar con color si esta activada o no
            if self.active: 
                self.color = COLORACTIVO 
            else: 
                self.color = COLORINACTIVO

        #Borrar de a uno con backspace y borrar todo con enter
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = self.show
                    self.show = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.show = self.show[:-1]
                
            #Escribir las caracteres
                else:
                    self.show += event.unicode

                # Re-render the show.
                self.txt_surface = self.fuente.render(self.show, True, "Red")


    def update(self):
        # Expandir el input box si el texto es muy grande.
        width = max(200, self.txt_surface.get_width()+5)
        self.rect.w = width

    def Dibujarcaja(self, screen):
        header = self.fuente.render(self.header, True, "black")
        screen.blit(header,(self.rect.x , self.rect.y - 30))
        # Dibujar el texto
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Dibujar el cuadro de texto
        pygame.draw.rect(screen, self.color, self.rect, 2)
    
    def getText(self):
        return self.text
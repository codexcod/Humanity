from typing import Text
from codigo.Isla.Helper import Helper
import pygame


class InputBox:

    def __init__(self, x, y, w, h,header, show=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.header = header
        self.color = Helper.COLORINACTIVO
        self.show = show
        self.text = ""
        self.fuente = Helper.FUENTE(22)
        self.txt_surface = self.fuente.render(show, True, self.color)
        self.active = False
        self.width = 200
    
    
        
    def dibujarTexto(self,screen):
        header = self.fuente.render(self.header, True, (0,0,0))
        if self.active:
                headerSelect = self.fuente.render(self.header, True, Helper.COLORACTIVO)
                screen.blit(headerSelect,(self.rect.x , self.rect.y - 31))
                screen.blit(headerSelect,(self.rect.x  , self.rect.y - 29))
                screen.blit(headerSelect,(self.rect.x - 1, self.rect.y - 30))
                screen.blit(headerSelect,(self.rect.x + 1, self.rect.y - 32))
        else:
            pass
        screen.blit(header, (self.rect.x , self.rect.y - 30))
    
    def InputEventos(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario clickea en el input box, Activarse.
            if self.rect.collidepoint(event.pos):
                self.active = True
                # Remarco el texto
            else:
                self.active = False

            # Marcar con color si esta activada o no
            if self.active: 
                self.color = Helper.COLORACTIVO 

            else: 
                self.color = Helper.COLORINACTIVO

        #Borrar de a uno con backspace y borrar todo con enter
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.show = self.show[:-1]
                    self.txt_surface = self.fuente.render(self.show, True, "White")
                
            #Escribir las caracteres
                else:
                    self.show += event.unicode
                    #Dibujar cada letra
                    self.txt_surface = self.fuente.render(self.show, True, "White")  
                
                
        self.text = self.show


    def update(self,ancho):
        # Expandir el input box si el texto es muy grande.        
        self.width = max(200, self.txt_surface.get_width()+5)
        
        self.rect.w = self.width

    def dibujarCaja(self, screen):
        #Dibujar fondo
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 3))
        pygame.draw.rect(screen, "black", self.rect)

        # Dibujar el texto
        self.dibujarTexto(screen)

        # Dibujar el cuadro de texto
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 3))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    
    def getText(self):
        return self.text
from codigo.Isla.Movibles.Movible import Movible
from codigo.Isla.Helper import Helper
import pygame
from codigo.Camara.UI.CloseUI import CloseUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper

class Persona(Movible):

    def __init__(self,nombre,casa,x,y,isla):
        Movible.__init__(self,x,y,isla)
        self.edad = 0
        self.casa = casa
        self.nombre = nombre
        self.image = Helper.PERSONA
        self.inventario = []
        self.accionar = [False,0,0]
        

    def getCasa(self):
        return self.casa

    def getAldea(self):
        return self.casa.getAldea()

    def getInfoStr(self):
        result = self.nombre
 
        return result

    def agregarInventario(self,objeto):
        self.inventario.append(objeto)

    def getInventario(self):
        return self.inventario

    def getUI(self):
        info = []
        fondo = pygame.surface.Surface((800, 500))
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(25)
        texto = self.getInfoStr()
        lineas = texto.splitlines()
        forI = 0 
        for i in lineas:
            textObject = font.render(i, True, (255, 255, 255), None)
            info.append(UIObject(textObject, 550, 70 + forI * 40))
            forI += 1
        
        image = pygame.transform.scale(self.getImage(), (200, 200))
        info.append(UIObject(image, 200, 200))

        forPosX = 0
        forPosY = 0
        for objeto in self.inventario:
            fondoObjeto = pygame.surface.Surface((40, 40))
            fondoObjeto.fill((82, 30, 0), None, 0)
            info.append(UIObject(fondoObjeto,550 + 40 * forPosX,120+ 40 * forPosY ))
            imagenObjeto = pygame.transform.scale(objeto.getImage(), (40, 40))
            info.append(UIObject(imagenObjeto,550 + 40 * forPosX,120 + 40 * forPosY))
            if forPosX == 7:
                forPosX = 0
                forPosY += 1

            else:
                    
                forPosX += 1
        
        return info

    def accionarObjeto(self,posX,posY):
        self.moveToPosition(posX,posY)  
        self.accionar = [True,posX,posY]

    def makeMoves(self):
        if len(self.moves) > 0:
            if self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1]):
                self.moves.pop(len(self.moves) - 1)
                if len(self.moves) == 1:
                    if self.accionar[0]:
                        self.agregarInventario(self.isla.getMapaObjetos()[self.accionar[2]][self.accionar[1]]) 
                        self.isla.getMapaObjetos()[self.accionar[2]][self.accionar[1]].onClick()
                        self.accionar[0] = False


            else:
                
                if self.moves[len(self.moves) - 1][0] == 0:

            
                    if self.directionX > 0:
                        self.moves.append([1,0])
                        self.moves.insert(0,[-1,0])

                    else:
                        self.moves.append([-1,0])
                        self.moves.insert(0,[1,0])

                else:
                    
                    if self.directionY > 0:
                        self.moves.append([0,1])
                        self.moves.insert(0,[0,-1])

                    else:
                        self.moves.append([0,-1])
                        self.moves.insert(0,[0,1])
                    
        

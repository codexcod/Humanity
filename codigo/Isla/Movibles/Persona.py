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
        self.trabajando = False
        self.tiempoTrabajando = 0

    def toJson(self):
        jsonText = {
            'objeto' : 'Persona',
            'name' : self.nombre,
            'edad' : self.edad,
            'x' : self.x,
            'y' : self.y,
            'inventario' : []
        }

        for objeto in self.inventario:
            jsonText['inventario'].append(objeto.toJson())

        return jsonText
        

    def getCasa(self):
        return self.casa

    def getAldea(self):
        return self.casa.getAldea()

    def getInfoStr(self):
        result = self.nombre
 
        return result

    def agregarInventario(self,objeto):
        if len(self.inventario) < 80:
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
            fondoObjeto = pygame.transform.scale(Helper.INVENTARIO, (40, 40))
            info.append(UIObject(fondoObjeto,550 + 40 * forPosX,120+ 40 * forPosY ))
            imagenObjeto = pygame.transform.scale(objeto.getImage(), (30, 30))
            info.append(UIObject(imagenObjeto,550 + 40 * forPosX +  5 ,120 + 40 * forPosY + 5))
            if forPosX == 7:
                forPosX = 0
                forPosY += 1

            else:
                    
                forPosX += 1
        
        return info

    def moveToPosition(self,posX,posY):
        self.moves.clear()
        self.accionar[0] = False
        
        for y in range(abs(posY - self.y)):
            
            if posY - self.y > 0:
                self.moves.append([0,1])

            elif posY - self.y < 0:
                self.moves.append([0,-1])

        for x in range(abs(posX - self.x)):
            if posX - self.x > 0:
                self.moves.append([1,0])

            elif posX - self.x < 0:
                self.moves.append([-1,0])

        self.directionX = 0
        self.directionY = 0
        for move in self.moves:
            self.directionX += move[0]
            self.directionY += move[1]
                    


    def accionarObjeto(self,objeto):
        if not self.trabajando:
            self.moveToPosition(objeto.getX(),objeto.getY())  
            self.accionar = [True,objeto]

    def makeMoves(self):
        if not self.trabajando:
            if len(self.moves) > 0:
                if self.accionar[0]:
                        if self.tieneAlLado(self.accionar[1].getX(),self.accionar[1].getY()):
                            self.definirTrabajo(self.accionar[1])

                        elif len(self.moves) == 1:
                            if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                                self.accionarObjeto(self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()])

                            else:
                                self.accionarObjeto(self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()])
                                
                if self.move(self.moves[len(self.moves) - 1][0],self.moves[len(self.moves) - 1][1]):
                    self.moves.pop(len(self.moves) - 1)
                            
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
                
        else:
            self.trabajar()



    def definirTrabajo(self,objeto):
        if objeto.getNombre()[:4] == "Casa":
            if self.tieneAlgoEnElInventario():
                self.trabajando = True
                self.tiempoTrabajando = len(self.inventario)
                self.setImage(Helper.PERSONA_TRABAJANDO)

        elif not objeto.getTrabajo() == 0:
            self.trabajando = True
            self.tiempoTrabajando = objeto.getTrabajo()
            self.setImage(Helper.PERSONA_TRABAJANDO)
                    
        
    def trabajar(self):
        if self.trabajando:
            self.tiempoTrabajando -= 1
            if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                if self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].getNombre()[:4] == "Casa":
                    self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].getAldea().añadirObjeto(self.inventario[len(self.inventario) - 1])
                    self.inventario.pop(len(self.inventario) - 1)

            if self.tiempoTrabajando == 0:
                self.trabajando = False
                self.setImage(Helper.PERSONA)
                if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    if not self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].getValor() is None:
                        for objeto in self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].getValor():
                            self.agregarInventario(objeto) 
                    self.isla.getMapaObjetos()[self.accionar[1].getY()][self.accionar[1].getX()].onClick()

                elif not self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()] is None:
                    valor = self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()].getValor()
                    if not valor is None:
                        for objeto in valor:
                            self.agregarInventario(objeto) 
                    
                    else:
                        self.isla.getMapaMovible()[self.accionar[1].getY()][self.accionar[1].getX()].onClick()

                self.accionar[0] = False
                self.moves.clear()

    def tieneAlgoEnElInventario(self):
        return len(self.inventario) > 0
            

        
                    

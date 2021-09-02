from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
import random


class Arbol(Objeto):

    def __init__(self,x,y,isla):
        Objeto.__init__(self,x,y,isla)
        self.setNombre("Arbol")
        self.setImage(Helper.ARBOL)
        self.troncos = 0
        self.talado = False
        self.tiempoCrecimiento = 0
        


    def setTroncos(self,troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            self.setImage(Helper.ARBOL_GRANDE)

        else:
            self.setImage(Helper.ARBOL)

    def getTroncos(self):
        return self.troncos

    def onClick(self):
        
        self.talarArbol()
        return super().onClick()

    def talarArbol(self):
        if self.talado == False:
            self.talado = True
            self.setImage(Helper.ARBOL_TALADO)
            self.setNombre("Arbol talado")
            self.setCaminable(True)
            self.troncos = 1
            self.isla.getArbolesTalados().append(self)

            
        else:
            self.isla.getArbolesTalados().remove(self)
            self.isla.getMapaObjetos()[self.y][self.x] = None

    
    def avanzarTiempo(self):
        if self.talado:
            if not self.isla.getMapaMovible()[self.y][self.x]:
                self.tiempoCrecimiento += 1
                if self.tiempoCrecimiento == 25:
                    self.tiempoCrecimiento = 0
                    self.crecerArbol()
                    self.isla.getArbolesTalados().remove(self)      


    def crecerArbol(self):
        self.setNombre("Arbol")
        self.setTroncos(random.randrange(5,20))
        if self.getTroncos() > 15:
            self.setImage(Helper.ARBOL_GRANDE)      
        else:
            self.setImage(Helper.ARBOL)

        self.setCaminable(False)
        self.talado = False
              
            
    def getInfoStr(self):
        result = f"""Objeto : {self.nombre}
Troncos : {self.troncos}"""
        return result


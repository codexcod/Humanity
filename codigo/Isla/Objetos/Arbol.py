from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Tronco import Tronco
import random
import json


class Arbol(Objeto):

    def __init__(self, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.setNombre("Arbol")
        self.setImage(Helper.ARBOL)
        self.troncos = 0
        self.talado = False
        self.tiempoCrecimiento = 0
        

    def toJson(self):
        return {
            'objeto' : 'Arbol',
            'name' : self.nombre,
            'troncos' : self.troncos,
            'talado' : self.talado,
            'tiempoCrecimiento' : self.tiempoCrecimiento,
            'x' : self.x,
            'y' : self.y
        }


    def setTiempoCrecimiento(self, tiempoCrecimiento):
        self.tiempoCrecimiento = tiempoCrecimiento

    def setTroncos(self, troncos):
        self.troncos = troncos
        if self.troncos >= 15:
            # En el caso que tenga muchos troncos que la imagen se vea mas grande para mantener la ilusion del mundo
            # real
            self.setImage(Helper.ARBOL_GRANDE)

        else:
            self.setImage(Helper.ARBOL)

    def getTalado(self):
        return self.talado

    def getTroncos(self):
        return self.troncos

    def setTalado(self, talado):
        self.talado = talado

    def onClick(self):
        
        self.talarArbol()
        return super().onClick()

    def talarArbol(self):
        # Cuando el arbol es talado
        if self.talado == False:
            self.talado = True
            self.setImage(Helper.ARBOL_TALADO)
            self.setNombre("Arbol talado")
            self.setCaminable(True)
            self.troncos = 1
            self.isla.getArbolesTalados().append(self)

            
        else:
            # Si talan el arbol pero ya estaba talado, que lo eliminen
            self.isla.getArbolesTalados().remove(self)
            self.isla.getMapaObjetos()[self.y][self.x] = None

    
    def avanzarTiempo(self):
        # Avanza el tiempo interno del arbol
        if self.talado:
            # Si el arbol estaba talado que ese tiempo ayude a que pueda crecer
            if not self.isla.getMapaMovible()[self.y][self.x]:
                # Si no esta en el mapa que crezca el tiempo de crecimiento
                self.tiempoCrecimiento += 1
                if self.tiempoCrecimiento == 25:
                    # Si ya llego al tiempo maximo, que crezca y que ya no sea considerado talado
                    self.tiempoCrecimiento = 0
                    self.crecerArbol()
                    self.isla.getArbolesTalados().remove(self)      


    def crecerArbol(self):
        # Que crezca el arbol
        self.setNombre("Arbol")
        self.setTroncos(random.randrange(5, 20))
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

    def getTrabajo(self,herramienta):
        if herramienta.getDañoArbol() > 0:
            return (self.troncos * 10) // herramienta.getDañoArbol() 

        return (self.troncos * 10)

    def getValor(self):
        valor = []
        for i in range(self.troncos):
            valor.append(Tronco())

        return valor

    def isArbol(self):
        return True


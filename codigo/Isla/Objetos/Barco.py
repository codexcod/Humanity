from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Isla.Objetos.Tronco import Tronco
import random


class Barco(Objeto):
    
    def __init__(self,x,y,isla):
        Objeto.__init__(self,x,y,isla)
        self.image = Helper.BARCO
        self.nombre = "Barco de travesias"
        self.roto = True


    def arreglarBarco(self):
        self.roto = False

    def getInfoStr(self):
        return  "Barco de traversias"

    def onClick(self):

    def     
        
from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Camara.UI.UIObject import UIObject
from codigo.Camara.UI.ActividadUI import ActividadUI
from codigo.Camara.UI.FlechaUI import FlechaUI

class MesaTrabajo(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.name = "Mesa de trabajo"
        self.aldea = aldea
        self.image = Helper.MESA_DE_TRABAJO
        self.numeroDeObjetos = 2

    
     def getUI(self,clickeables,lista,listaUI,ui):
        info = []
        

            
        
        return info
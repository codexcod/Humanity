from codigo.Camara.UI.VentaObjeto import VentaObjeto
from codigo.Isla.Helper import Helper
from codigo.Isla.Movibles.conejo import Conejo
from codigo.Isla.Objetos.Arbol import Arbol
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Camara.UI.UIObject import UIObject
from codigo.Camara.UI.ActividadUI import ActividadUI
from codigo.Camara.UI.FlechaUI import FlechaUI
from codigo.Isla.Objetos.Piedra import Piedra
from codigo.Isla.Objetos.Roca import Roca
from codigo.Isla.Objetos.Tronco import Tronco


class MesaTrabajo(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.name = "Mesa de trabajo"
        self.aldea = aldea
        self.image = Helper.MESA_DE_TRABAJO
        self.numeroDeObjetos = 2


    def toJson(self):
        return {
            'objeto' : 'Mesa de trabajo',
            'name' : self.nombre,
            'x' : self.x,
            'y' : self.y
        }

    
    def getUI(self,clickeables,lista,listaUI,ui):
        info = []

        fondo = Helper.getSurface(800, 500)
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))

        font = Helper.FUENTE(30)
        textPrecio = font.render("Mesa de trabajo", True, (255, 255, 255), None)
        info.append(UIObject(textPrecio, 400,75))



        listaObjetos = [[Arbol(23,50,self.isla),[[Tronco(),40],[Roca(),20]]],[Piedra(23,50,self.isla),[[Tronco(),20],[Roca(),10]]],[Conejo(23,50,self.isla,50),[[Tronco(),20],[Roca(),10]]]]

        forVenta = 0
        for venta in listaObjetos:
            ventaObjeto = VentaObjeto(venta[0],venta[1],45)
            uiVenta = ventaObjeto.getUI(150 + 250 * forVenta ,150)
            for uiObeject in uiVenta:
                info.append(uiObeject)

            forVenta += 1

        font = Helper.FUENTE(55)
        textPrecio = font.render("PROXIMAMENTE", True, (255, 255, 255), None)
        info.append(UIObject(textPrecio, 300, 250))

        return info
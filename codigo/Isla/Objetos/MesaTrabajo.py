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
from codigo.Datos.Venta import Venta
import json


class MesaTrabajo(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.name = "Mesa de trabajo"
        self.aldea = aldea
        self.image = Helper.MESA_DE_TRABAJO
        self.numeroDeObjetos = 2

    def toJson(self):
        return {
            'objeto': 'Mesa de trabajo',
            'name': self.nombre,
            'x': self.x,
            'y': self.y
        }

    def getUI(self, clickeables, lista, listaUI, ui):
        info = []

        fondo = Helper.getSurface(800, 500)
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))

        font = Helper.FUENTE(30)
        textPrecio = font.render("Mesa de trabajo", True, (255, 255, 255), None)
        info.append(UIObject(textPrecio, 400, 75))

        listaVentas = []
        data = None
        with open(f'Datos/Ventas.json', 'r') as file:
            data = json.load(file)

        datosVentas = data['ventas']
        for venta in datosVentas:
            item = Venta(venta['objeto'], venta['nivelNecesario'])
            for precio in venta['precio']:
                item.addListaPrecio([precio['objeto'], precio['cantidad']])

            listaVentas.append(item)

        forVenta = 0
        for venta in listaVentas:
            ventaObjeto = VentaObjeto(venta)
            uiVenta = ventaObjeto.getUI(150 + 250 * forVenta, 150, lista, listaUI, ui, clickeables, self)
            for uiObeject in uiVenta:
                info.append(uiObeject)

            forVenta += 1

        return info

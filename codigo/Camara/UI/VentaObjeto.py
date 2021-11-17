from codigo.Camara.UI.UIObject import UIObject
from codigo.Camara.UI.BotonVenta import BotonVenta
from codigo.Isla.Helper import Helper


class VentaObjeto:

    def __init__(self, venta):
        self.venta = venta
        self.objeto = venta.getObjeto()
        self.precio = venta.getListaPrecio()
        self.nivelNecesario = venta.getNivelNecesario()

    def getImageObjeto(self):
        if self.objeto == 'casa':
            return Helper.CASA

        elif self.objeto == 'muro':
            return Helper.MURO

        return Helper.ARBOL

    def getImagePrecio(self, objeto):
        if objeto == 'roca':
            return Helper.ROCA_OBJETO

        elif objeto == 'tronco':
            return Helper.TRONCO

        return Helper.SELECCIONADO

    def getObjeto(self):
        return self.objeto

    def getListaPrecios(self):
        return self.precio

    def getUI(self, posX, posY, lista, listaUI, ui, clickeables, objetoActualizar):
        card = []

        fondoObjeto = Helper.getSurface(200, 350)
        fondoObjeto.fill((102, 51, 0), None, 0)
        card.append(UIObject(fondoObjeto, posX, posY))

        font = Helper.FUENTE(20)
        textoInteligencia = font.render(f"Inteligencia : {self.nivelNecesario}", True, (255, 255, 255), None)
        card.append(UIObject(textoInteligencia, posX + 25, posY + 15))

        imagenObjeto = Helper.getImage(self.getImageObjeto(), 100, 100)
        card.append(UIObject(imagenObjeto, posX + 50, posY + 50))

        forPrecio = 0
        font = Helper.FUENTE(15)
        for precio in self.precio:
            imagenPrecio = Helper.getImage(self.getImagePrecio(precio[0]), 30, 30)
            card.append(UIObject(imagenPrecio, posX + 25 + 60 * forPrecio, posY + 190))

            textPrecio = font.render(f"{precio[1]}", True, (255, 255, 255), None)
            card.append(UIObject(textPrecio, posX + 30 + 60 * forPrecio, posY + 230))

            forPrecio += 1

        botonVenta = BotonVenta(None, posX + 20, posY + 275, lista, ui, self.venta, objetoActualizar)
        for uiObject in botonVenta.getUI(clickeables):
            card.append(uiObject)

        return card

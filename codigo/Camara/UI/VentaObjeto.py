from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class VentaObjeto:

    def __init__(self,objeto,precio,nivelNecesario):
        self.objeto = objeto
        self.precio = precio
        self.nivelNecesario = nivelNecesario

    def getImageObjeto(self):
        return self.objeto.getImage()

    def getImageObjeto(self):
        return self.objeto.getImage()

    def getObjeto(self):
        return self.objeto

    def getListaPrecios(self):
        return self.precio

    def getUI(self,posX,posY):
        ui = []

        fondoObjeto = Helper.getSurface(200, 300)
        fondoObjeto.fill((102, 51, 0), None, 0)
        ui.append(UIObject(fondoObjeto, posX, posY))

        imagenObjeto = Helper.getImage(self.objeto.getImage(),100,100)
        ui.append(UIObject(imagenObjeto,posX + 50,posY + 50))

        forPrecio = 0
        font = Helper.FUENTE(20)
        for precio in self.precio:
            imagenPrecio = Helper.getImage(precio[0].getImage(),50,50)
            ui.append(UIObject(imagenPrecio, posX + 40 + 70 * forPrecio, posY + 170))

            textPrecio = font.render(f"{precio[1]}", True, (255, 255, 255), None)
            ui.append(UIObject(textPrecio, posX + 50 + 75 * forPrecio, posY + 230))

            forPrecio += 1

        return ui
from codigo.Camara.UI.BotonIslaUI import BotonIslaUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class IslaObjeto:

    def __init__(self,isla,nivelNecesario,explorador,botonActivado):
        self.isla = isla
        self.nivelNecesario = nivelNecesario
        self.explorador = explorador
        self.botonActivado = botonActivado



    def getIslaNombre(self):
        return self.isla

    def getNivelNecesario(self):
        return self.nivelNecesario

    def getUI(self,posX,posY,listaUI,ui,clickeables):
        card = []

        fondoObjeto = Helper.getSurface(200, 300)
        fondoObjeto.fill((102, 51, 0), None, 0)
        card.append(UIObject(fondoObjeto, posX, posY))

        font = Helper.FUENTE(24)
        textPrecio = font.render(self.isla, True, (255, 255, 255), None)
        card.append(UIObject(textPrecio, posX +25, posY + 50))


        if self.botonActivado:
            boton = BotonIslaUI(None,posX + 25,posY + 200,listaUI,ui,self.isla,self.explorador)
            for uiBoton in boton.getUI(clickeables):
                card.append(uiBoton)

        return card
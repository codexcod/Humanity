from codigo.Camara.UI.BotonIslaUI import BotonIslaUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class IslaObjeto:

    def __init__(self,isla,nivelNecesario,explorador):
        self.isla = isla
        self.nivelNecesario = nivelNecesario
        self.explorador = explorador

    def getImageIsla(self):
        return self.isla.getImage()

    def getIsla(self):
        return self.isla

    def getNivelNecesario(self):
        return self.nivelNecesario

    def getUI(self,posX,posY,listaUI,ui,clickeables):
        card = []

        fondoObjeto = Helper.getSurface(200, 300)
        fondoObjeto.fill((102, 51, 0), None, 0)
        card.append(UIObject(fondoObjeto, posX, posY))

        imagenObjeto = Helper.getImage(self.isla.getImage(),100,100)
        card.append(UIObject(imagenObjeto,posX + 50,posY + 50))

        boton = BotonIslaUI(None,posX + 25,posY + 200,listaUI,ui,self.isla,self.explorador)
        for uiBoton in boton.getUI(clickeables):
            card.append(uiBoton)

        return card
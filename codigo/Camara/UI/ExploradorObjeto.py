from codigo.Camara.UI.ActividadUI import ActividadUI
from codigo.Camara.UI.BotonExplorador import BotonExplorador
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class ExploradorObjeto:

    def __init__(self, explorador):
        self.explorador = explorador

    def getUI(self, posX, posY, lista, listaUI, ui, clickeables, objetoActualizar):
        card = []

        fondoPersonas = Helper.getSurface(260, 120)
        fondoPersonas.fill((102, 51, 0), None, 0)
        card.append(UIObject(fondoPersonas, posX, posY))

        persona = self.explorador
        imagenPersona = Helper.getImage(persona.getImage(), 100, 100)
        card.append(UIObject(imagenPersona, posX, posY + 10))

        font = Helper.FUENTE(25)
        nombrePersona = font.render(persona.getNombre(), True, (255, 255, 255), None)
        card.append(UIObject(nombrePersona, posX + 100, posY + 10))

        fondoBoton = Helper.getSurface(140, 40)
        if objetoActualizar.getExplorador() == self.explorador:
            fondoBoton.fill((0, 255, 0), None, 0)

        else:
            fondoBoton.fill((255, 0, 0), None, 0)

        card.append(UIObject(fondoBoton, posX + 100, posY + 50))

        fuenteActividad = Helper.FUENTE(18)
        if objetoActualizar.getExplorador() == self.explorador:
            textoExplorador = fuenteActividad.render("Seleccionado", True, (255, 255, 255), None)

        else:
            textoExplorador = fuenteActividad.render("Seleccionar", True, (255, 255, 255), None)

        botonActividad = BotonExplorador(textoExplorador, posX + 130, posY + 50, lista, persona, ui, objetoActualizar)
        card.append(UIObject(textoExplorador, posX + 110, posY + 60))
        clickeables.append(botonActividad)

        return card

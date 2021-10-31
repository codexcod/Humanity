from codigo.Camara.UI.ActividadUI import ActividadUI
from codigo.Camara.UI.UIObject import UIObject
from codigo.Isla.Helper import Helper


class ExploradorObjeto:

    def __init__(self,explorador):
        self.explorador = explorador


    def getUI(self,posX,posY,lista,listaUI,ui,clickeables,objetoActualizar):
        card = []

        fondoPersonas = Helper.getSurface(300, 120)
        fondoPersonas.fill((102, 51, 0), None, 0)
        card.append(UIObject(fondoPersonas, posX, posY))

        persona = self.explorador
        imagenPersona = Helper.getImage(persona.getImage(), 100, 100)
        card.append(UIObject(imagenPersona, posX, posY + 10))

        font = Helper.FUENTE(25)
        nombrePersona = font.render(persona.getNombre(), True, (255, 255, 255), None)
        card.append(UIObject(nombrePersona, posX + 100, posY + 10))

        fondoActividad = Helper.getSurface(150, 40)
        fondoActividad.fill(Helper.getActividad(persona.getBusqueda())[0], None, 0)
        card.append(UIObject(fondoActividad, posX + 100, posY + 50))

        fuenteActividad = Helper.FUENTE(18)
        actividad = fuenteActividad.render(Helper.getActividad(persona.getBusqueda())[1], True, (255, 255, 255), None)
        botonActividad = ActividadUI(actividad,posX + 160, posY + 70, lista, persona, ui, objetoActualizar)
        card.append(UIObject(actividad, posX + 130, posY + 70))
        clickeables.append(botonActividad)

        return card

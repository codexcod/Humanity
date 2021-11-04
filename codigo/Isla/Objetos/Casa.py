from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto
from codigo.Camara.UI.UIObject import UIObject
from codigo.Camara.UI.ActividadUI import ActividadUI
from codigo.Camara.UI.FlechaUI import FlechaUI


class Casa(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.aldea = aldea
        self.personas = []
        self.image = Helper.CASA
        self.nombre = "Casa"
        self.numeroListaPersonas = 2

    def toJson(self):
        jsonText = {
            'objeto': 'Casa',
            'name': self.nombre,
            'aldea': self.aldea.getNombre(),
            'x': self.x,
            'y': self.y,
            'personas': []
        }
        for persona in self.personas:
            jsonText['personas'].append(persona.toJson())

        return jsonText

    def getUI(self,clickeables,lista,listaUI,ui):
        info = []
        fondo = Helper.getSurface(800,500)
        fondo.fill((128, 64, 0), None, 0)
        info.append(UIObject(fondo, 100, 50))
        font = Helper.FUENTE(25)
        texto = self.getInfoStr()
        lineas = texto.splitlines()
        forI = 0 
        for i in lineas:
            textObject = font.render(i, True, (255, 255, 255), None)
            info.append(UIObject(textObject, 450, 75 + forI * 40))
            forI += 1
        
        
        image = Helper.getImage(self.getImage(),200, 200)
        info.append(UIObject(image, 175, 200))

        forPersona = 0
        for numPersona in range(self.numeroListaPersonas - 2, self.numeroListaPersonas):
            if not self.getPersonas()[numPersona] is None:
                fondoPersonas = Helper.getSurface(400,140)
                fondoPersonas.fill((102,51, 0), None, 0)
                info.append(UIObject(fondoPersonas, 450 , 165 + 180 * forPersona))

                persona = self.getPersonas()[numPersona]
                imagenPersona = Helper.getImage(persona.getImage(),120,120)
                info.append(UIObject(imagenPersona, 450 , 175 + 180 * forPersona))

                nombrePersona = font.render(persona.getNombre(), True, (255, 255, 255), None)
                info.append(UIObject(nombrePersona, 600 , 175 + 180 * forPersona))

                fondoActividad = Helper.getSurface(200,70)
                fondoActividad.fill(Helper.getActividad(persona.getBusqueda())[0], None, 0)
                info.append(UIObject(fondoActividad, 600 , 215 + 180 * forPersona))

                fuenteActividad = Helper.FUENTE(18)
                actividad = fuenteActividad.render(Helper.getActividad(persona.getBusqueda())[1], True, (255, 255, 255), None)
                botonActividad = ActividadUI(actividad, 615 , 230 + 180 * forPersona,lista,persona,ui,self)
                info.append(UIObject(actividad, 610 , 235 + 180 * forPersona))
                clickeables.append(botonActividad)


            forPersona += 1

        flechaArriba = FlechaUI(Helper.getImage(Helper.FLECHA_ARRIBA,50,50), 650 , 110,lista,ui,self,-1)
        info.append(flechaArriba)
        clickeables.append(flechaArriba)

        flechaAbajo = FlechaUI(Helper.getImage(Helper.FLECHA_ABAJO,50,50), 650 , 490,lista,ui,self,1)
        info.append(flechaAbajo)
        clickeables.append(flechaAbajo)

            
        
        return info

    def agregarPersona(self, persona):
        # Agrega una persona a la casa
        self.personas.append(persona)
        self.aldea.agregarPersona(persona)

    def getInfoStr(self):
        result = "Casa de :"

        return result

    def getAldea(self):
        return self.aldea

    def isCasa(self):
        return True

    def getPersonas(self):
        return self.personas

    def sumarListaObjetos(self,suma):
        self.numeroListaPersonas += suma
        if self.numeroListaPersonas > len(self.aldea.getPersonas()) - 2:
            self.numeroListaPersonas = 2

        elif self.numeroListaPersonas < 2:
            self.numeroListaPersonas = len(self.aldea.getPersonas()) - 2

    def isCasa(self):
        return True

from codigo.Isla.Helper import Helper
from codigo.Isla.Objetos.Objeto import Objeto


class Casa(Objeto):

    def __init__(self, aldea, x, y, isla):
        Objeto.__init__(self, x, y, isla)
        self.aldea = aldea
        self.personas = []
        self.image = Helper.CASA
        self.nombre = "Casa"

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

    def agregarPersona(self, persona):
        self.personas.append(persona)
        self.aldea.agregarPersona(persona)

    def getInfoStr(self):
        result = f"Aldea {self.aldea.getNombre()}  \n"
        result += "Casa de : \n"
        for persona in self.personas:
            result += f"{persona.getNombre()} \n"

        return result

    def getAldea(self):
        return self.aldea

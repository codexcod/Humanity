

class Aldea:

    def __init__(self, nombre):
        self.nombre = nombre
        self.troncos = 0
        self.piedras = 0
        self.carne = 0
        self.oro = 0
        self.casas = []
        self.personas = []
        self.inteligencia = 0

    def toJson(self):
        jsonText = {
            'objeto' : 'Aldea',
            'name' : self.nombre,
            'piedras' : self.piedras,
            'troncos': self.troncos,
            'oro': self.oro,
            'carne': self.carne,
            'casas' : [],
            'inteligencia' : self.inteligencia
        }

        for casa in self.casas:
            jsonText['casas'].append(casa.toJson())

        return jsonText


    def getInteligencia(self):
        return self.inteligencia

    def setInteligencia(self,inteligencia):
        self.inteligencia = inteligencia

    def sumarInteligencia(self,inteligencia):
        self.inteligencia += inteligencia

    def getNombre(self):
        return self.nombre

    def getMadera(self):
        return self.troncos

    def setMadera(self, troncos):
        self.troncos = troncos

    def getPiedra(self):
        return self.piedras

    def setPiedra(self, piedras):
        self.piedras = piedras

    def getCarne(self):
        return self.carne

    def setCarne(self, carne):
        self.carne = carne

    def setOro(self, oro):
        self.oro = oro

    def agregarCasa(self, casa):
        self.casas.append(casa)

    def agregarPersona(self, persona):
        self.personas.append(persona)

    def getPersonas(self):
        return self.personas

    def añadirObjeto(self, objeto):
        if objeto.getNombre() == "Tronco":
            self.troncos += 1
            return True

        elif objeto.getNombre() == "Roca":
            self.piedras += 1
            return True

        elif objeto.getNombre() == "Carne":
            self.carne += 1
            return True

        return False

    def tieneComida(self):
        return self.carne >= 1

    def conseguirComida(self):
        self.carne -= 1

    
import random

from codigo.Isla.Aldea import Aldea
from codigo.Isla.Estaticos.Agua import Agua
from codigo.Isla.Estaticos.Arena import Arena
from codigo.Isla.Estaticos.Pasto import Pasto
from codigo.Isla.Helper import Helper
from codigo.Isla.Herramientas.Pico import Pico
from codigo.Isla.Movibles.Persona import Persona
from codigo.Isla.NoiseGenerator import NoiseGenerator
from codigo.Isla.Objetos.Arbol import Arbol
from codigo.Isla.Objetos.Barco import Barco
from codigo.Isla.Objetos.Arbusto import Arbusto
from codigo.Isla.Objetos.Carne import Carne
from codigo.Isla.Objetos.Casa import Casa
from codigo.Isla.Objetos.Fogata import Fogata
from codigo.Isla.Objetos.MesaTrabajo import MesaTrabajo
from codigo.Isla.Objetos.Piedra import Piedra
from codigo.Isla.Movibles.conejo import Conejo
from codigo.Isla.Movibles.Jabali import Jabali
from codigo.Isla.Movibles.Vaca import Vaca
from codigo.Isla.Objetos.Muro import Muro

import json

from codigo.Isla.Objetos.Roca import Roca
from codigo.Isla.Objetos.Tronco import Tronco


class Isla:

    def obj_dict(obj):
        return obj.__dict__

    def __init__(self):
        self.mEstatico = []
        self.mMovible = []
        self.mObjetos = []
        self.ancho = 0
        self.animales = []
        self.altura = 0
        self.arbolesTalados = []
        self.arbustosSinBaya = []
        self.aldea = None
        self.image = None
        self.nombre = ""

    def generarIsla(self, ancho, altura):
        self.altura = altura
        self.ancho = ancho
        self.generarMapaObjetos()
        self.generarMapaEstaticoConocido()
        self.generarMapaMovible()

    def generarIslaDesconocida(self, ancho, altura):
        self.altura = altura
        self.ancho = ancho
        self.generarMapaObjetos()
        self.generarMapaEstaticoDesconocido()
        self.generarMapaMovible()

    def cargarMapa(self, partida):
        with open(f'Info/{partida}.json', 'r') as file:
            data = json.load(file)

        self.ancho = data['ancho']
        self.altura = data['altura']

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mObjetos.append(fila)

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mMovible.append(fila)

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mEstatico.append(fila)

        for objeto in data['visibilidad']:
            if objeto['objeto'] == 'Pasto':
                pasto = Pasto(objeto['y'], objeto['x'])
                pasto.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = pasto

            if objeto['objeto'] == 'Arena':
                arena = Arena(objeto['y'], objeto['x'])
                arena.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = arena

            if objeto['objeto'] == 'Agua':
                agua = Agua(objeto['y'], objeto['x'])
                agua.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = agua

        self.nombre = data['nombre']
        jsonAldea = data['aldea']

        aldea = Aldea(jsonAldea['name'])
        aldea.setMadera(jsonAldea['troncos'])
        aldea.setPiedra(jsonAldea['piedras'])
        aldea.setCarne(jsonAldea['carne'])
        aldea.setOro(jsonAldea['oro'])
        aldea.setInteligencia(jsonAldea['inteligencia'])
        for casa in jsonAldea['casas']:
            nuevaCasa = Casa(aldea, casa['x'], casa['y'], self)
            for persona in casa['personas']:
                nuevaPersona = Persona(persona['name'], nuevaCasa, persona['x'], persona['y'], self)
                nuevaPersona.setEdad(persona['edad'])
                nuevaPersona.setHambre(persona['hambre'])

                for objeto in persona['inventario']:
                    if objeto['objeto'] == 'Tronco':
                        nuevaPersona.agregarInventario(Tronco())

                    elif objeto['objeto'] == 'Roca':
                        nuevaPersona.agregarInventario(Roca())

                    elif objeto['objeto'] == 'Carne':
                        nuevaPersona.agregarInventario(Carne())

                    elif objeto['objeto'] == 'Pico':
                        pico = Pico()
                        pico.setUsos(objeto['usos'])
                        pico.setRota(objeto['rota'])
                        if pico.getRota():
                            pico.setImage(Helper.PICO_ROTO)

                        nuevaPersona.agregarInventario(pico)

                if not persona['herramienta'] is None:
                    nuevaPersona.setHerramienta(persona['herramienta'])

                nuevaCasa.agregarPersona(nuevaPersona)
                self.mMovible[persona['y']][persona['x']] = nuevaPersona

            aldea.agregarCasa(nuevaCasa)
            self.mObjetos[casa['y']][casa['x']] = nuevaCasa

        self.aldea = aldea

        jsonAnimales = data['animales']
        for animal in jsonAnimales:
            if animal['objeto'] == 'Vaca':
                vaca = Vaca(animal['x'], animal['y'], self, animal['vida'])
                vaca.setMuerto(animal['muerto'])
                if vaca.getMuerto():
                    vaca.setImage(Helper.VACA(4))
                self.animales.append(vaca)
                self.mMovible[animal['y']][animal['x']] = vaca

            elif animal['objeto'] == 'Conejo':
                conejo = Conejo(animal['x'], animal['y'], self, animal['vida'])
                conejo.setMuerto(animal['muerto'])
                if conejo.getMuerto():
                    conejo.setImage(Helper.CONEJO(14))
                self.animales.append(conejo)
                self.mMovible[animal['y']][animal['x']] = conejo

            elif animal['objeto'] == 'Jabali':
                jabali = Jabali(animal['x'], animal['y'], self, animal['vida'])
                jabali.setMuerto(animal['muerto'])
                if jabali.getMuerto():
                    jabali.setImage(Helper.JABALI(5))

                self.animales.append(jabali)
                self.mMovible[animal['y']][animal['x']] = jabali

        for objeto in data['mObjetos']:
            if objeto['objeto'] == 'Arbol':
                arbol = Arbol(objeto['x'], objeto['y'], self)
                arbol.setTroncos(objeto['troncos'])
                arbol.setTalado(objeto['talado'])
                arbol.setTiempoCrecimiento(objeto['tiempoCrecimiento'])
                if arbol.getTalado():
                    self.arbolesTalados.append(arbol)
                    arbol.setImage(Helper.ARBOL_TALADO)
                    arbol.setCaminable(True)
                self.mObjetos[objeto['y']][objeto['x']] = arbol
                arbol.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Piedra':
                piedra = Piedra(objeto['x'], objeto['y'], self)
                piedra.setPiedras(objeto['piedras'])
                piedra.setOro(objeto['oro'])
                self.mObjetos[objeto['y']][objeto['x']] = piedra
                piedra.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Arbusto':
                arbusto = Arbusto(objeto['x'], objeto['y'], self)
                arbusto.setBayas(objeto['bayas'])
                arbusto.setTalado(objeto['talado'])
                arbusto.setTiempoCrecimiento(objeto['tiempoCrecimiento'])
                arbusto.setNombre(objeto['name'])
                self.mObjetos[objeto['y']][objeto['x']] = arbusto

            elif objeto['objeto'] == 'Fogata':
                fogata = Fogata(self.aldea, objeto['x'], objeto['y'], self)
                self.mObjetos[objeto['y']][objeto['x']] = fogata
                fogata.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Mesa de trabajo':
                mesaDeTrabajo = MesaTrabajo(self.aldea, objeto['x'], objeto['y'], self)
                self.mObjetos[objeto['y']][objeto['x']] = mesaDeTrabajo
                mesaDeTrabajo.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Barco':
                barco = Barco(objeto['x'], objeto['y'], self)
                barco.setNombre(objeto['name'])
                self.mObjetos[objeto['y']][objeto['x']] = barco

            elif objeto['objeto'] == 'Muro':
                muro = Muro(objeto['x'], objeto['y'], self)
                muro.setNombre(objeto['name'])
                self.mObjetos[objeto['y']][objeto['x']] = muro

    def cargarMapaConArchivo(self, archivo):

        data = archivo

        self.ancho = data['ancho']
        self.altura = data['altura']

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mObjetos.append(fila)

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mMovible.append(fila)

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mEstatico.append(fila)

        for objeto in data['visibilidad']:
            if objeto['objeto'] == 'Pasto':
                pasto = Pasto(objeto['y'], objeto['x'])
                pasto.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = pasto

            if objeto['objeto'] == 'Arena':
                arena = Arena(objeto['y'], objeto['x'])
                arena.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = arena

            if objeto['objeto'] == 'Agua':
                agua = Agua(objeto['y'], objeto['x'])
                agua.setVisivilidad(objeto['visibilidad'])
                self.mEstatico[objeto['y']][objeto['x']] = agua

        self.nombre = data['nombre']
        jsonAldea = data['aldea']

        if not jsonAldea is None:
            aldea = Aldea(jsonAldea['name'])
            aldea.setMadera(jsonAldea['troncos'])
            aldea.setPiedra(jsonAldea['piedras'])
            aldea.setCarne(jsonAldea['carne'])
            aldea.setOro(jsonAldea['oro'])
            aldea.setInteligencia(jsonAldea['inteligencia'])
            for casa in jsonAldea['casas']:
                nuevaCasa = Casa(aldea, casa['x'], casa['y'], self)
                for persona in casa['personas']:
                    nuevaPersona = Persona(persona['name'], nuevaCasa, persona['x'], persona['y'], self)
                    nuevaPersona.setEdad(persona['edad'])
                    nuevaPersona.setHambre(persona['hambre'])

                    for objeto in persona['inventario']:
                        if objeto['objeto'] == 'Tronco':
                            nuevaPersona.agregarInventario(Tronco())

                        elif objeto['objeto'] == 'Roca':
                            nuevaPersona.agregarInventario(Roca())

                        elif objeto['objeto'] == 'Carne':
                            nuevaPersona.agregarInventario(Carne())

                        elif objeto['objeto'] == 'Pico':
                            pico = Pico()
                            pico.setUsos(objeto['usos'])
                            pico.setRota(objeto['rota'])
                            if pico.getRota():
                                pico.setImage(Helper.PICO_ROTO)

                            nuevaPersona.agregarInventario(pico)

                    if not persona['herramienta'] is None:
                        nuevaPersona.setHerramienta(persona['herramienta'])

                    nuevaCasa.agregarPersona(nuevaPersona)
                    self.mMovible[persona['y']][persona['x']] = nuevaPersona

                aldea.agregarCasa(nuevaCasa)
                self.mObjetos[casa['y']][casa['x']] = nuevaCasa

            self.aldea = aldea

        jsonAnimales = data['animales']
        for animal in jsonAnimales:
            if animal['objeto'] == 'Vaca':
                vaca = Vaca(animal['x'], animal['y'], self, animal['vida'])
                vaca.setMuerto(animal['muerto'])
                if vaca.getMuerto():
                    vaca.setImage(Helper.VACA(4))
                self.animales.append(vaca)
                self.mMovible[animal['y']][animal['x']] = vaca

            elif animal['objeto'] == 'Conejo':
                conejo = Conejo(animal['x'], animal['y'], self, animal['vida'])
                conejo.setMuerto(animal['muerto'])
                if conejo.getMuerto():
                    conejo.setImage(Helper.CONEJO(14))
                self.animales.append(conejo)
                self.mMovible[animal['y']][animal['x']] = conejo

            elif animal['objeto'] == 'Jabali':
                jabali = Jabali(animal['x'], animal['y'], self, animal['vida'])
                jabali.setMuerto(animal['muerto'])
                if jabali.getMuerto():
                    jabali.setImage(Helper.JABALI(5))

                self.animales.append(jabali)
                self.mMovible[animal['y']][animal['x']] = jabali

        for objeto in data['mObjetos']:
            if objeto['objeto'] == 'Arbol':
                arbol = Arbol(objeto['x'], objeto['y'], self)
                arbol.setTroncos(objeto['troncos'])
                arbol.setTalado(objeto['talado'])
                arbol.setTiempoCrecimiento(objeto['tiempoCrecimiento'])
                if arbol.getTalado():
                    self.arbolesTalados.append(arbol)
                    arbol.setImage(Helper.ARBOL_TALADO)
                    arbol.setCaminable(True)
                self.mObjetos[objeto['y']][objeto['x']] = arbol
                arbol.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Piedra':
                piedra = Piedra(objeto['x'], objeto['y'], self)
                piedra.setPiedras(objeto['piedras'])
                piedra.setOro(objeto['oro'])
                self.mObjetos[objeto['y']][objeto['x']] = piedra
                piedra.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Arbusto':
                arbusto = Arbusto(objeto['x'], objeto['y'], self)
                arbusto.setBayas(objeto['bayas'])
                arbusto.setTalado(objeto['talado'])
                arbusto.setTiempoCrecimiento(objeto['tiempoCrecimiento'])
                arbusto.setNombre(objeto['name'])
                self.mObjetos[objeto['y']][objeto['x']] = arbusto

            elif objeto['objeto'] == 'Fogata':
                fogata = Fogata(self.aldea, objeto['x'], objeto['y'], self)
                self.mObjetos[objeto['y']][objeto['x']] = fogata
                fogata.setNombre(objeto['name'])

            elif objeto['objeto'] == 'Mesa de trabajo':
                mesaDeTrabajo = MesaTrabajo(self.aldea, objeto['x'], objeto['y'], self)
                self.mObjetos[objeto['y']][objeto['x']] = mesaDeTrabajo
                mesaDeTrabajo.setNombre(objeto['name'])

    def toJsonPath(self, partida):
        jsonText = {}
        jsonText['nombre'] = self.nombre

        if not self.aldea is None:
            jsonText['aldea'] = self.aldea.toJson()

        else:
            jsonText['aldea'] = self.aldea

        jsonText['ancho'] = self.ancho
        jsonText['altura'] = self.altura
        jsonText['visibilidad'] = []
        for y in range(self.altura):
            for x in range(self.ancho):
                jsonText['visibilidad'].append(self.mEstatico[y][x].toJson())

        jsonText['mObjetos'] = []
        for y in range(self.altura):
            for x in range(self.ancho):
                if not self.mObjetos[y][x] is None:
                    jsonText['mObjetos'].append(self.mObjetos[y][x].toJson())

        jsonText['animales'] = []
        for animal in self.animales:
            jsonText['animales'].append(animal.toJson())

        with open(partida, 'w') as file:
            json.dump(jsonText, file, indent=4)

    def toJson(self, partida):
        jsonText = {}
        jsonText['nombre'] = self.nombre

        jsonText['aldea'] = self.aldea.toJson()

        jsonText['ancho'] = self.ancho
        jsonText['altura'] = self.altura
        jsonText['visibilidad'] = []
        for y in range(self.altura):
            for x in range(self.ancho):
                jsonText['visibilidad'].append(self.mEstatico[y][x].toJson())

        jsonText['mObjetos'] = []
        for y in range(self.altura):
            for x in range(self.ancho):
                if not self.mObjetos[y][x] is None:
                    jsonText['mObjetos'].append(self.mObjetos[y][x].toJson())

        jsonText['animales'] = []
        for animal in self.animales:
            jsonText['animales'].append(animal.toJson())

        with open(f'Info/{partida}.json', 'w') as file:
            json.dump(jsonText, file, indent=4)

    def generarMapaEstaticoConocido(self):
        # Genera el mapa de fondo como la tierra
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if x == 1 or y == 1 or x == self.ancho - 1 or y == self.altura - 1:
                    fila.append(Agua(x, y))
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None

                elif x == 2 or x == 3 or y == 2 or y == 3 or x == self.ancho - 2 or y == self.altura - 2 or x == self.ancho - 3 or y == self.altura - 3:

                    fila.append(Arena(x, y))
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None


                else:
                    fila.append(Pasto(x, y))

                fila[len(fila) - 1].setVisivilidad(True)

            self.mEstatico.append(fila)

    def generarMapaEstaticoDesconocido(self):
        # Genera el mapa de fondo como la tierra
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if x == 1 or y == 1 or x == self.ancho - 1 or y == self.altura - 1:
                    fila.append(Agua(x, y))
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None

                elif x == 2 or x == 3 or y == 2 or y == 3 or x == self.ancho - 2 or y == self.altura - 2 or x == self.ancho - 3 or y == self.altura - 3:

                    fila.append(Arena(x, y))
                    if not self.mObjetos[y][x] is None:
                        self.mObjetos[y][x] = None


                else:
                    fila.append(Pasto(x, y))

            self.mEstatico.append(fila)

    def generarMapaObjetos(self):
        # Genera el mapa en el cual entran los arboles y piedras
        arboles = NoiseGenerator(self.ancho, self.altura, None, Arbol(0, 0, self), 0.5)
        mArboles = arboles.getNoise()

        arbustos = NoiseGenerator(self.ancho, self.altura, None, Arbusto(0, 0, self), 0.05)
        mArbustos = arbustos.getNoise()

        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                if not mArboles[y][x] is None:
                    mArboles[y][x] = Arbol(x, y, self)
                    mArboles[y][x].setTroncos(random.randrange(5, 20))
                    fila.append(mArboles[y][x])

                elif random.randrange(1, 50) == 1:
                    piedra = Piedra(x, y, self)
                    piedra.setPiedras(random.randrange(5, 20))
                    if random.randrange(1, 30) == 1:
                        piedra.setOro(random.randrange(1, 3))

                    fila.append(piedra)

                elif not mArbustos[y][x] is None:
                    mArbustos[y][x] = Arbusto(x, y, self)
                    mArbustos[y][x].setBayas(random.randrange(1, 10))
                    fila.append(mArbustos[y][x])

                else:
                    fila.append(mArboles[y][x])

            self.mObjetos.append(fila)

    def generarMapaMovible(self):
        # Genera el mapa por el cual se mueven las personas y los animales
        for y in range(self.altura):
            fila = []
            for x in range(self.ancho):
                fila.append(None)

            self.mMovible.append(fila)

        for y in range(self.altura):
            for x in range(self.ancho):
                if self.getMapaObjetos()[y][x] is None:
                    if random.randrange(1, 1500) == 1:
                        claseDeAnimal = random.choice([0, 1, 2])
                        if claseDeAnimal == 0:
                            self.crearGrupoDeAnimales(5, x, y, "conejo")

                        elif claseDeAnimal == 1:
                            self.crearGrupoDeAnimales(5, x, y, "vaca")

                        elif claseDeAnimal == 2:
                            self.crearGrupoDeAnimales(3, x, y, "jabali")

    def getMapaEstatico(self):
        return self.mEstatico

    def getMapaObjetos(self):
        return self.mObjetos

    def getMapaMovible(self):
        return self.mMovible

    def getAncho(self):
        return self.ancho

    def getAltura(self):
        return self.altura

    def agregarObjeto(self, x, y, objeto):
        """
        if not self.mObjetos[y][x] is None:
            
            return True
        
        return False"""
        self.mObjetos[y][x] = objeto

    def agregarMovible(self, x, y, objeto):
        """
        if not self.mObjetos[y][x] is None:

            return True

        return False"""
        self.mMovible[y][x] = objeto

    def moverMovible(self, x, y, difX, difY):
        if not self.mMovible[y][x] is None:
            self.mMovible[y + difY][x + difX] = self.mMovible[y][x]
            self.mMovible[y][x] = None

    def agregarAldea(self, aldea, posX, posY, heroe, explorador):
        for y in range(posY - 5, posY + 5):
            for x in range(posX - 5, posX + 5):
                self.mObjetos[y][x] = None

        # crear el heroe, el explorador y a gonza
        self.aldea = aldea
        casa = Casa(aldea, posX, posY - 2, self)
        self.agregarObjeto(posX, posY - 2, casa)
        aldea.agregarCasa(casa)
        # HEROE
        heroe = Persona(heroe, casa, posX - 3, posY, self)
        self.agregarMovible(heroe.getX(), heroe.getY(), heroe)
        casa.agregarPersona(heroe)
        # EXPLORADOR
        explorador = Persona(explorador, casa, posX + 3, posY, self)
        self.agregarMovible(explorador.getX(), explorador.getY(), explorador)
        casa.agregarPersona(explorador)
        # Crea fogata
        fogata = Fogata(aldea, posX, posY, self)
        self.agregarObjeto(posX, posY, fogata)
        # Crea Mesa de Trabajo
        mesaDeTrabajo = MesaTrabajo(aldea, posX, posY + 2, self)
        self.agregarObjeto(posX, posY + 2, mesaDeTrabajo)
        # Crea a Darwin
        Darwin = Jabali(posX + 4, posY, self, 100000)
        self.agregarMovible(Darwin.getX(), Darwin.getY(), Darwin)
        Darwin.setNombre("Darwin")
        self.animales.append(Darwin)

        barco = Barco(self.ancho // 2, self.altura - 1, self)
        self.agregarObjeto(self.ancho // 2, self.altura - 1, barco)

    def getArbolesTalados(self):
        return self.arbolesTalados

    def getArbustosSinBayas(self):
        return self.arbustosSinBaya

    def getAnimales(self):
        return self.animales

    def crearGrupoDeAnimales(self, numero, x, y, animal):
        if animal == "conejo":
            for i in range(numero):
                aleatorioX = random.randrange(-3, 3)
                aleatorioY = random.randrange(-3, 3)
                while x + aleatorioX >= self.ancho or x + aleatorioX <= 0:
                    aleatorioX = random.randrange(-3, 3)

                while y + aleatorioY >= self.altura or y + aleatorioY <= 0:
                    aleatorioY = random.randrange(-3, 3)

                if self.getMapaMovible()[y + aleatorioY][x + aleatorioX] is None and \
                        self.getMapaObjetos()[y + aleatorioY][x + aleatorioX] is None:
                    conejo = Conejo(x + aleatorioX, y + aleatorioY, self, 10)
                    self.agregarMovible(conejo.getX(), conejo.getY(), conejo)
                    self.animales.append(conejo)

        elif animal == "vaca":
            for i in range(numero):
                aleatorioX = random.randrange(-6, 6)
                aleatorioY = random.randrange(-6, 6)
                while x + aleatorioX >= self.ancho or x + aleatorioX <= 0:
                    aleatorioX = random.randrange(-6, 6)

                while y + aleatorioY >= self.altura or y + aleatorioY <= 0:
                    aleatorioY = random.randrange(-6, 6)

                if self.getMapaMovible()[y + aleatorioY][x + aleatorioX] is None and \
                        self.getMapaObjetos()[y + aleatorioY][x + aleatorioX] is None:
                    vaca = Vaca(x + aleatorioX, y + aleatorioY, self, 15)
                    self.agregarMovible(vaca.getX(), vaca.getY(), vaca)
                    self.animales.append(vaca)

        elif animal == "jabali":
            for i in range(numero):
                aleatorioX = random.randrange(-6, 6)
                aleatorioY = random.randrange(-6, 6)
                while x + aleatorioX >= self.ancho or x + aleatorioX <= 0:
                    aleatorioX = random.randrange(-6, 6)

                while y + aleatorioY >= self.altura or y + aleatorioY <= 0:
                    aleatorioY = random.randrange(-6, 6)

                if self.getMapaMovible()[y + aleatorioY][x + aleatorioX] is None and \
                        self.getMapaObjetos()[y + aleatorioY][x + aleatorioX] is None:
                    jabali = Jabali(x + aleatorioX, y + aleatorioY, self, 15)
                    self.agregarMovible(jabali.getX(), jabali.getY(), jabali)
                    self.animales.append(jabali)

    def getAldea(self):
        return self.aldea

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def setNombre(self, nombre):
        self.nombre = nombre

    def enviarViajero(self, explorador):
        self.mMovible[explorador.getY()].remove(explorador)

    def agregarViajero(self, explorador):
        explorador.setX(self.ancho // 2)
        explorador.setY(self.altura - 2)
        explorador.setIsla(self)
        self.mMovible[self.altura - 2][self.ancho // 2] = explorador
        explorador.descubrir()
        self.mObjetos[self.altura - 1][self.ancho // 2] = Barco(self.ancho // 2, self.altura - 1, self)

    def getNombre(self):
        return self.nombre
import sys
from typing import Text

# Hay que cambiar el path para que detecte bien o usar pycharm y poner add content root to PYTHONPATH


path = sys.path[0]
sys.path.append(path[:len(path) - 7])

import pygame
import os
from os import remove
from pygame import mixer
from codigo.Controlador import Controlador
from codigo.MenuControlador import ControladorMenu
from codigo.Isla.Isla import Isla
from codigo.Camara.Camara import Camara
from codigo.Camara.UI.UI import UI
from codigo.Camara.Zoom import Zoom
from codigo.Camara.Mouse import Mouse
from codigo.CargarPartidaControlador import CargarPartidaControlador
from codigo.Controlador import Controlador
from codigo.Isla.Isla import Isla
from codigo.Camara.Zoom import Zoom
from codigo.Camara.UI.UI import UI
from codigo.Camara.Camara import Camara
from codigo.Camara.Mouse import Mouse
from codigo.Isla.Aldea import Aldea


def conseguirPartidas():
        #Meter los archivos de "Info" en "archivos"
        archivos = os.listdir("Info")
        #Buscar las partidas que hay
        partidas = []
        for partida in archivos:
            partes = partida.split(".")
            partidas.append(partes[0])

        return partidas

        

pygame.init()
mixer.init()

menu = input("Desea cargar una partida(G) o crear una(C)? ")

if menu == "g" or menu == "G":
    print("estas son las partidas disponibles: ")
    for partida in conseguirPartidas():
        print(f"Partida : {partida}")

    partidaSeleccionada = input("complete el nombre de la partida que desea cargar: ") 
    if partidaSeleccionada in conseguirPartidas():
        isla = Isla()
        isla.cargarMapa(partidaSeleccionada)
        ancho = isla.getAncho()
        altura = isla.getAltura()
        aldea = isla.getAldea()

        # Camara para controlar el zoom
        camara = Camara(ancho // 2, altura // 2, isla, Zoom.NORMAL_ZOOM, UI())
        mouse = Mouse(camara)

        controlador = Controlador(isla, camara, partidaSeleccionada)
        controlador.run()

    else:
        print("partida no encontrada")

else:
    ancho = 400
    alto = 400
    print("para crear una nueva partida complete los siguientes campos : ")
    nombreAldea = input("Ingrese el nombre de su aldea :")
    heroe = input("Ingrese el nombre de su heroe :")
    explorador = input("Ingrese el nombre de su explorador :")
    partida = input("Ingrese el nombre de su partida: ")
    isla = Isla()
    isla.generarIsla(ancho, alto)
    isla.setNombre(partida)
    aldea = Aldea(nombreAldea)
    isla.agregarAldea(aldea, ancho // 2, alto // 2, heroe, explorador)

    # Camara para controlar el zoom
    camara = Camara(ancho // 2, alto // 2, isla, Zoom.NORMAL_ZOOM, UI())
    mouse = Mouse(camara)

    controlador = Controlador(isla, camara, partida)
    controlador.run()
    





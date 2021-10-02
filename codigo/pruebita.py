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

pygame.init()
mixer.init()


def menu():
    controlador = ControladorMenu()
    controlador.run()
    

def Islasini():
    controladorCargarPartida = CargarPartidaControlador()
    if controladorCargarPartida.run():
        Islasini()

Islasini()
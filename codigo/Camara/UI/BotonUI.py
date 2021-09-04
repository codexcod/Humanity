from codigo.Camara.UI.UIObject import UIObject

from codigo.Isla.Helper import Helper
import pygame

class BotonUI(UIObject):

    def __init__(self, posX, posY):
        self.objeto = pygame.transform.scale(Helper.PAUSAR, (50, 50))
        super().__init__(self.objeto, posX, posY)

        
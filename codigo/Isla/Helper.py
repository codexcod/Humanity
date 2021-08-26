import pygame


class Helper:
    AGUA = pygame.image.load('../img/agua.jpg')
    PASTO = pygame.image.load('../img/pasto.jpg')
    ARENA = pygame.image.load('../img/arena.jpg')
    ARBOL = pygame.image.load('../img/arbol.png')
    ARBOL_GRANDE = pygame.image.load('../img/arbol_grande.png')
    ARBOL_TALADO = pygame.image.load('../img/arbol_talado.png')
    PIEDRA = pygame.image.load('../img/piedra.png')
    CLOSE = pygame.image.load('../img/close.png')
    CASA = pygame.image.load('../img/casa.png')
    PERSONA = pygame.image.load('../img/persona.png')

    def FUENTE(size):
        return pygame.font.Font('../fonts/poppinsmedium.ttf', size)


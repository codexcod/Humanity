import pygame


class Helper:

    AGUA = pygame.image.load('../img/agua.jpg')
    PASTO = pygame.image.load('../img/pasto.jpg')
    ARENA = pygame.image.load('../img/arena.jpg')
    ARBOL = pygame.image.load('../img/arbol.png')
    ARBOL_GRANDE = pygame.image.load('../img/arbol_grande.png')
    ARBOL_TALADO = pygame.image.load('../img/arbol_talado.png')
    PIEDRA = pygame.image.load('../img/piedra.png')
    PIEDRA_ORO = pygame.image.load('../img/piedraoro.png')
    CLOSE = pygame.image.load('../img/close.png')
    CASA = pygame.image.load('../img/casa.png')
    PERSONA = pygame.image.load('../img/persona.png')
    FOGATA = pygame.image.load('../img/fogata.gif')
    RECUADRO = pygame.image.load('../img/recuadro.png')
    SELECCIONADO = pygame.image.load('../img/seleccionado.png')
    COLORINACTIVO = pygame.Color('lightskyblue3')
    COLORACTIVO = pygame.Color('dodgerblue2')
    PAUSAR = pygame.image.load('../img/Pausar.png')

    def FUENTE(size):
        return pygame.font.Font('../fonts/poppinsmedium.ttf', size)


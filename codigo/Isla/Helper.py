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
    PERSONA_TRABAJANDO = pygame.image.load('../img/persona_trabajando.png')
    FOGATA = pygame.image.load('../img/fogata.gif')
    RECUADRO = pygame.image.load('../img/recuadro.png')
    SELECCIONADO = pygame.image.load('../img/seleccionado.png')
    COLORINACTIVO = pygame.Color('lightblue')
    COLORACTIVO = pygame.Color('dodgerblue2')
    TRONCO = pygame.image.load('../img/tronco.png')

    
    
    def FUENTE(size):
        return pygame.font.Font('../fonts/poppinsmedium.ttf', size)

    
    def CONEJO(animacionConejo):
        return pygame.image.load(f'../img/Conejo/Conejo-{animacionConejo}.png')

    



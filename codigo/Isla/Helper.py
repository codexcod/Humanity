import pygame
from pygame import mixer
mixer.init()

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
    INVENTARIO = pygame.image.load('../img/inventario.png')
    MENU_MUSICA = mixer.music.load('../sounds/menumusic.wav')
    FONDO = pygame.image.load('../img/fondo/fondo.png') 

    def playMusic(music,volume):
        if music == 'menu':
            pygame.mixer.music.set_volume(volume)
            mixer.music.load('../sounds/menumusic.wav')
            mixer.music.play()
        elif music == 'juego':
            pass
        else:
            pass

    def stopMusic():
        pygame.mixer.music.stop()

    def fadeMusic(time):
        pygame.mixer.music.fadeout(time)

    def FUENTE(size):
        return pygame.font.Font('../fonts/poppinsmedium.ttf', size)

    def CONEJO(animacionConejo):
        return pygame.image.load(f'../img/Conejo/Conejo-{animacionConejo}.png')

    def FONDOANIMACION(animacionFondo):
        return pygame.image.load(f'../img/fondo/fondo{animacionFondo}.png')

    



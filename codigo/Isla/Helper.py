import pygame
from pygame import mixer


mixer.init()

class Helper:
    # El helper es una herramienta la cual usamos para achicar el codigo

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
    PERSONA_DAÑADA = pygame.image.load('../img/persona_dañada.png')
    FOGATA = pygame.image.load('../img/fogata.gif')
    RECUADRO = pygame.image.load('../img/recuadro.png')
    SELECCIONADO = pygame.image.load('../img/seleccionado.png')
    COLORINACTIVO = pygame.Color('lightblue')
    COLORACTIVO = pygame.Color(18,220,110)
    TRONCO = pygame.image.load('../img/tronco.png')
    INVENTARIO = pygame.image.load('../img/inventario.png')
    MENU_MUSICA = mixer.music.load('../sounds/menumusic.wav')
    FONDO = pygame.image.load('../img/fondo/fondo.png') 
    CARNE = pygame.image.load('../img/carne.png')
    ARBUSTO = pygame.image.load('../img/arbusto.png') 
    ARBUSTO_FRUTAL = pygame.image.load('../img/arbusto_frutal.png')
    ROCA_OBJETO = pygame.image.load('../img/roca_objeto.png')
    BAYA_OBJETO = pygame.image.load('../img/baya.png')
    HACHA = pygame.image.load('../img/hacha.png')
    PICO = pygame.image.load('../img/pico.png')
    PICO_ROTO = pygame.image.load('../img/pico_roto.png')
    LEÑADOR = pygame.image.load('../img/leñador.png')
    FLECHA_ABAJO = pygame.image.load('../img/flecha_abajo.png')
    FLECHA_ARRIBA = pygame.image.load('../img/flecha_arriba.png')
    FONDO_PIEDRA = pygame.image.load('../img/FondoPiedra.png')
    CEREBRO = pygame.image.load('../img//cerebro/cerebro.png')
    CEREBRO_MEDIANO = pygame.image.load('../img//cerebro/cerebro_mediano.png')
    CEREBRO_CHICO = pygame.image.load('../img//cerebro/cerebro_chico.png')
    CEREBRO_DIMINUTO = pygame.image.load('../img//cerebro/cerebro_diminuto.png')
    MURO = pygame.image.load('../img/muro.png')

    MESA_DE_TRABAJO = pygame.image.load('../img/mesa_de_trabajo.png')

    BARCO = pygame.image.load('../img/barco.png')

    NIEBLA = pygame.image.load('../img/niebla.png')



    FONDO_BORDO = pygame.image.load('../img/fondo_bordo.png')
    CABEZA_PERSONA = pygame.image.load('../img/cabeza_persona.png')

    
    def getImage(image,width,height):
        return pygame.transform.scale(image, (width, height))

    def getSurface(width,height):
        return pygame.surface.Surface((width, height))

    def playMusic(music, volume):
        if music == 'menu':
            pygame.mixer.music.set_volume(volume)
            mixer.music.load('../sounds/menumusic.wav')
            mixer.music.play(-1)
        elif music == 'juego':
            pass
        else:
            pass
    menumusic= True

    def pauseMusic():
        pygame.mixer.music.pause()
        menumusic= True
        return menumusic

    def unpauseMusic():
        menumusic= False
        pygame.mixer.music.unpause()
        

    def fadeMusic(time):
        pygame.mixer.music.fadeout(time)
    

    def FUENTE(size):
        return pygame.font.Font('../fonts/poppinsmedium.ttf', size)


    def FONDOANIMACION(animacionFondo):
        return pygame.image.load(f'../img/fondo/fondo{animacionFondo}.png')
  
    def CONEJO(animacionConejo):
        return pygame.image.load(f'../img/Conejo/CONEJO-{animacionConejo}.png')

    def VACA(animcacionVaca):
        return pygame.image.load(f'../img/Vaca/vaca{animcacionVaca}.png')

    def JABALI(animcacionJabali):
        return pygame.image.load(f'../img/Jabali/Jabali-{animcacionJabali}.png')

    def getActividad(actividad):
        if actividad == 1:
            return (128,64,0),"Talando arboles"

        elif actividad == 2:
            return (155,155,155),"Picando piedra"

        elif actividad == 4:
            return (0,143,57),"Cortando Arbustos"

        elif actividad == 3:
            return (250,128,114),"Cazando animales"

        elif actividad == 0:
            return (155,155,155),"Sin tarea"
        

    



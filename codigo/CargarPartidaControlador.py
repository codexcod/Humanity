import pygame



class CargarPartidaControlador:
    def __init__(self):
    self.ancho = 640
    self.alto = 480
    self.screen = pygame.display.set_mode((ancho, alto))
    self.clock = pygame.time.Clock()


    #Tiempo para fondo
    timerFondo = 4
    pygame.time.set_timer(timerFondo,1000)


    partida = None
    start= ""
    
    def degradado():
        # Pantalla para el FADE de cambio de pantalla
        pantallaNegra = pygame.Surface((self.ancho, self.alto))
        pantallaNegra.fill((0, 0, 0))
        #Cambia rapidamente entre la pantalla y la pantalla negra cada vez mas lento
        #hasta quedar todo negro
        for alpha in range(0, 300):
            pantallaNegra.set_alpha(alpha)
            dibujarMenu()
            screen.blit(pantallaNegra, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)


    partidas = []
    slotsPartidas = 3
    #Meter los archivos de "Info" en "archivos"
    archivos = os.listdir("Info")
    #Buscar las partidas que hay
    for partida in archivos:
        partes = partida.split(".")
        partidas.append(partes[0])

    #Definir los slots vacios de partidas
    nuevasPartidas = slotsPartidas
    for partida in partidas:
        nuevasPartidas -= 1


    #Crear los recuadros para las islas
    recuadrosIslas = []
    for i in range(0,3):
        recuadrosIslas.append(pygame.Rect((10, 10 + (155*i)), (self.ancho- 20, 150)))


    botonesIniciar = []
    botonesNew = []
    botonesBorrar = []
    botones = []
    i = 0
    for partida in partidas:
        i += 1
        #Por cada partida que haya crear sus respectivos botones iniciar y borrar
        botonesIniciar.append(Partida((ancho-150,(i*155)),20,"  Elegir Isla  ",screen,"white","black","brown",partida))
        botonesBorrar.append(Partida((ancho-10,(i*155)),20,"  Borrar Isla  ",screen,"white","black","brown",partida))
    
    #Por cada slot de partida vacio crear un boton "Nueva Partida"
    for i in range(3-nuevasPartidas+1, 3+1):
        botonesNew.append(Button((ancho-10,(i*155)),20,"Nueva Partida",screen,"white","black","brown"))

    #Ordenar los tipos de botones en una lista para que sean mas faciles de dibujar
    botones = [botonesIniciar , botonesBorrar, botonesNew]

    #Crear el cuadro de la advertencia de Borrar
    advertencia = PopUp(ancho, alto)

    #Crear los botones para la advertencia de Borrar
    botonAceptar = Button((ancho / 2 , alto / 2 + 45), 24, "   Si   ", screen, "black", "black", "grey")
    botonRechazar = Button((ancho / 2 + 85 , alto / 2 + 45), 24, "   No   ", screen, "black", "black", "grey")
    

    def dibujarMenu():
        orange = (210,137,8)
        for recuadro in recuadrosIslas:
            pygame.draw.rect(screen, orange, recuadro)

        nombrePartida = []
        for partida in partidas:
            nombrePartida.append(Helper.FUENTE(30).render(partida, True, "black"))

        for i in range(nuevasPartidas):
            nombrePartida.append(Helper.FUENTE(30).render("No hay partida creada", True, "black"))

        i = 0
        #Dibujar los nombres de las partidas
        for nombre in nombrePartida:
            screen.blit(nombre,(20, 50 + (i*155) + 10)) 
            i += 1

        #Dibujar los botones de cada tipo
        for listas in botones:
            for boton in listas:  
                boton.dibujarBoton(1)

        #Dibujar la advertencia si se clickeo borrar
        if confirmarBor == True:
            popArriba = "Seguro que desea eliminar"
            popAbajo = "Esta isla"
            popPosArriba = (ancho/ 2 - 90, alto/ 2 - 40)
            popPosAbajo = (ancho/ 2 - 30, alto/ 2 - 20)
            advertencia.dibujarCuadro(popArriba, popAbajo, screen, popPosArriba, popPosAbajo)
            botonAceptar.dibujarBoton(1)
            botonRechazar.dibujarBoton(1)

    def run(self):  
        confirmarBor = False
        islas = True     
        while islas:
            for event in pygame.event.get():
                # Salir
                if event.type == pygame.QUIT:
                    islas = False


            #Por cada boton "Iniciar" checkear si clickean en el
            if confirmarBor == False:
                for boton in botonesIniciar:      
                    if boton.click(event):
                        #Iniciar la partida asociada al boton
                        degradado()
                        cargarJuego(boton.getPartida())
                        islas = False


            #Por cada boton "Borrar" checkear si clickean en el
            for boton in botonesBorrar:
                if boton.click(event):
                    #se debera llamar a la advertencia
                    confirmarBor = True
                    #Crear un holder para la info de ese boton
                    botonHolder = boton

            
            if botonAceptar.click(event):
                confirmarBor = False
                botonHolder.setBorrar(True)


            if botonRechazar.click(event):
                confirmarBor = False

            #Por cada boton "Nueva partida" checkear si clickean en el
            if confirmarBor == False:
                for boton in botonesNew:
                    if boton.click(event):
                        #salir de esta pantalla e ir al menu de creacion
                        degradado()
                        islas = False
                        menu()


            try:
                #Si se confirma que se quiere borrar borrara
                if botonHolder.getBorrar() == True:
                    remove(f'info/{botonHolder.getPartida()}.json')
                    islas = False
                    Islasini()
            except:
                pass


            # Dibujar todo
            clock.tick(60)     
            screen.fill("black")
            dibujarMenu()   
            pygame.display.update()
import pygame


class Controlador:

    def __init__(self, isla, camara, partida):
        self.isla = isla
        self.camara = camara
        self.mouse = camara.getMouse()
        self.aldea = self.isla.getAldea()
        self.ancho = self.isla.getAncho()
        self.altura = self.isla.getAltura()
        self.partida = partida
        self.running = True

    def run(self):
        # Controlar tiempo en el juego
        clock = pygame.time.Clock()
        screenUpdate = 1
        # Tiempo para movibles
        pygame.time.set_timer(screenUpdate, 250)
        # Tiempo para arboles
        arbolesUpdate = 2
        pygame.time.set_timer(arbolesUpdate, 10000)

        guardado = 3
        pygame.time.set_timer(guardado, 20000)

        while self.running:
            # Checkea todos los eventos
            for event in pygame.event.get():
                # Cerrar juego
                if event.type == pygame.QUIT:
                    self.stopGame()

                # Checkea si algun boton del mouse es presionado
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousePressed(pygame.mouse.get_pressed())
                    if event.button == 4:
                        # Baja el zoom
                        self.camara.getZoom().bajarZoom()

                    if event.button == 5:
                        # Aumenta el zoom
                        self.camara.getZoom().subirZoom()

                if event.type == pygame.KEYDOWN:
                    self.keyEvent(event.key)

                if event.type == screenUpdate:
                    self.screenUpdate()

                if event.type == arbolesUpdate:
                    self.arbolesUpdate()

            self.camara.actualizarPantalla()
            self.camara.getUI().generarAldeaUI(self.aldea)
            self.camara.dibujarUI()
            pygame.display.update()

            clock.tick(60)
            # El reloj por el cual todos los eventos se actualizan

    def arbolesUpdate(self):
        # Dentro de los arboles talados, se suma el tiempo para que vuelva a crecer
        for arbol in self.isla.getArbolesTalados():
            arbol.avanzarTiempo()

    def screenUpdate(self):
        # Cuando se actualiza la pantalla, se movera todas las personas y animales
        for persona in self.aldea.getPersonas():
            persona.makeMoves()

        for animal in self.isla.getAnimales():
            animal.makeMoves()

    def stopGame(self):
        self.isla.toJson(self.partida)
        self.running = False

    def keyEvent(self, event):
        if event == pygame.K_RIGHT or event == pygame.K_d:
            self.camara.moveX(2)

        if event == pygame.K_LEFT or event == pygame.K_a:
            self.camara.moveX(-2)

        if event == pygame.K_UP or event == pygame.K_w:
            self.camara.moveY(-2)

        if event == pygame.K_DOWN or event == pygame.K_s:
            self.camara.moveY(2)

        if event == pygame.K_z:
            self.camara.getZoom().subirZoom()

        if event == pygame.K_x:
            self.camara.getZoom().bajarZoom()

        if event == pygame.K_SPACE:
            # Mueve la camara para volver a la aldea
            self.camara.setPosY(self.altura // 2)
            self.camara.setPosX(self.ancho // 2)

    def mousePressed(self, mouse):
        left, middle, right = mouse
        if left:

            # En el caso que sea el izquierdo se fija si hay UI´s
            if not self.camara.getUI().hayUIActivos():
                if not self.mouse.seleccionarMovible() is None:

                    self.camara.getUI().generarInfoObjeto(self.mouse.seleccionarMovible())

                elif not self.mouse.pedirInfoObjeto() is None:
                    self.camara.getUI().generarInfoObjeto(self.mouse.pedirInfoObjeto())

            else:
                self.mouse.clickearPorPoscicion(self.camara.getUI().getObjetosClickeables())

        # En el caso que sea derecha checkea si esta seleccionado
        if right:
            # Si esta seleccionado y no es una persona, y trata de seleccionar una persona, la selecciona.
            if not self.mouse.seleccionarMovible() is None:
                if not self.camara.getSeleccionado() == self.mouse.seleccionarMovible():
                    if self.mouse.seleccionarMovible() in self.aldea.getPersonas():
                        self.camara.setSeleccionado(self.mouse.seleccionarMovible())

                else:
                    # Si tiene algo seleccionado y es una persona, la deselecciona
                    self.camara.setSeleccionado(None)

            if not self.camara.getSeleccionado() is None:
                if self.mouse.pedirInfoObjeto() is None:
                    # Si lo seleccionado es una persona, y selecciona al piso, lo mueve al lugar
                    self.camara.getSeleccionado().moveToPosition(self.mouse.getObjectMousePosition()[0],
                                                                 self.mouse.getObjectMousePosition()[1])


                else:
                    if self.mouse.seleccionarMovible() is None:
                        # Si selecciona un objeto se fija si no es movible, hacerle algo al objeto
                        self.camara.getSeleccionado().accionarObjeto(self.mouse.pedirInfoObjeto())

                    else:
                        # Si selecciona a un movible, desde una persona, se fija de poder hacerle algo al movile
                        if not self.mouse.seleccionarMovible() in self.aldea.getPersonas():
                            self.camara.getSeleccionado().accionarObjeto(self.mouse.seleccionarMovible())

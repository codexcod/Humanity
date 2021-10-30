
class Estatico:

    def __init__(self,x,y):
        self.visible = False
        self.image = None
        self.x = x
        self.y = y

    def setVisivilidad(self,visibilidad):
        self.visible = visibilidad

    def getVisibilidad(self):
        return self.visible

    def toJson(self):
        return {
            'x' : self.x,
            'y' : self.y,
            'visibilidad' : self.visible
        }
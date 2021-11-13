class Venta:

    def __init__(self,objeto,nivelNecesario):
        self.objeto = objeto
        self.nivelNecesario = nivelNecesario
        self.listaPrecio = []

    def getObjeto(self):
        return self.objeto

    def getNivelNecesario(self):
        return self.nivelNecesario

    def getListaPrecio(self):
        return self.listaPrecio        

    def addListaPrecio(self,precio):
        self.listaPrecio.append(precio)
import numpy as np
import sys

class NoiseGenerator:

    def __init__(self, ancho, altura, obj1, obj2,cantidad):
        self.ancho = ancho
        self.altura = altura
        self.obj1 = obj1
        self.obj2 = obj2
        
        # Formacion de arboles
        np.set_printoptions(threshold=sys.maxsize)
        from scipy.ndimage.interpolation import zoom
        arr = np.random.uniform(size=(altura // 10,ancho // 10))
        arr = zoom(arr, 10)
        arr = arr > cantidad
        arr = np.where(arr, obj1, obj2)
        self.noise = arr
        arr = np.array_str(arr, max_line_width = 300)
        

    
    def getNoise(self):
        return self.noise
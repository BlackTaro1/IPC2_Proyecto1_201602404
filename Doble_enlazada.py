from Terrenos import Terreno

class ListaDoble():
    def __init__(self):
        self.inicio = None

    def insertar(self, nombre, dimension, combustible): #insertar
        nuevo = Terreno(nombre, dimension, combustible)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

    def mostrarCursos(self):
        tmp = self.inicio
        while tmp is not None:
            print('Nombre:', tmp.nombre, 'Dimension:', tmp.dimension, 'Combustible:', tmp.combustible)
            tmp = tmp.siguiente

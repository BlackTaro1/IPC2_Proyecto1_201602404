from Terrenosvfall import Terreno
from Posicion import Posicion

class listaEncabezado:
    def __init__(self, primero=None):
        self.primero = primero
    
    def setEncabezado(self, nuevo):
        if self.primero == None:
            self.primero == nuevo
        elif nuevo.nombre < self.primero.nombre:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo    
        else:
            actual = self.primero
            while actual.siguiente != None:
                if nuevo.nombre < actual.siguiente.nombre:
                    nuevo.siguiente = actual.siguiente
                    actual.siguente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
            if actual.siguente == None:
                actual.siguiente = nuevo
                nuevo.anterior = actual
         
    def getEncabezado(self, nombre): #Metodo a utilizar para la busqueda del terreno
        actual = self.primero
        while actual != None:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

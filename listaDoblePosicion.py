from Posicion import Posicion

class listaDoblePosicion():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertar(self, Posx, Posy, Combustible):
        nodo = Posicion(Posx, Posy, Combustible)
        #print("nodo combustible", nodo.combustible)
        if self.inicio is None:
            self.inicio = nodo
            self.fin = nodo
        else:
            tmp = self.fin
            tmp.siguiente = nodo
            nodo.anterior = nodo
            self.fin = nodo
        self.size +=1
        return nodo

    
    
    def getPosiciones(self):
        tmp = self.inicio
        while tmp is not None:
            print("x", tmp.x, "y: ", tmp.y, "combustible: ", tmp.combustible)
            tmp = tmp.siguiente
    
    def getPosicion(self, x,y):
        tmp = self.inicio
        while tmp is not None: #1.s -> 2.s -> 3.s -> 4.s -> None
            if tmp.x == x and tmp.y==y:
                return tmp
            tmp = tmp.siguiente

    def iterar(self):
        actual = self.inicio
        while actual:
            combustible = actual.gas
            actual = actual.siguiente
            yield combustible

    def getList(self):
        print("llego al get list de posiciones")
        return self    

  

    

        
        
        

    

  
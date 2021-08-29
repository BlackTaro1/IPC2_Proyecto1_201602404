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
        return self    

    # def insertar(self, posx, posy, combustible):
    #     nuevo = Posicion(posx, posy, combustible)
    #     inicio = self.inicio
    #     if ePosx == None:
    #         Posicion(posx, posy, combustible)
    #         ePosx.accesoNodo = nuevo
    #         self.eFila.setEncabezado(ePosx)
    #         return ePosx
    
    # def insertarPosicion(self, posx, posy, combustible, listaPos):
    #     nuevo = Posicion(posx, posy, combustible)
    #     print(nuevo.posx, nuevo.posy, nuevo.combustible, "datos recividos")
    #     nuevo.siguiente = None
    #     if listaPos.combustible == None:
    #          listaPos = nuevo
    #     else:
    #         aux = listaPos
    #         cont = 0
    #         while aux != None:
    #            print(aux.posx, "posicion x", aux.posy, "posicion y", aux.combustible, "combustible")
    #            aux = aux.siguiente
    #            nuevo = aux
    #     print(listaPos.posx, "soy el nodo actual")
        
    def imprimir(self, listaPos):
        cont = 0
        if listaPos.a == None:
            print("no hay datos")
        else:
            aux = listaPos
            while aux != None:
                print("Entre ", cont)
                print(aux.b, aux.c, aux.a)
                aux = aux.siguiente
                cont += 1
        return listaPos

    

        
        
        

    

  
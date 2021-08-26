from Posicion import Posicion
from Terrenos import Terreno
from encabezado import listaEncabezado

class listaDoblePosicion():
    def __init__(self):
        self.inicio = Posicion("", "", -1)

    # def insertar(self, posx, posy, combustible):
    #     nuevo = Posicion(posx, posy, combustible)
    #     inicio = self.inicio
    #     if ePosx == None:
    #         Posicion(posx, posy, combustible)
    #         ePosx.accesoNodo = nuevo
    #         self.eFila.setEncabezado(ePosx)
    #         return ePosx
    
    def insertarPosicion(self, posx, posy, combustible, listaPos):
        nuevo = Posicion(posx, posy, combustible)
        #print(nuevo.posx, nuevo.posy, nuevo.combustible, "l")
        nuevo.siguiente = None
        if listaPos.combustible == None:
             listaPos = nuevo
        else:
             aux = listaPos
        #     cont = 0
             while aux != None:
                print(aux.combustible, " < algo")
                aux = aux.siguiente
        aux = nuevo
        return listaPos
    
    def imprimir(self, listaPos):
        cont = 0
        if listaPos.combustible == None:
            print("no hay datos")
        else:
            aux = listaPos
            while aux != None:
                print("Entre ", cont)
                print(aux.posx, aux.posy, aux.combustible)
                aux = aux.siguiente
                cont += 1

    

        
        
        

    

  
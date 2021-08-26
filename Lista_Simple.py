from Posicion import Posicion
from matrizT import listaEncabezado

class ListaSimple():
    def __init__(self):
        self.eFila = listaEncabezado()
        self.eColumna = listaEncabezado()

    def insertar(self, fila, columna, gas):
        nuevo = Posicion(fila, columna, gas)
        ePosx = self.eFila.getEncabezado
        if ePosx == None:
            ePosx == Posicion(fila)
            ePosx.accesoNodo = nuevo
            self.eFila.setEncabezado(ePosx)
        else:
            if nuevo.columna < ePosx.accesoNodo.columna:
                nuevo.derecha = ePosx.accesoNodo
                ePosx.accesoNodo.izquierda = nuevo
                ePosx.accesoNodo = nuevo
            else:
                actual = ePosx.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual
        ePosy = self.eColumna.getEncabezado(columna)
        if ePosy == None:
            ePosy = Posicion(columna)
            ePosy.accesoNodo = nuevo
            self.eColumna.setEncabeza(ePosy)
        else: 
            if nuevo.fila < ePosy.accesoNodo.fila:
                nuevo.abajo = ePosy.accesoNodo
                ePosy.accesoNodo.arriba = nuevo
                ePosy.accesoNodo = nuevo
            else:
                actual = ePosy.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo 
                        nuevo.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual
    
    
    #     self.size = 0

    # def insertarTerreno(Lterreno, nuevo):
    #     newTerreno = nuevo
    #     if Lterreno.anterior != None: #comparamos el nodo inicio 
    #             anterior = Lterreno #si esta vacio entonces inciamos si no pasamos al siguiente
    #             while anterior.siguiente != None:
                    
    #                 anterior = anterior.siguiente
    #             anterior.siguiente = newTerreno
    #     else: #si esta vacia entonces el nodo inicio es nuevo
    #             Lterreno.inicio = newTerreno
    #     return Lterreno

    

  
    def imprimir(cadena):
        print(cadena.nombre)


    def listadoTerrenos(self): #Metodo para imprimir los datos en la lista.
            tmp = self.inicio
            while tmp != None:
                print("Nombre: ", tmp.nombre)
                tmp = tmp.siguiente
            print("No hay mas datos")  

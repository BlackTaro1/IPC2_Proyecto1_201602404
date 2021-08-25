from Terrenos import Terreno

class ListaSimple():
    def __init__(self):
        self.inicio = None
        self.size = 0

    def insertarTerreno(self, Terreno):
        #self.size += 1
        print(Terreno.attrib)
       #nuevo = Terreno
        self = Terreno
        nuevo = self
        if self.inicio: #comparamos el nodo inicio 
                anterior = self.inicio #si esta vacio entonces inciamos si no pasamos al siguiente
                while anterior.siguiente != None:
                    anterior = anterior.siguiente
                anterior.siguiente = nuevo
        else: #si esta vacia entonces el nodo inicio es nuevo
                self.inicio = nuevo

    def insertarCombustible(self, combustible):
        self.inicio = combustible
        



    def imprimir(cadena):
        print(cadena)
        print("hola prro")


    def listadoTerrenos(self): #Metodo para imprimir los datos en la lista.
            tmp = self.inicio
            while tmp != None:
                print("Nombre: ", tmp.nombre)
                tmp = tmp.siguiente
            print("No hay mas datos")  

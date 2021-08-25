from Terrenos import Terreno

class ListaSimple():
    def __init__(self):
        self.inicio = None
        self.size = 0

    def insertarTerreno(Lterreno, nuevo):
        newTerreno = nuevo
        if Lterreno.anterior != None: #comparamos el nodo inicio 
                anterior = Lterreno #si esta vacio entonces inciamos si no pasamos al siguiente
                while anterior.siguiente != None:
                    
                    anterior = anterior.siguiente
                anterior.siguiente = newTerreno
        else: #si esta vacia entonces el nodo inicio es nuevo
                Lterreno.inicio = newTerreno
        return Lterreno

    

  
    def imprimir(cadena):
        print(cadena.nombre)


    def listadoTerrenos(self): #Metodo para imprimir los datos en la lista.
            tmp = self.inicio
            while tmp != None:
                print("Nombre: ", tmp.nombre)
                tmp = tmp.siguiente
            print("No hay mas datos")  

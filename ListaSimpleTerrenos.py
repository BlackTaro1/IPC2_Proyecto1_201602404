class nodoTerreno():
    def __init__(self, nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy):
        self.nombre = nombre
        self.dimensionm = dimensionm
        self.dimensionn = dimensionn
        self.iniciox = iniciox
        self.inicioy = inicioy
        #self.posicion = posicion
        self.finx = finx
        self.finy = finy
        self.siguiente = None
        self.accesoNodo = None

class listaSimpleTerrenos(object):

    def __init__(self):
        self.inicio = None

    def insertarenlistaVacia(self, nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy):
        if self.inicio is None:
            nuevo = nodoTerreno(nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy)
            self.inicio = nuevo
        else:
            print("la lista no esta vacia")

    def insertarInicio(self, nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy):
        if self.inicio is None:
            nuevo = nodoTerreno(nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy)
            self.inicio = nuevo
            print("nodo insertado")
            return
        nuevo = nodoTerreno(nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo
    
    def iterar(self):
        actual = self.inicio
        while actual:
            datos = actual.nombre
            actual = actual.siguiente
            yield datos

        

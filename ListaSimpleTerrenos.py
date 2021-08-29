from listaDoblePosicion import listaDoblePosicion

class nodoTerreno():
    def __init__(self, nombre, dm, dn, iniciox, inicioy, finx, finy):
        self.nombre = nombre
        self.dimensionm = dm
        self.dimensionn = dn
        self.iniciox = iniciox
        self.inicioy = inicioy
        #self.posicion = posicion
        self.finx = finx
        self.finy = finy
        self.listaPosiciones = listaDoblePosicion()
        self.siguiente = None

class listaSimpleTerrenos():

    def __init__(self):
        self.inicio = None
        self.size = 0

    def insertarTerreno(self, nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy):
        nuevo = nodoTerreno(nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy)
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            temp = self.inicio
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo
        return nuevo

    def iterar(self):
        actual = self.inicio
        while actual:
            datos = actual.nombre
            actual = actual.siguiente
            yield datos

        

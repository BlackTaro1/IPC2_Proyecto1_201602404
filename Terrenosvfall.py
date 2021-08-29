from Posicion import Posicion 

class Terreno:

    def __init__(self, nombre, dimensionm, dimensionn, iniciox, inicioy, finx, finy, posicion):
        self.nombre = nombre
        self.dimensionm = dimensionm
        self.dimensionn = dimensionn
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.posicion = posicion
        self.finx = finx
        self.finy = finy
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None

    

    
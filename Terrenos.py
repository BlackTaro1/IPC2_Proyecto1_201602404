class Terreno:

    def __init__(self, nombre, dimension, iniciox, inicioy, finx, finy):
        self.nombre = nombre
        self.dimension = dimension
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.siguiente = None
        self.anterior = None
class Posicion():
    def __init__(self, posx, posy, combustible):
       self.posx = posx #fila
       self.posy = posy #columna
       self.combustible = combustible # combustible
       self.anterior = None
       self.siguiente = None

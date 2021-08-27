class Posicion(object):
    def __init__(self, posx, posy, combustible):
       self.posx = posx #fila
       self.posy = posy #columna
       self.combustible = combustible # combustible
       self.siguiente = None
       self.anterior = None
      

class Posicion(object):
    def __init__(self, posx, posy, gas):
       self.posx = posx #fila
       self.posy = posy #columna
       self.gas = gas # combustible
       self.siguiente = None
       self.anterior = None
      

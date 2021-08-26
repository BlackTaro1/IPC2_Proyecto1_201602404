class Posicion():
    def __init__(self, posx, posy, combustible):
       self.posx = posx #fila
       self.posy = posy #columna
       self.combustible = combustible # combustible
       self.izquierda = None
       self.derecha = None
       self.arriba = None
       self.abajo = None

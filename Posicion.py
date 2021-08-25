class Posicion():
    def __init__(self, posx, posy, combustible):
       self.posx = posx
       self.posy = posy
       self.combustible = combustible
       self.izquierda = None
       self.derecha = None
       self.arriba = None
       self.abajo = None

class encabezadoPosicion():
    def __init__(self) -> None:
        self.id
class Canal:
    def __init__(self, grilla, precio):
        self.grilla = grilla
        self.precio = precio
        self.codigo = hash(self)

    def set_precio(self, value):
        self.precio = value


class Grilla:
    def __init__(self, programas):
        self.programas = programas


class Programa:
    def __init__(self, inicio, fin, precio):
        self.inicio = inicio
        self.fin = fin
        self.precio = precio

    def set_precio(self, value):
        self.precio = value


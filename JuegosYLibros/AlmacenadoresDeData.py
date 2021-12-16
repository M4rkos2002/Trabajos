class Carrito:
    def __init__(self):
        self.storge = []
    
    def set_storge_vacío(self):
        self.storge = []

class Factura:
    def __init__(self, costo, productos, fecha):
        self.costo = costo
        self.productos = productos
        self.emitida = False
        self.fecha = fecha

    def __repr__(self):
        return f"{self.fecha}"

    def getCosto(self):
        return self.costo
    
    def set_emitida(self):
        self.emitida = True
    
    def __lt__(self, other):
        return self.fecha < other.fecha
    
class Tarjeta:
    def __init__(self):
        self.saldo = 0

    def set_pedir_saldo(self, dinero):
        self.saldo += dinero

    def set_abonar_saldo(self, dinero):
        self.saldo -= dinero

import Excepciones
class AlmacenDeLibros:
    libros = []

    @classmethod
    def agregar_libro(cls, libro):
        cls.libros.append(libro)
    
    @classmethod
    def quitar_libro(cls, libro):
        try:
            cls.libros.remove(libro)
        except ValueError:
            print(Excepciones.LibroNoExiste.getMsg())

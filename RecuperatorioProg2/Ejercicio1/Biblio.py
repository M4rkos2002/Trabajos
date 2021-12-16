class Libro:
    def __init__(self):
        self.__codigo = hash(self)

    def getCodigo(self):
        return self.__codigo

class Biblioteca:

    def __init__(self):
        self.dia = 0
    
    def recibir_libros(self, bibliotecario):
        if self.dia%7 == 0:
            counter = 0
            while counter < 1000:
                bibliotecario.getlibros_sin_Cargar().append(Libro())
                counter += 1
        elif self.dia%7 != 0:
            return "No es día de entrega"

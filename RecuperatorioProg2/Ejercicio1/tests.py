import Excepsciones
import almacenadores
class Bibliotecario:

    def __init__(self):
        self.__recaudo_multas = 0
        self.__libros_sin_cargar = []

    def cargar_libros_al_sistema(self):
        for libro in self.__libros_sin_cargar:
            SistemaDeLibros.libros.append(libro)
            self.__libros_sin_cargar = []

    def verificar_existencia_libro(self, cliente, libro):
        try:
            counter = 0
            for i in SistemaDeLibros.libros:
                if i.getCodigo() == libro.getCodigo():
                    for reserva in SistemaDeLibros.reservados:
                        if reserva.getCodigoLibro() == i.getCodigo():
                            counter += 1
                            raise Excepsciones.LibroExistePeroEstaReservado()
            if counter == 1:
                raise Excepsciones.LibroNoExiste()
        except Excepsciones.LibroExistePeroEstaReservado:
            print(Excepsciones.LibroExistePeroEstaReservado.getMsg())
        except Excepsciones.LibroNoExiste:
            print(Excepsciones.LibroNoExiste.getMsg())
        
        reserva = almacenadores.Reserva(cliente.getNombre(), Calendario.dia+7, libro.getCodigo())
        SistemaDeLibros.reservados.append(reserva)


    def recibir_devueltos(self, libro):
        pass

    def getlibros_sin_Cargar(self):
        return self.__libros_sin_cargar

class Cliente:

    def __init__(self, nombre):
        self.__libros = []
        self.__nombre = nombre

    def retirar_libro(self, biblotecario, libro):
        pass

    def devolver_libro(self, bibliotecario, libro):
        pass

    def getNombre(self):
        return self.__nombre

class SistemaDeLibros:

    libros = []
    reservados = []
    devueltos = []

    @classmethod
    def verificar(libro):
        pass

class Calendario:
    dia = 0
    @classmethod
    def pasar_dia(self):
        self.dia += 1

import Biblio
import unittest

class testeos(unittest.TestCase):

    def test_verificar_existencia(self):
        yo = Bibliotecario()
        vos = Cliente("Hola")
        libro = Biblio.Libro()
        yo.verificar_existencia_libro(vos, libro)
        self.assertEqual(len(SistemaDeLibros.reservados),1)

if __name__ == "__main__":
    unittest.main()
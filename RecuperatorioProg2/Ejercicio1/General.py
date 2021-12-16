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
            return -1
        except Excepsciones.LibroNoExiste:
            print(Excepsciones.LibroNoExiste.getMsg()) 
            return -1
        reserva = almacenadores.Reserva(cliente.getNombre(), Calendario.dia+7, libro.getCodigo())
        SistemaDeLibros.reservados.append(reserva)
        return libro


    def recibir_devueltos(self, libro):
        dia = Calendario.dia
        devolucion = almacenadores.Devolucion(dia)
        for reserva in SistemaDeLibros.reservados:
            if reserva.getCodigoLibro() == libro.getCodigo():
                laReserva = reserva
                diaPrestado = reserva.getDia()
        try:
            if dia >= (diaPrestado + 14):
                raise Excepsciones.NoEntregaATiempo()
        except Excepsciones.NoEntregaATiempo:
            print(Excepsciones.NoEntregaATiempo.getMsg())
            self.__recaudo_multas += 100
            devolucion.set_multa()
        SistemaDeLibros.devoluciones.append(devolucion)
        SistemaDeLibros.QuitarReserva(laReserva)
        

    def getlibros_sin_Cargar(self):
        return self.__libros_sin_cargar

    def getRecaudado(self):
        return self.__recaudo_multas


class Cliente:

    def __init__(self, nombre):
        self.__libros = []
        self.__nombre = nombre

    def retirar_libro(self, bibliotecario, libro):
        a_retirar = bibliotecario.verificar_existencia_libro(self.__nombre, libro)
        if a_retirar == libro:
            self.__libros.appened(libro)

    def devolver_libro(self, bibliotecario, libro):
        bibliotecario.recibir_devueltos(libro)
        self.__libros.remove(libro)

    def getNombre(self):
        return self.__nombre


class SistemaDeLibros:

    libros = []
    reservados = []
    devoluciones = []

    @classmethod
    def QuitarReserva(cls, reserva):
        for i in cls.reservados:
            if reserva == i:
                cls.reservados.remove(reserva)



class Calendario:
    dia = 0
    @classmethod
    def pasar_dia(self):
        self.dia += 1
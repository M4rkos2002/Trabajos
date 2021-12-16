class Reserva:

    def __init__(self, nombre_cliente, dia_de_devolucion, codigoLibro):
        self.__codigoLibro = codigoLibro
        self.__nombre_cliente = nombre_cliente
        self.__dia_de_devolucion = dia_de_devolucion

    def getDia(self):
        return self.__dia_de_devolucion

    def getNombreCliente(self):
        return self.__nombre_cliente

    def getCodigoLibro(self):
        return self.__codigoLibro


class Devolucion:

    def __init__(self, dia_devuelto):
        self.__dia_devuelto = dia_devuelto
        self.__multa = False
    
    def set_multa(self):
        self.__multa = True

    def get_multa(self):
        return self.__multa

    def get_dia_devuelto(self):
        return self.__dia_devuelto
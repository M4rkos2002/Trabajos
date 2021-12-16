class Zona:

    def __init__(self):
        self.__terminales = [] 

    def agregar_terminales(self, terminal):
        self.__terminales.append(terminal)

    def quitar_terminales(self, terminal):
        self.__terminales.remove(terminal)

    def getTerminales(self):
        self.__terminales

class Calendario:

    dia = 0
    hora = 0

    def pasarDia(self):
        self.dia += 1
    def pasarHora(self):
        self.hora += 1
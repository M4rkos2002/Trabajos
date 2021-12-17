class Streamin:

    def hacer_informe(self, fecha, hora, codigoUsuario, codigoCanal):
        informe 


class Informe:
    def __init__(self, codigoUsuario, codigoCanal, fecha, hora):
        self.codigoUsuario = codigoUsuario
        self.codigoCanal = codigoCanal
        self.fecha = fecha
        self.hora = hora

class Calendario:
    dia = 0
    hora = 0
    minutos = 0
    
    @classmethod
    def pasar_tiempo(cls):
        cls.minutos += 1
        if cls.minutos == 60:
            cls.minutos = 0
            cls.horas += 1
            if cls.horas == 24:
                cls.horas = 0
                cls.dia += 1  
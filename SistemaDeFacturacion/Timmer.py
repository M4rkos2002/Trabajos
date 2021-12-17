class Calendario:
    
    def __init__(self):
        self.mes = 0
        self.semana = 1
        self.dia = 1 #1=Lunes, 2=Martes....
        self.hora = 0
        self.min = 0

    def pasar_minuto(self):
        self.min += 1
        if self.min == 60:
            self.min = 0
            self.hora += 1
            if self.hora == 24:
                self.hora = 0
                self.dia += 1
                if self.dia == 8:
                    self.dia = 0
                    self.semana += 1
                    if self.demana == 5:
                        self.semana = 0
                        self.mes += 1

class Fecha:
    def __init__(self, semana, dia, hora, minuto):
        self.semana = semana
        self.dia = dia
        self.hora = hora
        self.minuto = minuto

    def diferencia_dias(self, hasta):
        """Calcula la diferencia de los dias"""
        hasta_dias = hasta.dia
        diferencia_dias = hasta_dias - self.dia
        if diferencia_dias < 0:
            diferencia_dias = (-1) * diferencia_dias
        return diferencia_dias

class Horario:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def diferencia_horas(self, horarioHasta):
        """Calcula la diferencia de horas"""
        hasta_hora = horarioHasta.hora
        diferencia_horas = hasta_hora - self.hora
        if diferencia_horas < 0:
            diferencia_horas = (-1) * diferencia_horas
        return diferencia_horas

    def diferencia_minutos(self, horarioHasta):
        """Calcula la diferencia de minutos"""
        diferencia_horas = self.diferencia_horas(horarioHasta)
        hasta_minutos = horarioHasta.minuto
        diferencia_minutos_desde_hasta = hasta_minutos - self.minuto
        if diferencia_minutos_desde_hasta < 0:
            diferencia_minutos_desde_hasta = (-1)*diferencia_minutos_desde_hasta 
        diferencia_minutos = (60*diferencia_horas) + diferencia_minutos_desde_hasta
        return diferencia_minutos
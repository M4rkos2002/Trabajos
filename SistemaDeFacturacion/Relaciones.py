import Timmer
timmer = Timmer.Calendario()
import Excepciones
import Almacenadores

class SistemaDeFacturacion:

    reportes = []
    localidades_Habilitadas = []

    def facturar(self, cliente):
        counter = 0 #para chequear si entró al loop
        llamadas_externas = []
        llamadas_locales = []
        abonoMensual = 0
        for reporte in self.reportes:
            if reporte.clienteId == cliente.id:
                llamada = reporte.llamada
                total_minutos = self.calcular_duracion_llamada(llamada.desde, llamada.hasta)
                if llamada.tipo == "Local":
                    llamadas_locales.append(llamada)
                    if reporte.fecha.dia != 6 and reporte.fecha.dia != 7:
                        if llamada.desde.hora > 8 and llamada.hasta.hora < 20:
                            abonoMensual += 0.20 * total_minutos
                        elif llamada.desde.hora < 8 and llamada.hasta.hora > 20:
                            abonoMensual += 0.10 * total_minutos
                    elif reporte.fecha.dia == 6 or reporte.fecha.dia == 7:
                        abonoMensual += 0.10* total_minutos    
                elif llamada.tipo == "Nacional":
                    llamadas_externas.append(llamada)
                    for posicion in self.localidades_Habilitadas:
                        if posicion.localidad == llamada.getLocalidad():
                            costo = posicion.precio
                            abonoMensual += total_minutos * costo
                elif llamada.tipo == "Internacional":
                    llamadas_externas.append(llamada)
                    for posicion in self.localidades_Habilitadas:
                        if posicion.pais == llamada.getPais():
                            costo = posicion.precio
                            abonoMensual += total_minutos * costo
            counter += 1
        try:
            if counter == 0:
                raise Excepciones.NoHayReportesDeLlamadas()
        except Excepciones.NoHayReportesDeLlamadas:
            return Excepciones.NoHayReportesDeLlamadas.getMsg()
        else:
            factura = Almacenadores.Factura(abonoMensual, llamadas_locales, llamadas_externas)             
            cliente.facturas.append(factura)
            return factura

    def calcular_duracion_llamada(self, desde, hasta):
        return desde.diferencia_minutos(hasta) #Desde seria una instancia de Horario en Timmer

    def set_localidades_habilitadas(self, posicionGeografica):
        self.localidades_Habilitadas.append(posicionGeografica)

class Cliente:
    
    def __init__(self, localidad, pais):
        self.id = hash(self)
        self.facturas = []
        self.localidad = localidad
        self.pais = pais

    def llamar(self, desde, hasta, tipo, localidad, pais):  #Desde y Hasta son Horarios, ver clase Horario() en archivo Timmer
        if tipo.title() == "Local":
            llamada = Almacenadores.LlamadaLocal(desde, hasta)
        elif tipo.title() == "Nacional":
            llamada = Almacenadores.LlamadaNacional(desde, hasta, localidad.title())
        elif tipo.title() == "Internacional":
            llamada = Almacenadores.LlamadaInternacional(desde, hasta, localidad.title(), pais.title())
        minutos_trascurridos = desde.diferencia_minutos(hasta)#En este bloque trascurre el tiempo
        counter = 0
        while counter < minutos_trascurridos:
            timmer.pasar_minuto()
            counter += 1
        Sensor.reportar_sistDeFact(self.id, llamada)



class Sensor:
    
    @classmethod
    def reportar_sistDeFact(self, clienteId, llamada):
        SistemaDeFacturacion.reportes.append(Almacenadores.Reporte(clienteId,
                                                        llamada, 
                                                        Timmer.Fecha(timmer.semana,
                                                        timmer.dia, timmer.hora,
                                                        timmer.min)))

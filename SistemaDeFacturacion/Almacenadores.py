class Reporte:
    def __init__(self, clienteId, llamada, fecha):
        self.clienteId = clienteId
        self.llamada = llamada
        self.fecha = fecha

    
class Llamada:
    def __init__(self, desde, hasta, tipo, localidad, pais):
        self.desde = desde
        self.hasta = hasta
        self.tipo = tipo
        self.localidad = localidad
        self.pais = pais

class LlamadaLocal(Llamada):
    def __init__(self, desde, hasta):
        super().__init__(desde, hasta, "Local", "Pilar", "Argentina")
    
class LlamadaNacional(Llamada):
    def __init__(self, desde, hasta, localidad):
        super().__init__(desde, hasta, "Nacional", localidad, "Argentina")

    def getLocalidad(self):
        return super().localidad  

class LlamadaInternacional(Llamada):
    def __init__(self, desde, hasta, localidad, pais):
        super().__init__(desde, hasta, "Internacional", localidad, pais)
        
    def getPais(self):
        return super().localidad

    
class Factura:
    def __init__(self, abonoMensual, LlamadosLocales, LlamadosExternos):
        self.abonoMensual = abonoMensual
        self.llamadosLocales = LlamadosLocales
        self.llamadosExternos = LlamadosExternos


class PosicionGeografica:

    def __init__(self, localidad, pais, precio):
        self.localidad = localidad
        self.pais = pais
        self.precio = precio
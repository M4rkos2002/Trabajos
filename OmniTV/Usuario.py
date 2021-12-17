from OmniTV.Streaming import Sensor
import Streaming
class Usuario:
    def __init__(self):
        self.facturas = []
        self.codigo = hash(self)

    def ver_programa(self, fecha, hora, canal, plataforma):
        plataforma.hacerInforme(fecha, hora, self.codigo, canal.codigo)
        
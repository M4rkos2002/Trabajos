class OmniTV:
    informes = []

    @classmethod
    def set_agregar_informe(self, informe):
        self.informes.append(informe)

    @classmethod
    def set_quitar_informe(self, informe):
        try:
            self.informes.remove(informe)
        except ValueError:
            print("Error, informe no existe")
        
    @classmethod
    def facturar(self, usuario):
        for informe in self.informes:
            if informe.codigoUsuario == usuario.codigo:
                for canal in Servidores.canales:
                    if canal.codigo == informe.codigoCanal:
                        factura = Factura(canal.precio, usuario.codigo)
                        usuario.facturas.append(factura)
                        return factura


import Canales
class GeneradorDeContenido:
    def __init__(self, canales):
        self.canales = canales

    def colocar_precio(self, objeto, monto):
        if isinstance(objeto, Canales.Canal):
            objeto.set_precio(monto)
        elif isinstance(objeto, Canales.Programa):
            objeto.set_precio(monto)


class Factura:
    def __init__(self, precio, codigoUsuario):
        self.precio = precio
        self.codigoUsuario = codigoUsuario


class Servidores:

    canales = []

    @classmethod
    def agregar_canal(self, canal):
        self.canales.append(canal)
    @classmethod
    def quitar_canal(self, canal):
        self.canales.remove(canal)
import AlmacenadoresDeData
import Excepciones
class Cliente:
    def __init__(self, tarjeta):
        self.mis_productos = []
        self.tarjeta = tarjeta
        self.carrito = None

    def elegir(self, producto, cantidad):
        if self.carrito == None:
            self.carrito = AlmacenadoresDeData.Carrito()
        item = (producto, cantidad)
        self.carrito.storge.append(item) 

    def abonar(self, factura, caja):
        caja.validar_tarjeta(self.tarjeta, factura)

    def set_carrito(self):
        self.carrito = None
    

class PostNator:
    @classmethod
    def verificarTrjeta(tarjeta, monto):
        try:
            if tarjeta.saldo < monto:
                raise Excepciones.SaldoInsuficiente()
        except Excepciones.SaldoInsuficiente:
            return False
        else:
            return True
            

import Extras
class Caja:
    def __init__(self):
        self.facturasEmitidas = []

    def checkout(self, carrito):
        costoTotal = 0
        for tupla in carrito.storge:
            producto = tupla[0]
            cantidad = tupla[1]
            costoTotal += producto.precio * cantidad
        return AlmacenadoresDeData.Factura(costoTotal, carrito.storge, Extras.Calendario.dia)


    def cobrar(self, cliente, factura):
        try:
            verificacion = PostNator.verificarTrjeta(cliente.tarjeta, factura.costo)
            if verificacion == False:
                raise Excepciones.SaldoInsuficiente()
        except Excepciones.SaldoInsuficiente:
            print(Excepciones.SaldoInsuficiente.getMsg())
            cliente.carrito.set_storge_vacio()
            cliente.set_carrito()
        else:
            cliente.tarjeta.set_abonar_saldo(factura.costo)
            nuevaFactura = AlmacenadoresDeData.Factura(factura.costo, factura.productos, Extras.Calendario.dia)#factura con fecha emitida
            self.facturasEmitidas.append(nuevaFactura)
            cliente.mis_productos.append(nuevaFactura.productos)



            



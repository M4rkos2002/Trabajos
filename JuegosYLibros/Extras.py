class Reporte:

    @classmethod
    def armar_reporte(cls, facturas):
        facturas.sort()
        return facturas


import AlmacenadoresDeData
class FiltradorLibros:
 
    @classmethod
    def filtrar(cls, condicion):    #La condicion debe ser una funcion, esa lambda o mas dearrollada, es decir un bloque de codigo
        return list(filter(condicion, AlmacenadoresDeData.AlmacenDeLibros.libros))


class Calendario:
    dia = 0
    @classmethod
    def pasar_dia(cls):
        cls.dia += 1
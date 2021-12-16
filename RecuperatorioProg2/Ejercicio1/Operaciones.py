import General



class Operaciones:

    def calcular_reservados(self):
        return len(General.SistemaDeLibros.reservados)
    
    def calcular_no_devueltos(self):
        return len(General.SistemaDeLibros.reservados)

    def calcular_multas_recaudadas(self, bibliotecario):
        counter = 0
        for devoluciones in General.SistemaDeLibros:
            if devoluciones.getMulta() == True:
                counter += 1
        recaudado = bibliotecario.getRecaudado()
        return f"Se recaudaron ${recaudado} de {counter} multas"

    def calcular_devoluciones_del_día(self):
        counter = 0
        for devoluciones in General.SistemaDeLibros.devoluciones:
            if devoluciones.get_multa() == False:
                counter += 1
        return counter

    def calcular_promedio_dias_no_entregado_a_termino(self):
        devueltosFueraDeDia = []
        for devolucion in General.SistemaDeLibros.devoluciones:
            if devolucion.get_multa() == True:
                devueltosFueraDeDia.append(devolucion)
        devueltosEnDia = []
        for value in range(0, General.Calendario.dia + 1):
            for devuelto in devueltosFueraDeDia:   
                devueltosEnEsteDia = []
                if devuelto.get_dia_devuelto() == value:
                    devueltosEnEsteDia.append(devuelto)
            if len(devueltosEnEsteDia) > len(devueltosEnDia):
                devueltosEnDia = devueltosEnEsteDia
        if len(devueltosEnDia) != 0:
            devolucion = devueltosEnDia[0]
            dia = devolucion.get_dia_devuelto()
            return f"Hubieron mas devoluciones el dia {dia}"
        elif len(devueltosEnDia) == 0:
            return "O no hay devoluciones o el programa falló xd"
        


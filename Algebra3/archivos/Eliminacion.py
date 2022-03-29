#Eliminacion
#   
#    -->Eliminacion Logica: la hacemos colocando un valor ilogico como -1 a una cantidad
#                         poniendo una variable extra, en el registro podemos modificarlo, por ejemplo una variable ACTIVO que tome valores 0 o 1
#                         Esta fisicamente pero no logicamente
#
#           1-Dado el codigo del registro lo buscamos
#           2-Hallar el codigo con una busqueda secuencial
#           3-Una vez encontrado le cambiamos la variable lógica que declaramos
#           4-Escribir nuevamente el nuevo registro en el archivo en esa posicion
#           5-Si no se encuentra el registro que le corresponde al codigo, lo elimina
#
#   Cuando encuentre el codigo a modificar, voy a haber hecho un read el puntero se
#   posiciona en el siguiente registro, por lo que nececito hacer un seek en la posicion
#   actual y una cantidad negativa de registro

import os
import struct

def bajas(formato, file_name):
    fp = open(file_name, "r+b")
    cant_registro = os.path.getsie(file_name)//struct.calcsize(formato)
    codigo = input("Ingrese codigo: ")
    for i in range(cant_registro):
        result = fp.read(struct.calcsize(formato))  #obtengo un registro
        resultF = struct.unpack(formato, result)
        if int(codigo) == resultF[0]: #analizo si es el que quiero eliminar
            fp.seek(-struct.calcsize(formato), 1) #me posiciono en la correcta
            precio = result[1] 
            cantidad = -1 #baja logica
            buffer = struct.pack(formato, int(codigo), float(precio), int(cantidad)) #sobreescribo el registro a dar de baja
            ##terminar
        
#
# Otra Eliminacion:
#   
#       -->Modificacion: Es similar a la eliminacion logica
#
#       1-Buscamos con el codigo el registro a eliminar
#       2- lo eliminamos
#
#
#
#
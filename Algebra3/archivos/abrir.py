# find_pointer = open(nombre_archivo, modo) 
# Abre un archivo, el nombre es un String y el modo es qué se le va a hacer
# al archivo, escribir, leer, apendear
# Valores de modo:  rb ==> solo para lectura, si no existe hay error
#                   r+b ==> Para escritura y lectura, si no existe hay error, si existe el punetro se coloca al inicio
#                   wb ==> Se abte en formato binario, si existe lo sobreescribe, si no existe lo crea
#                   w+b ==> escritura y lectura, sobreescribe el arvhivo si ya existe, si no existe lo crea
#                   

#Funcion exists
#   en el paquete os nos permite verificar archivos
#   os.path.exists("nombre") me retorna un booleano dependiendo si existe o no
#   
#

import os
print(os.path.exists("mercado"))  #retorna false porque no existe

#creo el archivo

if os.path.exists("mercado"):
    fp = open("mercado", "r+b") #abro el archivo
else:
    fp = open("mercado", "w+b") #si no existe lo abro y lo creo

print(os.path.exists("mercado"))

#   Metodo write
#       variable.write(secuencia_de_bytes)
#   Con la libreria Struct transformo datos en una secuencia de bytes
#       
#   empaco
#           struct.pack(formato, variable1, variable2, ..., variablen)
#       retorna una secuencia de bytes con esas varaibles
#       
#       para el formato, "l" un entero ==> tantas variables como caracteres
#                        "d" un float
#                      

import struct
contenido = struct.pack("lll", 1,3,4)
contenido2 = struct.pack("ldl", 1,2.3,3)

#Hay que cerrar los archivos 
#     variable.close()
#

# Para leer los caracteres
#       variable = archivo.read(n) siendo n la cantidad de bytes que lee
# 
# Para leer todos los caracteres nececitamos saber cuantos bytes tiene mi texto
#           cantidad_bytes = os.path.getsize(archivo)
#
#


# Esa secuencia de bytes hay que transformarla en datos
#     struct.calcsize(formato)
#
# Ahora debo desempaquetar el contenido
#   tupla = struct.unpack(formato, variable)  debo desempaquetar, devuevle una tupla con los valores
#
#
# Para acceder a los datos del arvhico hay varias formas
#   Reportes: revisar el archivo registro por registro.
#               1-Abrir el archivo
#               2-Hago un rango que accede a los archivos
#               3-Leo el proximo registro y despues procesarlo
#               4-Cierro el archivo
#             Para saber el numero de registros es sabiendo el tamaño del registro,
#              y lo divido por el tamaño del registro
#                   cantidad_bytes_Archivo = os.path.getsize(nombre_Archivo)
#                   cantidad_bytes_Registro = struct.calcsize(formato) 
#               
#               Para leer el archivo se usa:
#                   var = archivo.read(n) lee nbytes desde un archivo, los devuelve como secuencia de bytes
#                   struct.unpack(formato, var) retorna una tupla y me el read no binario
#
#        
#Cada registro tiene el mismo numero de bytes
#
#
#
#
#

import struct
import os

def listador(formato, file_name):
    #calculo el numero de registros
    fp = open(file_name, "rb")
    #Consigo el numero de registros que hay en el archivo
    registro = int((os.path.getsize(file_name))//struct.calcsize(formato))
    #mientras i este en el rango del numero de registros
    for i in range(registro):
        result = fp.read(struct-struct.calcsize(formato))
        resultF = struct.unpack(formato, result)
        print(resultF)
        fp.close





#  Ahora puedo acceder por consulta, o tambien query
#       Consite en buscar el registro, utiliamos busqueda secuencial ya que no está oredenado
#           1- Ingresa el codigo a buscar
#           2- Lee el primer registro
#           3- Si lo encuentra lo devuelve, de lo contrario va al siguiente
#
#

def buscador(formato, file_name):
    fp = open(file_name, "rb") #solo lectura
    cantidad_registros = os.path.getsize(file_name)//struct.calcsize(formato)
    codigo = input("ingrese codigo: ")
    # Hasta haber recorrido la cantidad 
    for i in range(cantidad_registros):
        result = fp.read(struct.calcsize(formato)) #consigo en binario el registro
        #Cada vez que hace un read mueve el puntero al final, lo mismo con un write
        resultF = struct.unpack(formato, result) #lo traduzco
        if int(codigo) == resultF[0]: #La posicion cero de la tupla seria el codgio dado la funcion altas
            return resultF
    fp.close()
    return -1
    
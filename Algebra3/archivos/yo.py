import struct
import os

file_name = input("Ingrese el nombre del archivo: ")

if os.path.exists(file_name):
    file = open(file_name,  "r+b")
    contenido = struct.pack("ldl",1,3.5,4)
    file.write(contenido)
    file.close()

else:
    file = open(file_name, "w+b")
    contenido = struct.pack("lll", 1,2,3)
    file.write(contenido)
    
#No modificiar y leer a al vez
file = open(file_name, "r+b")
tamaño = struct.calcsize("ldl")  #tamaño del tipo de formato en el que guardé el archivo
contenido = file.read(tamaño)    #lector de la secuencia
lecture = struct.unpack("ldl", contenido) #lectura no binaria
file.close()
print(lecture)      #imprimo la lectura

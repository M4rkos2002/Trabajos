import struct
import os

def altas(formato, file_name):
    if os.path.exists(file_name):
        fp = open(file_name, "r+b")  #Lo abre en formato de escritura y lectura
                                    #Siempre que abra el archivo se van a pisar ya que el puntero se posiciona en el principio
                                    #para solucionarlo debo mandar el findPointer al final del archivo
    else:
        fp = open(file_name, "w+b")  #crea el archivo si no existe
    codigo = input("Ingrese codigo del producto: ") # preparo el centinela
    while codigo!= "0":
        precio = input("Ingrese precio: ")
        cantidad = input("Ingresar cantidad: ")
        buffer = struct.pack(formato, int(codigo), float(precio), int(cantidad))
        #Paso el los dato a binario en buffer
        fp.write(buffer)
        #Escribo el archivo con el buffer
        codigo = input("ingresar codigo: ")
    fp.close

archivo = "Hello2"
formato = "ldl"
altas(formato, archivo)

def leer_Archivo(nombre, formato):
    fp = open(nombre, "r+b")
    tamaño = struct.calcsize(formato)
    contenido = fp.read(tamaño)
    lectura = struct.unpack(formato, contenido)
    print(lectura)

leer_Archivo(archivo, formato)

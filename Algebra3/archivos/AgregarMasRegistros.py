# Hay que mover el puntero al final del archivo para que pueda escribir un nuevo registro
#       
#  fp.seex(cantidad, desde) cantidad:Bytes en los que se debe mover el puntero
#                                 desde:Toma el 0, 1 o 2; 0-Desde el inicio
#                                                         1-Desde posicion actual
#                                                         2-Desde el final
#       
#           ejemplo:
#                    fp.seek(os.path.getsize(file_name)) el puntero se mueve todos esos bytes al final
#                             Si le paso un numero de bytes negativo se mueve hacia la izquierda                  
#     
#           Si no se utiliza seek SIEMPRE se coloca al inicio 
#           con fp.tell() me dice en bytes la posicion del puntero
#

import os

def altas(formato, file_name):
    if os.path.exists(file_name):
        fp = open(file_name, "r+b") #abro archivo
    else:
        fp = open(file_name, "w+b") #creo y abro archivo
    #ahora nececito colocar el puntero al final del archivo
    fp.seek(os.path.getsize(file_name), 0) #Desde el principio movete todos los bytes posibles 

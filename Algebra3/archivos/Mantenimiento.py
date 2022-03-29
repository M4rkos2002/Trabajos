#  
#   Mantenimiento:
# 
# 
#       -->Estructuracion: Definir un nuevo archivo con todos los datos pero formato distinto
# 
#       -->Compactacion: Para ahorrar memoria, y todos aquellos archivos activos (sin baja logica)
#                       los paso a un nuevo archivo, sin pasar aquellos dados de baja (con baja logica)
#                   1-Abro archivo
#                   2-Cero una archivo temporal               
#                   3-Leo los registros y aquellos activos los escribo en el temporal
#                   4-Cierro los archivos
#                   5-Elimino el archivo de datos(el viejo) os.delete(file_name)
#                   6-Renombrar el temporal como el archivo a compactar 
# 
# 
# 
# 
# 
# 
# 
# 
# 

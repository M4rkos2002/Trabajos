import Excepciones
import Zona
class Empresa:

    def reubicar(self, zona, monopatines):
        totalMonopatines = len(monopatines)
        for terminal in zona.getTerminales():
            try:
                if totalMonopatines == 0:
                    raise Excepciones.NoHayMonopatinesAReubicar()
                elif Zona.Calendario.hora < 14:
                    raise Excepciones.FueraDeHoraPico()
            except Excepciones.NoHayMonopatinesAReubicar:
                print(Excepciones.NoHayMonopatinesAReubicar.getMsg())
            except Excepciones.FueraDeHoraPico:
                print(Excepciones.FueraDeHoraPico.getMsg())
            else:
                if terminal.getCalidad() == "Alta":
                    monopatinesAcolocar = int(totalMonopatines*0.6) #Puede darme un float
                    terminal.set_total_monopatines(monopatines[:monopatinesAcolocar+1]) #Para que incluya todo el 60%
                    totalMonopatines = int(totalMonopatines*0.6)
                elif terminal.getCalidad() == "Media":
                    monopatinesAcolocar = int(totalMonopatines*0.3)
                    terminal.set_total_monopatines(monopatines[:monopatinesAcolocar+1])
                    totalMonopatines = int(totalMonopatines*0.7)
                elif terminal.getCalidad() == "Baja":
                    monopatinesAcolocar = int(totalMonopatines*0.1)
                    terminal.set_total_monopatines(monopatines[:monopatinesAcolocar])
                    totalMonopatines = int(totalMonopatines*0.9)
            



class Monopatin:

    def __init__(self, ubicacion):
        self.__ubicacion = ubicacion
        self.__uso = False
        self.__disponible = True
        self.__codigo = hash(self)

    def set_estado_a_prestado(self):
        self.__disponible = False
        self.__uso = True
    
    def set_estado_a_devuelto(self):
        self.__disponible = True
        self.__uso = False

    def getEstado(self):
        if self.__uso == True:
            return self.__uso
        elif self.__uso == False:
            return self.__disponible
    
    def getUbicacion(self):
        return self.__ubicacion

    def getCodigo(self):
        return self.__codigo
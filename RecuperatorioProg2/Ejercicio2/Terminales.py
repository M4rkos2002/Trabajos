from abc import ABC, abstractmethod
class Terminal(ABC):

    @abstractmethod
    def dar_monopatin(self):
        pass
    @abstractmethod
    def recibir_monopatin(self):
        pass
    @abstractmethod
    def ubicar_monopatin(self, monopatin):
        pass

import Excepciones
class TerminalAlta(Terminal):

    def __init__(self):
        self.__calidad = "ALTA"
        self.__monopatines = []
        self.__monopatines_en_terminal = []
        self.__en_uso = []
    
    def dar_monopatin(self):
        try:
            if len(self.__monopatines_en_terminal) == 0:
                raise Excepciones.NoHayMonopatinesDisponibles()
        except Excepciones.NoHayMonopatinesDisponibles:
            print(Excepciones.NoHayMonopatinesDisponibles.getMsg())
        monopatin = self.__monopatines_en_terminal[0]
        self.__monopatines_en_terminal.remove(monopatin)
        monopatin.set_estado_a_prestado()
        self.__en_uso.append(monopatin)

    def recibir_monopatin(self, monopatin):
        monopatin.set_estado_a_devuelto()
        self.__monopatines_en_terminal.append(monopatin)
        self.__en_uso.remove(monopatin)
        
    def ubicar_monopatin(self, codigo):
        try:
            for monopatin in self.__monopatines:
                if monopatin.getCodigo() == codigo:
                    return monopatin.getUbicacion()
            raise Excepciones.MonopatinNoExiste()
        except Excepciones.MonopatinNoExiste:
            print(Excepciones.MonopatinNoExiste.getMsg())

    def getCalidad(self):
        return self.__calidad

    def set_total_monopatines(self, monopatines):
        self.__monopatines = monopatines


class TerminalMedia(Terminal):
    def __init__(self):
        self.__calidad = "MEDIA"
        self.__monopatines_en_terminal = []
        self.__monopatines = []
        self.__en_uso = []
    def dar_monopatin(self):
        try:
            if len(self.__monopatines_en_terminal) == 0:
                raise Excepciones.NoHayMonopatinesDisponibles()
        except Excepciones.NoHayMonopatinesDisponibles:
            print(Excepciones.NoHayMonopatinesDisponibles.getMsg())
        monopatin = self.__monopatines_en_terminal[0]
        self.__monopatines_en_terminal.remove(monopatin)
        monopatin.set_estado_a_prestado()
        self.__en_uso.append(monopatin)


    def recibir_monopatin(self, monopatin):
        monopatin.set_estado_a_devuelto()
        self.__monopatines_en_terminal.append(monopatin)
        self.__en_uso.remove(monopatin)
        
    def ubicar_monopatin(self, codigo):
        try:
            for monopatin in self.__monopatines:
                if monopatin.getCodigo() == codigo:
                    return monopatin.getUbicacion()
            raise Excepciones.MonopatinNoExiste()
        except Excepciones.MonopatinNoExiste:
            print(Excepciones.MonopatinNoExiste.getMsg())

    def getCalidad(self):
        return self.__calidad
    
    def set_total_monopatines(self, monopatines):
        self.__monopatines = monopatines

class TerminalBaja(Terminal):
    def __init__(self):
        self.__calidad = "BAJA"
        self.__monopatines_en_terminal = []
        self.__monopatines = []
        self.__en_uso = []
    
    def dar_monopatin(self):
        try:
            if len(self.__monopatines_en_terminal) == 0:
                raise Excepciones.NoHayMonopatinesDisponibles()
        except Excepciones.NoHayMonopatinesDisponibles:
            print(Excepciones.NoHayMonopatinesDisponibles.getMsg())
        monopatin = self.__monopatines_en_terminal[0]
        self.__monopatines_en_terminal.remove(monopatin)
        monopatin.set_estado_a_prestado()
        self.__en_uso.append(monopatin)

    def recibir_monopatin(self, monopatin):
        monopatin.set_estado_a_devuelto()
        self.__monopatines_en_terminal.append(monopatin)
        self.__en_uso.remove(monopatin)
        
    def ubicar_monopatin(self, codigo):
        try:
            for monopatin in self.__monopatines:
                if monopatin.getCodigo() == codigo:
                    return monopatin.getUbicacion()
            raise Excepciones.MonopatinNoExiste()
        except Excepciones.MonopatinNoExiste:
            print(Excepciones.MonopatinNoExiste.getMsg())

    def getCalidad(self):
        return self.__calidad
    
    def set_total_monopatines(self, monopatines):
        self.__monopatines = monopatines
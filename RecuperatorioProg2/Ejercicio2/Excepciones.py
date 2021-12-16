class NoDisponible(Exception):
    msg = "Monopatin no disponible"
    @classmethod
    def getMsg(cls):
        return cls.msg

class NoHayMonopatinesDisponibles(Exception):
    msg = "No hay monopatines disponibles"
    @classmethod
    def getMsg(cls):
        return cls.msg

class MonopatinNoExiste(Exception):
    msg = "El monopatin no existe"
    @classmethod
    def getMsg(cls):
        return cls.msg

class NoHayMonopatinesAReubicar(Exception):
    msg = "No hay monopatines para reubicar"
    @classmethod
    def getMsg(cls):
        return cls.msg

class FueraDeHoraPico(Exception):
    msg = "Fuera de hora Pico, espere a las 14hs"
    @classmethod
    def getMsg(cls):
        return cls.msg
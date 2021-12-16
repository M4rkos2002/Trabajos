class EnergiaMenorOIgual1(Exception):
    msg = "La energia colocada debe ser mayor a 1"
    @classmethod
    def getMsg(cls):
        return cls.msg

class BlindajeCubreTodoDano(Exception):
    msg = "La armadura absorve todo el daño"
    @classmethod
    def getMsg(cls):
        return cls.msg

class ObjetoNoExiste(ValueError):
    msg = "Este objeto no existe"
    @classmethod
    def getMsg(cls):
        return cls.msg

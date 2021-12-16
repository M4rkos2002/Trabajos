class LibroNoExiste(ValueError):
    msg = "Este libro no existe"
    @classmethod
    def getMsg(cls):
        return cls.msg

class SaldoInsuficiente(Exception):
    msg = "Saldo Insuficiente"
    @classmethod
    def getMsg(cls):
        return cls.msg
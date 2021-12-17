
class NoHayReportesDeLlamadas(Exception):
    msg = "Este cliente no relaizó llamadas"
    @classmethod
    def getMsg(cls):
        return cls.msg
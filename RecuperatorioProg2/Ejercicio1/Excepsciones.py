class LibroNoExiste(Exception):
    msg = "Este libro no Existe"
    @classmethod
    def getMsg(self):
        return self.msg
    
class LibroExistePeroEstaReservado(Exception):
    msg = "Este libro existe pero está reservado"
    @classmethod
    def getMsg(self):
        return self.msg

class NoEntregaATiempo(Exception):
    msg = "Este libro no fue entregado a tiempo se cobrará multa= $100"
    @classmethod
    def getMsg(self):
        return self.msg
        
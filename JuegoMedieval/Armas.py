
class Arma:
    def __init__(self, dano, tipo):
        self.dano = dano
        self.tipo = tipo

    def getDano(self):
        return self.dano
    
    def getTipo(self):
        return self.tipo


class Espada(Arma):

    def __init__(self, dano, tipo):
        super().__init__(dano, tipo)

    def __repr__(self):
        return f"Espada de {self.getTipo()}"
    
    def getDano(self):
        return super().getDano()
    
    def getTipo(self):
        return super().getTipo()

class Basculo(Arma):
    def __init__(self, dano, tipo):
        super().__init__(dano, tipo)
    
    def __repr__(self):
        return f"Basculo de {self.getTipo()}"
    
    def getDano(self):
        return super().getDano()

    def getTipo(self):
        return super().getTipo()

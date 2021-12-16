class Pregunta:
    def __init__(self, enunciado, rta, tipo):
        self.enunciado = enunciado
        self.rta = rta
        self.tipo = tipo
    
    def __repr__(self):
        return f"{self.enucniado}"
    
    def getRta(self):
        return self.rta

   

class Texto(Pregunta):

    def __init__(self, enunciado, rta):
        super().__init__(enunciado, rta, tipo=Texto)
    
    def __repr__(self):
        return super().__repr__()

    def getRta(self):
        return super().getRta()
    


class Numerica(Pregunta):

    def __init__(self, enunciado, rta):
        super().__init__(enunciado, rta, tipo="Numerica")

    def __repr__(self):
        return super().__repr__()

    def getRta(self):
        return super().getRta()
    


class MultipleChoice(Pregunta):

    def __init__(self, enunciado, rta):
        super().__init__(enunciado, rta, tipo="MultipleChoice")

    def __repr__(self):
        return super().__repr__()

    def getRta(self):
        return super().getRta()

    

class VerdaderoOFalse(Pregunta):
    def __init__(self, enunciado, rta):
        super().__init__(enunciado, rta, tipo="VerdaderoOFalso")
    
    def __repr__(self):
        return super().__repr__()
        
    def getRta(self):
        return super().getRta()
    
    
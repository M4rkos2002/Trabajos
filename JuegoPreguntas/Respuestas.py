class Respuesta:
    def __init__(self, rta):
        self.rta = rta
    
    def getRta(self):
        return self.rta
    
class RtaTexto(Respuesta):
    def __init__(self, rta):
        super().__init__(self, rta)
        self.rta = str(super().getRta())
    
    def getRta(self):
        return self.rta
    
class RtaNumerica(Respuesta):
    def __init__(self, rta):
        super().__init__(rta)
        self.rta = float(super().getRta())
    
    def getRta(self):
        return self.rta
    
class RtaMultipleChoice(Respuesta):
    def __init__(self, rta, rta2):
        super().__init__(rta)
        self.rta2 = rta2
        self.rtas = [super().getRta(),rta2]
    
    def getRta(self):
        return self.rtas
    
class RtaChoice(Respuesta):
    def __init__(self, rta):
        super().__init__(rta)
        self.rta = str(super().getRta())
    
    def getRta(self):
        return self.rta


class RtaVerdaderoOFalso(Respuesta):
    def __init__(self, rta):
        super().__init__(rta)
        self.rta = bool(rta)
    
    def getRta(self):
        return self.rta
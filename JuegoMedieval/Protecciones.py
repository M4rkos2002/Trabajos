class Proteccion:

    def __init__(self, proteccion, durabilidad):
        self.proteccion = proteccion
        self.durabilidad = durabilidad

    def getProteccion(self):
        return self.proteccion
    
    def set_reducir_durabilidad(self, value):
        self.durabilidad -= value

class Armadura(Proteccion):
    
    def __init__(self, proteccion, durabilidad):
        super().__init__(proteccion, durabilidad)
    
    def getProteccion(self):
        return super().getProteccion()
    
    def set_reducir_durabilidad(self, value):
        return super().set_reducir_durabilidad(value)

class Casco(Proteccion):
    def __init__(self, proteccion, durabilidad):
        super().__init__(proteccion, durabilidad)
    
    def getProteccion(self):
        return super().getProteccion()
    
    def set_reducir_durabilidad(self, value):
        return super().set_reducir_durabilidad(value)

class Escudo(Proteccion):
    def __init__(self, proteccion, durabilidad):
        super().__init__(proteccion, durabilidad)
    
    def getProteccion(self):
        return super().getProteccion()
    
    def set_reducir_durabilidad(self, value):
        return super().set_reducir_durabilidad(value)
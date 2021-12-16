import Excepciones
class Criatura:
    def __init__(self, xpdrop, dano, salud):
        self.xpdrop = xpdrop
        self.dano = dano
        self.salud = salud
    
    def atacar(self, personaje):
        if personaje.getArmadura() == None:
            personaje.set_reducir_salud(self.dano)
        elif personaje.getArmadura() != None:
            armadura = personaje.getArmadura()
            blindaje = armadura.getProteccion()
            try:
                dano = self.dano - blindaje
                if dano <= 0:
                    raise Excepciones.BlindajeCubreTodoDano()
            except Excepciones.BlindajeCubreTodoDano:
                print(Excepciones.BlindajeCubreTodoDano.getMsg())
                armadura.set_reducir_durabilidad(self.dano)
            else:
                personaje.set_reducir_salud(dano)

    def getSalud(self):
        return self.salud

    def set_salud(self, value):
        self.salud -= value

    def getXp(self):
        return self.xpdrop



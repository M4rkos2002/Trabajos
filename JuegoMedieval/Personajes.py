import Protecciones
import Armas
import Excepciones

class Personaje:
    def __init__(self, salud, xp):
        self.salud = salud
        self.xp = 0
        self.inventario = []
        self.arma = None
        self.armadura = None
    
    def equiparse(self, objeto):
        if isinstance(objeto, Protecciones.Proteccion):
            self.armadura = objeto
        elif isinstance(objeto, Armas.Arma):
            self.arma = objeto
        else:
            return "No es un objeto equipable"

    def atacar(self, enemigo):
        pass

    def abrirInventario(self):
        counter = 1
        for item in self.inventario:
            print(counter + "- " + item)
            counter += 1

    def añadir_a_Inventario(self, objeto):
        self.inventario.append(objeto)
    
    def retirar_de_Inventario(self, objeto):
        try:
            self.inventario.remove(objeto)
        except Excepciones.ObjetoNoExiste:
            print(Excepciones.ObjetoNoExiste.getMsg())
    
    def getArma(self):
        return self.arma

    def set_salud(self, value):
        self.salud += value

    def getArmadura(self):
        return self.armadura

    def set_reducir_salud(self, value):
        self.salud -= value
    
    def set_xp(self, value):
        self.xp += value

class Guerrero(Personaje):

    def __init__(self, danoFisico,salud):
        super().__init__(salud)
        self.danoFisico = danoFisico
        
    def equiparse(self, objeto):
        return super().equiparse(objeto)
    
    def atacar(self, enemigo):
        if super().getArma() == None:
            enemigo.set_salud(self.danoFisico)
        elif super().getArma() != None:
            arma = super().getArma()
            if isinstance(arma, Armas.Basculo):
                dano = arma.getDano() * 0.5
            enemigo.set_salud(dano + self.danoFisico)
        if enemigo.getSalud() <= 0:
            self.set_xp(enemigo.getXp())
    
    def abrirInventario(self):
        return super().abrirInventario()
    
    def getArmadura(self):
        return super().getArmadura()
    
    def set_salud(self, value):
        return super().set_salud(value)
    
    def set_reducir_salud(self, value):
        return super().set_reducir_salud(value)

    def añañadir_a_Inventario(self, objeto):
        return super().añadir_a_Inventario(objeto)
    
    def retirar_de_Inventario(self, objeto):
        return super().retirar_de_Inventario(objeto)

class Hechizero(Personaje):

    def __init__(self, energia, danoMagico, salud):
        super().__init__(salud)
        self.energia = energia
        self.danoMagico = danoMagico
        self.carga = self.danoMagico

    def equiparse(self, objeto):
        return super().equiparse(objeto)
    
    def atacar(self, enemigo):
        if super().getArma() == None:
            enemigo.set_salud(self.carga)
        elif super().getArma() != None:
            arma = super().getArma()
            dano = self.carga
            if isinstance(arma, Armas.Espada):
                dano = self.carga * 0.5
            enemigo.set_salud(dano)
        self.carga = self.danoMagico
        if enemigo.getSalud() <= 0:
            self.set_xp(enemigo.getXp())

    def abrirInventario(self):
        return super().abrirInventario()

    def PotenciarAtaque(self, energia):
        try:
            if energia <= 1:
                raise Excepciones.EnergiaMenorOIgual1()
        except Excepciones.EnergiaMenorOIgual1:
            print(Excepciones.EnergiaMenorOIgual1.getMsg())
        else:
            self.energia -= energia
            self.carga = self.carga * energia

    def getArmadura(self):
        return super().getArmadura()
    
    def set_salud(self, value):
        return super().set_salud(value)
    
    def set_reducir_salud(self, value):
        return super().set_reducir_salud(value)

    def añañadir_a_Inventario(self, objeto):
        return super().añadir_a_Inventario(objeto)
    
    def retirar_de_Inventario(self, objeto):
        return super().retirar_de_Inventario(objeto)


class Curandero(Personaje):
    def __init__(self, salud, dano):
        super().__init__(salud)
        self.dano = dano
        
    def equiparse(self, objeto):
        return super().equiparse(objeto)
    
    def atacar(self, enemigo):
        if super().getArma() == None:
            enemigo.set_salud(self.dano)
        elif super().getArma() != None:
            arma = super().getArma()
            enemigo.set_salud(arma.getDano())
        if enemigo.getSalud() <= 0:
            self.set_xp(enemigo.getXp())
    
    def abrirInventario(self):
        return super().abrirInventario()
    
    def Curar(self, aliado, value):
        aliado.set_salud(value)  

    def getArmadura(self):
        return super().getArmadura()   

    def set_reducir_salud(self, value):
        return super().set_reducir_salud(value)
    
    def añañadir_a_Inventario(self, objeto):
        return super().añadir_a_Inventario(objeto)
    
    def retirar_de_Inventario(self, objeto):
        return super().retirar_de_Inventario(objeto)
        
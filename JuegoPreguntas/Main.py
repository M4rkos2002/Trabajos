class Juego:
    def __init__(self, puntajeDeAprobacion):
        self.puntajeDeAprobacion = puntajeDeAprobacion
        self.pregutnas = []
        self.correctas = []
        self.incorectas = []

    def presentar(self):
        for pregunta in self.preguntas:
            print(pregunta)

    def verificar_Respuesta(self, pregunta, rtaDada):
        rtaCorrecta = pregunta.getRta()
        if rtaCorrecta == rtaDada:
            for i in self.preguntas:
                if i == pregunta:
                    self.preguntas.remove(pregunta)
            self.correctas.append(pregunta)
        elif rtaCorrecta != rtaDada:
            for i in self.preguntas:
                if i == pregunta:
                    self.preguntas.remove(pregunta)
            self.incorrectas.append(pregunta)

    def verificar_victoria(self, usuario):
        if len(self.pregutnas) != 0:
            return "Debe terminar de responder"
        elif len(self.pregutnas) == 0:
            if len(self.correctas) >= self.puntajeDeAprobacion:
                usuario.set_victorias()
                return f"Ha aprobado con {len(self.correctas)} puntos"
            elif len(self.correctas) < self.puntajeDeAprobacion:
                return f"Ha desaprobado con {len(self.correctas)} puntos"



class Usuario:

    def __init__(self):
        self.vitorias = 0

    def responder(self,juego, rta):
        juego.verificarRespuesta(rta)

    def set_victorias(self):
        self.victorias += 1
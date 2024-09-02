class Pregunta:
    def __init__(self, enunciado, esRequerida=False, ayuda=None):
        self._enunciado = enunciado
        self._esRequerida = esRequerida
        self._ayuda = ayuda
        self._alternativas = []


    #consulta el enunciado de la pregunta
    def getEnunciado(self):
        return self._enunciado

    #modifica el enunciado de la pregunta
    def modificarEnunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    #consulta la ayuda de la pregunta
    def getAyuda(self):
        return self._ayuda

    #modifica la ayuda de la pregunta
    def modificarAyuda(self, nuevo_ayuda):
        self._ayuda = nuevo_ayuda


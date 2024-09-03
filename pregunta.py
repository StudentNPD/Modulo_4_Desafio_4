from alternativa import Alternativa


class Pregunta:
    def __init__(self, enunciado, esRequerida=False, ayuda=None):
        self._enunciado = enunciado
        self._esRequerida = esRequerida
        self._ayuda = ayuda
        self._alternativas = []

    # consulta el enunciado de la pregunta
    def getEnunciado(self):
        return self._enunciado

    # modifica el enunciado de la pregunta
    def modificarEnunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    # consulta la ayuda de la pregunta
    def getAyuda(self):
        return self._ayuda

    # modifica la ayuda de la pregunta
    def modificarAyuda(self, nuevo_ayuda):
        self._ayuda = nuevo_ayuda

    # consulta si es requerida la pregunta (ojo es boleano)
    def getEsRequerida(self):
        return self._esRequerida

    # modifica si es requerida la pregunta (ojo es boleano)
    def setEsRequerida(self, esRequerida):
        self._es_requerida = esRequerida

    # consulta las alternativas de la pregunta (tipo lista)
    def getAlternativas(self):
        return self._alternativas

    # Agrega nueva alternativa a la pregunta
    def agregar_alternativa(self, alternativa_dict):
        alternativa = Alternativa(
            alternativa_dict["contenido"], alternativa_dict.get("ayuda")
        )
        self._alternativas.append(alternativa)

    # Muestra la pregunta, su enunciado, ayuda y sus alternativas
    def mostrar(self):
        muestra = f"Enunciado: {self._enunciado}"
        if self._ayuda:
            muestra += f"\nAyuda: {self._ayuda}"
        muestra += f"\nRequerida: {'Sí' if self._esRequerida else 'No'}"
        muestra += "\nAlternativas:"
        # recorre las alternativas mostrandolas
        for i, alternativa in enumerate(self._alternativas, 1):
            muestra += f"\n  {i}. {alternativa.mostrar()}"
        return muestra

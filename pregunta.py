from alternativa import Alternativa


class Pregunta:
    def __init__(self, enunciado, esRequerida=False, ayuda=None):
        """Inicializa una instancia de la clase Pregunta.

        Args:
            enunciado (str): El enunciado de la pregunta.
            esRequerida (bool, optional): Indica si la pregunta es requerida. Por defecto es False.
            ayuda (str, optional): Texto de ayuda adicional para la pregunta. Por defecto es None.
        """
        self._enunciado = enunciado
        self._esRequerida = esRequerida
        self._ayuda = ayuda
        self._alternativas = []

    def getEnunciado(self):
        """Obtiene el enunciado de la pregunta.

        Returns:
            str: El enunciado actual de la pregunta.
        """
        return self._enunciado

    def modificarEnunciado(self, nuevo_enunciado):
        """Modifica el enunciado de la pregunta.

        Args:
            nuevo_enunciado (str): El nuevo enunciado que reemplazará al existente.
        """
        self._enunciado = nuevo_enunciado

    def getAyuda(self):
        """Obtiene el texto de ayuda de la pregunta.

        Returns:
            str: El texto de ayuda actual de la pregunta, o None si no existe.
        """
        return self._ayuda

    def modificarAyuda(self, nueva_ayuda):
        """Modifica el texto de ayuda de la pregunta.

        Args:
            nueva_ayuda (str): El nuevo texto de ayuda que reemplazará al existente.
        """
        self._ayuda = nueva_ayuda

    def getEsRequerida(self):
        """Consulta si la pregunta es requerida.

        Returns:
            bool: True si la pregunta es requerida, False en caso contrario.
        """
        return self._esRequerida

    def setEsRequerida(self, esRequerida):
        """Modifica si la pregunta es requerida.

        Args:
            esRequerida (bool): Indica si la pregunta debe ser requerida.
        """
        self._esRequerida = esRequerida

    def getAlternativas(self):
        """Obtiene la lista de alternativas de la pregunta.

        Returns:
            list: Una lista de objetos de tipo Alternativa asociados a la pregunta.
        """
        return self._alternativas

    def agregar_alternativa(self, alternativa_dict):
        """Agrega una nueva alternativa a la pregunta.

        Args:
            alternativa_dict (dict): Un diccionario que contiene el contenido de la alternativa y
            opcionalmente su texto de ayuda, con las claves 'contenido' y 'ayuda'.
        """
        alternativa = Alternativa(
            alternativa_dict["contenido"], alternativa_dict.get("ayuda")
        )
        self._alternativas.append(alternativa)

    def mostrar(self):
        """Muestra el enunciado, la ayuda, si es requerida y las alternativas de la pregunta.

        Returns:
            str: Una cadena que contiene el enunciado, la ayuda, si es requerida, y las alternativas de la pregunta.
        """
        muestra = f"Enunciado: {self._enunciado}"
        if self._ayuda:
            muestra += f"\nAyuda: {self._ayuda}"
        muestra += f"\nRequerida: {'Sí' if self._esRequerida else 'No'}"
        muestra += "\nAlternativas:"
        for i, alternativa in enumerate(self._alternativas, 1):
            muestra += f"\n  {i}. {alternativa.mostrar()}"
        return muestra

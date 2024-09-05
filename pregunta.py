from alternativa import Alternativa

class Pregunta:
    """Representa una pregunta que puede incluir un enunciado, si es requerida, ayuda y una lista de alternativas.

    Esta clase permite manejar una pregunta con su respectivo enunciado, 
    si es requerida, ayuda adicional y varias alternativas. Proporciona 
    métodos para modificar y obtener estos atributos, así como para agregar 
    alternativas a la pregunta.

    Args:
        enunciado (str): El enunciado de la pregunta.
        esRequerida (bool, optional): Indica si la pregunta es obligatoria. 
            Por defecto es False.
        ayuda (str, optional): Información adicional o ayuda relacionada 
            con la pregunta. Por defecto es None.
    """

    def __init__(self, enunciado, esRequerida=False, ayuda=None):
        """Inicializa una nueva instancia de la clase Pregunta.

        Args:
            enunciado (str): El enunciado de la pregunta.
            esRequerida (bool, optional): Indica si la pregunta es obligatoria. 
                Por defecto es False.
            ayuda (str, optional): Información adicional o ayuda relacionada 
                con la pregunta. Por defecto es None.
        """
        self._enunciado = enunciado
        self._esRequerida = esRequerida
        self._ayuda = ayuda
        self._alternativas = []

    def getEnunciado(self):
        """Obtiene el enunciado de la pregunta.

        Returns:
            str: El enunciado de la pregunta.
        """
        return self._enunciado

    def modificarEnunciado(self, nuevo_enunciado):
        """Modifica el enunciado de la pregunta.

        Args:
            nuevo_enunciado (str): El nuevo enunciado que reemplazará al actual.
        """
        self._enunciado = nuevo_enunciado

    def getAyuda(self):
        """Obtiene la ayuda asociada a la pregunta.

        Returns:
            str: La ayuda asociada a la pregunta. Puede ser None si no 
            se ha definido ninguna ayuda.
        """
        return self._ayuda

    def modificarAyuda(self, nueva_ayuda):
        """Modifica la ayuda asociada a la pregunta.

        Args:
            nueva_ayuda (str): La nueva ayuda que reemplazará a la ayuda actual.
        """
        self._ayuda = nueva_ayuda

    def getEsRequerida(self):
        """Indica si la pregunta es requerida.

        Returns:
            bool: True si la pregunta es obligatoria, False en caso contrario.
        """
        return self._esRequerida

    def setEsRequerida(self, esRequerida):
        """Modifica el estado de si la pregunta es requerida.

        Args:
            esRequerida (bool): El nuevo estado que indica si la pregunta es 
                obligatoria (True) o no (False).
        """
        self._esRequerida = esRequerida

    def getAlternativas(self):
        """Obtiene la lista de alternativas asociadas a la pregunta.

        Returns:
            list: Una lista de instancias de la clase Alternativa.
        """
        return self._alternativas

    def agregar_alternativa(self, alternativa_dict):
        """Agrega una nueva alternativa a la lista de alternativas de la pregunta.

        Args:
            alternativa_dict (dict): Un diccionario que contiene los datos de 
                la nueva alternativa. Debe tener una clave "contenido" y 
                opcionalmente una clave "ayuda".
        """
        alternativa = Alternativa(
            alternativa_dict["contenido"], alternativa_dict.get("ayuda")
        )
        self._alternativas.append(alternativa)

    def mostrar(self):
        """Muestra el enunciado, la ayuda, el estado de si es requerida y las alternativas de la pregunta.

        Returns:
            str: Una cadena que representa el enunciado de la pregunta, si es 
            requerida, la ayuda asociada (si la hay) y las alternativas 
            disponibles.
        """
        muestra = f"Enunciado: {self._enunciado}"
        if self._ayuda:
            muestra += f"\nAyuda: {self._ayuda}"
        muestra += f"\nRequerida: {'Sí' si self._esRequerida else 'No'}"
        muestra += "\nAlternativas:"
        for i, alternativa in enumerate(self._alternativas, 1):
            muestra += f"\n  {i}. {alternativa.mostrar()}"
        return muestra

class Alternativa:
    def __init__(self, contenido, ayuda=None):
        """Inicializa una instancia de la clase Alternativa.

        Args:
            contenido (str): El contenido principal de la alternativa.
            ayuda (str, optional): Texto de ayuda adicional para la alternativa.
            Por defecto es None.
        """
        self._contenido = contenido
        self._ayuda = ayuda

    def getContenido(self):
        """Obtiene el contenido de la alternativa.

        Returns:
            str: El contenido actual de la alternativa.
        """
        return self._contenido

    def modificarContenido(self, nuevo_contenido):
        """Modifica el contenido de la alternativa.

        Args:
            nuevo_contenido (str): El nuevo contenido que reemplazará al existente.
        """
        self._contenido = nuevo_contenido

    def getAyuda(self):
        """Obtiene el texto de ayuda de la alternativa.

        Returns:
            str: El texto de ayuda actual de la alternativa, o None si no existe.
        """
        return self._ayuda

    def modificarAyuda(self, nueva_ayuda):
        """Modifica el texto de ayuda de la alternativa.

        Args:
            nueva_ayuda (str): El nuevo texto de ayuda que reemplazará al existente.
        """
        self._ayuda = nueva_ayuda

    def mostrar(self):
        """Muestra el contenido y el texto de ayuda de la alternativa.

        Returns:
            str: Una cadena que contiene el contenido y, si existe, el texto de ayuda.
        """
        muestra = f"Contenido: {self._contenido}"
        if self._ayuda:
            muestra += f"\nAyuda: {self._ayuda}"
        return muestra

    # print(mostrar)

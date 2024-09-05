class Alternativa:
    """Representa una alternativa con contenido y una posible ayuda adicional.

    Esta clase permite almacenar un contenido y una ayuda opcional que
    puede ser utilizada como información adicional. Proporciona métodos 
    para obtener y modificar tanto el contenido como la ayuda.

    Args:
        contenido (str): El contenido principal de la alternativa.
        ayuda (str, optional): Información adicional o ayuda relacionada 
            con la alternativa. Por defecto es None.
    """

    def __init__(self, contenido, ayuda=None):
        """Inicializa una nueva instancia de la clase Alternativa.

        Args:
            contenido (str): El contenido principal de la alternativa.
            ayuda (str, optional): Información adicional o ayuda relacionada 
                con la alternativa. Por defecto es None.
        """
        self._contenido = contenido
        self._ayuda = ayuda

    def getContenido(self):
        """Obtiene el contenido de la alternativa.

        Returns:
            str: El contenido de la alternativa.
        """
        return self._contenido

    def modificarContenido(self, nuevo_contenido):
        """Modifica el contenido de la alternativa.

        Args:
            nuevo_contenido (str): El nuevo contenido que reemplazará al 
                contenido actual de la alternativa.
        """
        self._contenido = nuevo_contenido

    def getAyuda(self):
        """Obtiene la ayuda asociada a la alternativa.

        Returns:
            str: La ayuda asociada a la alternativa. Puede ser None si no 
            se ha definido ninguna ayuda.
        """
        return self._ayuda

    def modificarAyuda(self, nueva_ayuda):
        """Modifica la ayuda asociada a la alternativa.

        Args:
            nueva_ayuda (str): La nueva ayuda que reemplazará a la ayuda 
                actual de la alternativa.
        """
        self._ayuda = nueva_ayuda

    def mostrar(self):
        """Muestra el contenido y la ayuda de la alternativa.

        Returns:
            str: Una cadena que representa el contenido de la alternativa y,
            si está disponible, la ayuda asociada.
        """
        muestra = f"Contenido: {self._contenido}"
        if self._ayuda:
            muestra += f"\nAyuda: {self._ayuda}"
        return muestra


    # print(mostrar)

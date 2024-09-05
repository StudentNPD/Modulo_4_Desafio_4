class ListadoRespuestas:
    """Representa un conjunto de respuestas proporcionadas por un usuario en una encuesta.

    Esta clase almacena las respuestas de un usuario a las preguntas de una encuesta, 
    permitiendo acceder al usuario y a su lista de respuestas.

    Args:
        usuario: Una instancia de la clase Usuario que representa al usuario 
            que contestó la encuesta.
        lista_respuestas (list): Una lista que contiene las respuestas dadas 
            por el usuario a las preguntas de la encuesta.
    """

    def __init__(self, usuario, lista_respuestas):
        """Inicializa una nueva instancia de la clase ListadoRespuestas.

        Args:
            usuario: El usuario que ha proporcionado las respuestas.
            lista_respuestas (list): Una lista con las respuestas del usuario.
        """
        self.__usuario = usuario
        self.__lista_respuestas = lista_respuestas

    @property
    def getUsuario(self):
        """Obtiene el usuario que proporcionó las respuestas.

        Returns:
            Usuario: La instancia del usuario que contestó la encuesta.
        """
        return self.__usuario

    @property
    def getRespuestas(self):
        """Obtiene la lista de respuestas proporcionadas por el usuario.

        Returns:
            list: Una lista con las respuestas dadas por el usuario.
        """
        return self.__lista_respuestas

from pregunta import Pregunta

class Encuesta:
    """Representa una encuesta con un nombre, un listado de preguntas y un listado de respuestas.

    Esta clase permite gestionar una encuesta, que incluye un nombre, un 
    conjunto de preguntas y un registro de las respuestas dadas por los usuarios.

    Args:
        nombre_encuesta (str): El nombre de la encuesta.
        listado_preguntas (list[Pregunta]): Una lista de instancias de la 
            clase Pregunta que conforman la encuesta.
    """

    def __init__(self, nombre_encuesta, listado_preguntas):
        """Inicializa una nueva instancia de la clase Encuesta.

        Args:
            nombre_encuesta (str): El nombre de la encuesta.
            listado_preguntas (list[Pregunta]): Una lista de preguntas que 
                conforman la encuesta.
        """
        self._nombre_encuesta = nombre_encuesta
        self._listado_preguntas = listado_preguntas
        self._listado_respuestas = []

    def getNombre(self):
        """Obtiene el nombre de la encuesta.

        Returns:
            str: El nombre de la encuesta.
        """
        return self._nombre_encuesta

    def setNombre(self, nuevo_nombre):
        """Modifica el nombre de la encuesta.

        Args:
            nuevo_nombre (str): El nuevo nombre que reemplazará al actual.
        """
        self._nombre_encuesta = nuevo_nombre

    def agregar_respuestas(self, listado_respuestas):
        """Agrega un conjunto de respuestas al listado de respuestas de la encuesta.

        Args:
            listado_respuestas: Una instancia que contiene las respuestas 
                proporcionadas por un usuario a las preguntas de la encuesta.
        """
        self._listado_respuestas.append(listado_respuestas)

    def getListadoPreguntas(self):
        """Obtiene el listado de preguntas de la encuesta.

        Returns:
            list[Pregunta]: La lista de preguntas que conforman la encuesta.
        """
        return self._listado_preguntas

    def mostrar(self):
        """Muestra el nombre de la encuesta y todas sus preguntas.

        Returns:
            str: Una cadena que representa el nombre de la encuesta y una 
            lista de las preguntas contenidas en ella.
        """
        muestra = f"Nombre de la encuesta: {self._nombre_encuesta}\n"
        muestra += "Preguntas:\n"
        for i, pregunta in enumerate(self._listado_preguntas, 1):
            muestra += f"{i}. {pregunta.mostrar()}\n"
        return muestra


class EncuestaLimitadaEdad(Encuesta):
    """Representa una encuesta limitada por un rango de edad de los usuarios.

    Esta clase extiende la funcionalidad de la clase Encuesta para imponer 
    restricciones basadas en la edad de los usuarios. Solo se aceptan 
    respuestas de usuarios dentro del rango de edad especificado.

    Args:
        nombre_encuesta (str): El nombre de la encuesta.
        listado_preguntas (list[Pregunta]): Una lista de preguntas que 
            conforman la encuesta.
        edad_minima (int): La edad mínima requerida para participar en la encuesta.
        edad_maxima (int): La edad máxima permitida para participar en la encuesta.
    """

    def __init__(self, nombre_encuesta, listado_preguntas, edad_minima, edad_maxima):
        """Inicializa una nueva instancia de la clase EncuestaLimitadaEdad.

        Args:
            nombre_encuesta (str): El nombre de la encuesta.
            listado_preguntas (list[Pregunta]): Una lista de preguntas que 
                conforman la encuesta.
            edad_minima (int): La edad mínima requerida para participar.
            edad_maxima (int): La edad máxima permitida para participar.
        """
        super().__init__(nombre_encuesta, listado_preguntas)
        self._edad_minima = edad_minima
        self._edad_maxima = edad_maxima

    def agregar_respuestas(self, listado_respuestas):
        """Agrega respuestas a la encuesta si el usuario está dentro del rango de edad permitido.

        Args:
            listado_respuestas: Una instancia que contiene las respuestas 
                proporcionadas por un usuario a las preguntas de la encuesta.

        Raises:
            ValueError: Si el usuario no está dentro del rango de edad permitido.
        """
        if self._edad_minima <= listado_respuestas.getUsuario.getEdad <= self._edad_maxima:
            super().agregar_respuestas(listado_respuestas)
        else:
            print("El usuario no cumple con el rango de edad para esta encuesta.")


class EncuestaLimitadaRegion(Encuesta):
    """Representa una encuesta limitada por regiones geográficas de los usuarios.

    Esta clase extiende la funcionalidad de la clase Encuesta para imponer 
    restricciones basadas en la región geográfica de los usuarios. Solo se 
    aceptan respuestas de usuarios que pertenecen a las regiones especificadas.

    Args:
        nombre_encuesta (str): El nombre de la encuesta.
        listado_preguntas (list[Pregunta]): Una lista de preguntas que 
            conforman la encuesta.
        regiones (list[int]): Una lista de regiones válidas para participar 
            en la encuesta.
    """

    def __init__(self, nombre_encuesta, listado_preguntas, regiones):
        """Inicializa una nueva instancia de la clase EncuestaLimitadaRegion.

        Args:
            nombre_encuesta (str): El nombre de la encuesta.
            listado_preguntas (list[Pregunta]): Una lista de preguntas que 
                conforman la encuesta.
            regiones (list[int]): Una lista de regiones válidas para participar 
                en la encuesta.
        """
        super().__init__(nombre_encuesta, listado_preguntas)
        self._regiones = regiones

    def agregar_respuestas(self, listado_respuestas):
        """Agrega respuestas a la encuesta si el usuario pertenece a una región permitida.

        Args:
            listado_respuestas: Una instancia que contiene las respuestas 
                proporcionadas por un usuario a las preguntas de la encuesta.

        Raises:
            ValueError: Si el usuario no pertenece a una región permitida.
        """
        if listado_respuestas.getUsuario.getRegion in self._regiones:
            super().agregar_respuestas(listado_respuestas)
        else:
            print("El usuario no pertenece a una región válida para esta encuesta.")


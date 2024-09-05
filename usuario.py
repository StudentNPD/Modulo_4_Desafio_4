class Usuario:
    """Representa un usuario con correo electrónico, edad y región.

    Esta clase maneja la información básica de un usuario, como su correo,
    edad y región, y proporciona métodos para modificar y acceder a estos
    atributos. También incluye un método para que el usuario responda a 
    encuestas.

    Args:
        correo (str): El correo electrónico del usuario.
        edad (int): La edad del usuario.
        region (int): La región a la que pertenece el usuario.
    """

    def __init__(self, correo: str, edad: int, region: int):
        """Inicializa una nueva instancia de la clase Usuario.

        Args:
            correo (str): El correo electrónico del usuario.
            edad (int): La edad del usuario.
            region (int): La región a la que pertenece el usuario.
        """
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def getCorreo(self) -> str:
        """Obtiene el correo electrónico del usuario.

        Returns:
            str: El correo electrónico del usuario.
        """
        return self.__correo

    @property
    def getEdad(self) -> int:
        """Obtiene la edad del usuario.

        Returns:
            int: La edad del usuario.
        """
        return self.__edad

    @property
    def getRegion(self) -> int:
        """Obtiene la región a la que pertenece el usuario.

        Returns:
            int: La región a la que pertenece el usuario.
        """
        return self.__region

    def modificarCorreo(self, nuevo_correo: str) -> None:
        """Modifica el correo electrónico del usuario.

        Args:
            nuevo_correo (str): El nuevo correo electrónico que reemplazará
                al actual.
        """
        self.__correo = nuevo_correo

    def modificarEdad(self, nueva_edad: int) -> None:
        """Modifica la edad del usuario.

        Args:
            nueva_edad (int): La nueva edad que reemplazará a la edad actual.
        """
        self.__edad = nueva_edad

    def modificarRegion(self, nueva_region: int) -> None:
        """Modifica la región a la que pertenece el usuario.

        Args:
            nueva_region (int): La nueva región que reemplazará a la región
                actual.
        """
        self.__region = nueva_region

    def contestarEncuesta(self, encuesta) -> None:
        """Permite al usuario contestar una encuesta.

        Este método guía al usuario a través de una serie de preguntas de una 
        encuesta, registrando las respuestas seleccionadas. Las respuestas se 
        almacenan y se asocian al usuario.

        Args:
            encuesta: Una instancia de la clase Encuesta que contiene las 
                preguntas que el usuario deberá contestar.

        Raises:
            ValueError: Si la respuesta ingresada no es un número válido.
        """
        from listado_respuestas import ListadoRespuestas

        respuestas = []
        for pregunta in encuesta.getListadoPreguntas():
            print(pregunta.mostrar())
            try:
                respuesta = int(input("Ingrese el número de la alternativa elegida: ")) - 1
                respuestas.append(respuesta)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_respuestas(listado_respuestas)
        print("Encuesta contestada exitosamente.")



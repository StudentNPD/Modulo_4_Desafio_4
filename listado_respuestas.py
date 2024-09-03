from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: "Usuario"):
        self.__usuario = usuario
        self.__lista_respuestas = []

    @property
    def getUsuario(self) -> "Usuario":
        return self.__usuario

    @property
    def getRespuestas(self) -> list:
        return self.__lista_respuestas

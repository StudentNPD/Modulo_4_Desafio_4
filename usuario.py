class Usuario:
    def __init__(self, , correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def getCorreo(self) -> str:
        return self.__correo

    @property
    def getEdad(self) -> int:
        return self.__edad

    @property
    def getRegion(self) -> int:
        return self.__region




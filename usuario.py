class Usuario:
    def __init__(self, , correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def region(self) -> int:
        return self.__region


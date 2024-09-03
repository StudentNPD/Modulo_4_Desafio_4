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

    @correo.setter
    def modificarCorreo(self, nuevo_correo: str) -> None:
        self.__correo = nuevo_correo

    @edad.setter
    def modificarEdad(self, nueva_edad: int) -> None:
        self.__edad = nueva_edad

    @region.setter
    def modificarRegion(self, nueva_region: int) -> None:
        self.__region = nueva_region



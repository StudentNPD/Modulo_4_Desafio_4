class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self._contenido = contenido
        self._ayuda = ayuda

    # consulta el contenido de la alternativa
    def getContenido(self):
        return self._contenido

    # modifica el contenido de la alternativa   
    def modificarContenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    # consulta la ayuda de la alternativa
    def getAyuda(self):
        return self._ayuda
    
    # modifica la ayuda de la alterniatica
    def modificarAyuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    
class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self._contenido = contenido
        self._ayuda = ayuda

    # consulta el contenido de la alternativa
    def get_contenido(self):
        return self._contenido

    # modifica el contenido de la alternativa   
    def set_contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    # consulta la ayuda de la alternativa
    def get_ayuda(self):
        return self._ayuda
    
    # modifica la ayuda de la alterniatica
    def set_ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    
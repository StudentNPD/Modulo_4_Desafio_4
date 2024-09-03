from pregunta import Pregunta
from alternativa import Alternativa
from listado_respuestas import ListadoRespuestas
from usuario import Usuario

# encuesta(nombre, listado_preguntas, listado_respuestas)
nombre_encuesta = input("Ingrese el nombre de la encuesta:\n")
listado_preguntas = []
listado_respuestas = []

# Menu Usuario:
# Ingresar Correo 
# Ingresar edad 
# Ingresar Region
mi_usuario = Usuario("gato@gmail.com", 18, 5)

# Menu: 
# 1) Consultar nombre de la encuesta 
# 2) Modificar encuesta //
# 3) Responder encuesta


class Encuesta(nombre_encuesta, listado_preguntas, listado_respuestas):
    def __init__(self, nombre_encuesta, listado_preguntas ):
        self._nombre_encuesta = nombre_encuesta
        self._listado_preguntas = listado_preguntas
        self._listado_respuestas = [] 
    
    def get_nombre(self):
        return nombre_encuesta

    def set_nombre(nombre_encuesta):
        print(nombre_encuesta)
        nuevo_nombre= input("Ingrese el nuevo nombre:")
        nombre_encuesta = nuevo_nombre      
    def agregar_respuestas(self, listado_respuestas ):
        # agregar listado de respuestas
        self._listado_respuestas = listado_respuestas
    
class EncuestaLimitadaEdad(Encuesta):
            # edad_minima, edad_maxima
        
        #def agregar_respuestas(self):
            # agregar listado de respuestas considerando la edad
class EncuestaLimitadaRegion(Encuesta):
    # lista regiones
    #def agregar_respuestas(self):
        # agregar listado de respuestas considerando la region

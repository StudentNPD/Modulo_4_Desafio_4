from pregunta import Pregunta
from alternativa import Alternativa
from listado_respuestas import ListadoRespuestas
from usuario import Usuario

# encuesta(nombre, listado_preguntas, listado_respuestas)
nombre_encuesta = input("Ingrese el nombre de la encuesta:\n")
listado_preguntas = []
listado_respuestas = []


print("WELCOME TO THIS APPLICATION")
mi_correo = input("Ingrese su correo:\n")
mi_edad = input("Ingrese su edad:\n")
mi_region = input("Ingrese su Region:\n")


mi_usuario = Usuario("gato@gmail.com", 18, 5)

# Menu: 
# 1) Consultar nombre de la encuesta 
# 2) Modificar encuesta //
# 3) Responder encuesta
# 4) Monstrar encuesta

# Menu Pregunta:
# 1) Modificar Enunciado
# 2) Modificar alternativa
# 3) 

# encuesta 1 
pregunta_1 = Pregunta("gato gato") 
alternativa_1 = dict({'contenido':'gato', 'ayuda':'gato1'})
alternativa_2 = dict({'contenido':'gato', 'ayuda':'gato1'})
alternativa_3 = dict({'contenido':'gato', 'ayuda':'gato1'})
pregunta_1.agregar_alternativa(alternativa_1)
pregunta_1.agregar_alternativa(alternativa_2)
pregunta_1.agregar_alternativa(alternativa_3)
#print(pregunta_1.mostrar())
listado_preguntas.append(pregunta_1)
listado_preguntas.append(pregunta_1)
# encuesta 2 
# encuesta 3



class Encuesta:
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
    
    def get_listado_preguntas(self):
        preguntas = ""
        for pregunta in listado_preguntas:
            preguntas += pregunta.mostrar()
        return preguntas
    
encuesta = Encuesta(nombre_encuesta,listado_preguntas)
print(encuesta.get_listado_preguntas())
#class EncuestaLimitadaEdad(Encuesta):
#        #edad_minima, edad_maxima
#        if edad >= 18: 
#          #  print lista_mayor de edad 
#            
#        def agregar_respuestas(self):
#            #agregar listado de respuestas considerando la edad
#class EncuestaLimitadaRegion(Encuesta):
#    #lista regiones
#    
#    def agregar_respuestas(self):
#        #agregar listado de respuestas considerando la region
#


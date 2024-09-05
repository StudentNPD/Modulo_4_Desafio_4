from usuario import Usuario
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from pregunta import Pregunta

def crear_pregunta():
    """Crea una nueva pregunta para una encuesta.

    Esta función solicita al usuario ingresar el enunciado de la pregunta, 
    si es requerida y un texto de ayuda opcional. Además, permite agregar 
    varias alternativas a la pregunta, cada una con su respectivo texto de ayuda opcional.

    Returns:
        Pregunta: Una instancia de la clase Pregunta con el enunciado, 
        si es requerida, ayuda y alternativas especificadas.
    """
    enunciado = input("Ingrese el enunciado de la pregunta: ")
    es_requerida = input("¿Es una pregunta requerida? (s/n): ").lower() == 's'
    ayuda = input("Ingrese el texto de ayuda (opcional, presione Enter para omitir): ") or None
    pregunta = Pregunta(enunciado, es_requerida, ayuda)

    while True:
        contenido = input("Ingrese el contenido de una alternativa (o presione Enter para terminar): ")
        if not contenido:
            break
        ayuda_alt = input("Ingrese el texto de ayuda para la alternativa (opcional, presione Enter para omitir): ") or None
        pregunta.agregar_alternativa({"contenido": contenido, "ayuda": ayuda_alt})

    return pregunta

def crear_encuesta():
    """Crea una nueva encuesta, que puede ser de tipo normal, limitada por edad o limitada por región.

    La función solicita al usuario ingresar el nombre de la encuesta y agregar preguntas. 
    Luego, permite seleccionar el tipo de encuesta a crear: normal, limitada por edad o 
    limitada por región, según las opciones que el usuario ingrese.

    Returns:
        Encuesta: Una instancia de la clase Encuesta, EncuestaLimitadaEdad o 
        EncuestaLimitadaRegion, dependiendo de la selección del usuario.
    """
    nombre = input("Ingrese el nombre de la encuesta: ")
    preguntas = []
    while True:
        respuesta = input("¿Desea agregar una pregunta? (s/n): ").lower()
        if respuesta != 's':
            break
        preguntas.append(crear_pregunta())

    tipo_encuesta = input("Seleccione el tipo de encuesta (1: Normal, 2: Limitada por Edad, 3: Limitada por Región): ")
    
    if tipo_encuesta == '2':
        edad_min = int(input("Ingrese la edad mínima: "))
        edad_max = int(input("Ingrese la edad máxima: "))
        return EncuestaLimitadaEdad(nombre, preguntas, edad_min, edad_max)
    elif tipo_encuesta == '3':
        regiones = [int(x) for x in input("Ingrese las regiones permitidas (separadas por coma): ").split(',')]
        return EncuestaLimitadaRegion(nombre, preguntas, regiones)
    else:
        return Encuesta(nombre, preguntas)

def main():
    """Función principal del sistema de encuestas.

    Esta función guía al usuario a través del proceso de creación de un usuario, 
    creación de una encuesta, y la posibilidad de contestar la encuesta 
    inmediatamente después de su creación.
    """
    print("Bienvenido al sistema de encuestas")
    
    # Crear usuario
    correo = input("Ingrese su correo: ")
    edad = int(input("Ingrese su edad: "))
    region = int(input("Ingrese su región: "))
    usuario = Usuario(correo, edad, region)

    # Crear encuesta
    encuesta = crear_encuesta()

    # Mostrar encuesta creada
    print("\nEncuesta creada:")
    print(encuesta.mostrar())

    # Contestar encuesta
    respuesta = input("¿Desea contestar la encuesta ahora? (s/n): ").lower()
    if respuesta == 's':
        usuario.contestarEncuesta(encuesta)

if __name__ == "__main__":
    main()


def hacer_pregunta(pregunta, respuesta_correcta):
    respuesta_usuario = input(pregunta).lower()
    if respuesta_usuario == respuesta_correcta:
        print("¡Correcto!")
        return True
    else:
        print("Incorrecto. La respuesta correcta es:", respuesta_correcta)
        return False


def juego_de_preguntas():
    print("¡Bienvenido al juego de preguntas!")
    puntaje = 0

    
    if hacer_pregunta("1. ¿Cual es el lenguaje de programación más popular en la actualidad? ", "python"):
        puntaje += 1

    
    if hacer_pregunta("2. ¿Cuantos patas tiene un cienpies? ", "100"):
        puntaje += 1

    
    if hacer_pregunta("3. ¿Cual es la capital de Francia? ", "paris"):
        puntaje += 1
    
    
    if hacer_pregunta("4. ¿Con que apodo se le conoce al CR7? ", "el bicho"):
        puntaje += 1

    print("Tu puntaje final es:", puntaje, "de 4 preguntas.")


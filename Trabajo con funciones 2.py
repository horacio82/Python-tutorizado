#PILDORAS INFORMÁTICAS
#Python tutorizado. Funciones III. Vídeo 12

def imprimeMensajes(): #definición (creación) de la función

    return "Este es el mensaje de la función"

valorMensaje = imprimeMensajes() #Guarda lo que devuele la función en una variable.
print(valorMensaje)

# Función con llamada de parámetros (mensaje, valor1, valor2)
def imprimeMensajePersonalizado(mensaje, valor1, valor2):
    return mensaje + str((valor1+valor2))

print(imprimeMensajePersonalizado("La suma es ", 5,7)) # Agrega datos a los parámetros de la función.

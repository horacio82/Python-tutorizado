#PILDORAS INFORMATICAS
#Python tutorizado. Funciones II, III Vídeo 11, 12

def imprimeMensajes(): #Definición (creación) de la función

    print("Esto es una función")
    print("Curso de Python")
    print("Hola mundo")

#Llamada a la función: 
imprimeMensajes()

print("El programa a terminado su ejecución")    

#-----------------------------------------------------------

def mensajes():

    return "Este es el mensaje de la función"

#guarda en una variable lo que devuelve la función:
valorMensaje = mensajes()
print(valorMensaje)


#-----------------------------------------------------------

#Función con parámetros
def impMensajePersonalizado(mensaje, valor1, valor2):

    return mensaje + str((valor1+valor2))

print(impMensajePersonalizado("La suma es: ",5,7))
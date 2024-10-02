#Pildoras informáticas
#Python tutorizado. Instrucciones pass, continue y else. Vídeo 21

nombre = "Horacio Molinari"

contador = 0

#El bucle for itera sobre cada elemento en la variable nombre:
for i in nombre:

    #Esto verifica si el elemento actual (i) es un espacio en blanco:
    if i==" ":

        #Si es así, se ejecuta la instrucción continue, que salta al siguiente elemento sin ejecutar el código que sigue
        continue
        
        #Si el elemento actual no es un espacio en blanco, se incrementa el valor de contador en 1 mediante la línea
    contador+=1

print(contador)    

'''En resumen, este código cuenta la cantidad de caracteres no espacios en blanco en la cadena nombre. 
Cada vez que encuentra un espacio en blanco, lo ignora y continúa con el siguiente carácter.'''

#-----------------------------------------------------------------------

#Este programa solicita al usuario que introduzca su dirección de correo electrónico mediante la función input()

#El valor ingresado por el usuario se almacena en la variable email:
email = input("Introduce tu correo electrónico: ")

#El bucle for itera sobre cada carácter en la cadena email.
#En cada iteración, se verifica si el carácter actual (i) es igual a "@":
for i in email:

    #Si se encuentra un "@", se ejecuta la instrucción dentro del bloque if
    if i=="@":
        #Se asigna el valor True a la variable arroba
        arroba=True
        #Luego, se utiliza break para salir del bucle y evitar seguir buscando más "@"
        break

#Si el bucle for completa todas las iteraciones sin encontrar un "@", se ejecuta el bloque else.
else:
    #En este caso, se asigna el valor False a la variable arroba
    arroba=False
#Finalmente, se imprime el valor de arroba, que indicará si se encontró o no un "@" en la dirección de correo electrónico.
print(arroba)    

'''En resumen, este código verifica si una dirección de correo electrónico contiene el símbolo "@". 
Si lo encuentra, establece la variable arroba en True; de lo contrario, la establece en False.'''
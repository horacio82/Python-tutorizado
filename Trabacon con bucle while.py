#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Bucle While I, II - Vídeo 18, 19.

import math 

contador = 0

while contador < 5:
    print("Hola")
    contador = contador +1

print("Hemos salido del bucle.")

#--------------------------------------------------------------------

edad = int(input("Introduce tu edad: "))

while edad < 0 or edad > 100:
    print("Has introducido una edad no válida.")
    edad = int(input("Introduce tu edad: "))

print("Gracias, puedes pasar.")
print("Edad del usuario "+str(edad))

#----------------------------------------------------------------------

print("Este programa halla la raíz cuadrada de un número.")

numero = int(input("Introduce un número: "))

intentos = 1

while numero<0:
    print("El valor numérico no puede ser negativo.")

    numero = int(input("Introduce un número: "))

    intentos=intentos+1

    if intentos==5:

        break

if intentos==5:
    print("Lo siento, no puedo realizar el cálculo:")
else:
    print(math.isqrt(numero))


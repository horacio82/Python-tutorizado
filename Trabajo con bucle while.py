#Pildoras informáticas (video 18 y 19) control de flujo, bucle while.
import math


#Variable
contador = 0

#Mientras que contador sea menor a 10, imprime "Hola"
while contador<10:
    print("Hola ")

    #incrementa la variable contador en cada vuelta:
    contador=contador+1

#Cuando contador valga más de 10, imprime esto:
print("Hemos salido del bucle")    

#------------------------------------------------------------

edad = int(input("Introduce tu edad por favor: "))

while edad <0 or edad>150:
    print("Has introducido una edad no válida.")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias, puedes pasar.")
print("Edad del usuario",str(edad),"años.")    

#-------------------------------------------------------------

print("Este programa halla la raíz cuadrada de un valor numérico")

numero = int(input("Introduce un número: "))

intentos = 1

while numero<0:
    print("El valor numérico no puede ser negativo")
    numero = int(input("Introduce un número: "))
    intentos=intentos+1

    #Si la variable intentos es igual a 5:
    if intentos==5:

        #corta:
        break

if intentos==5:
    print("Lo siento, no puedo realizar el cálculo.")
else:
    print(math.sqrt(numero))  
  
#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Bucle While I. Vídeo 18


contador = 0

while contador < 5:
    print("Hola")
    contador = contador +1

print("Hemos salido del bucle.")

#--------------------------------------------------------------------

edad = int(input("Introduce tu edad: "))

while edad < 0:
    print("Has introducido una edad negativa o no válida.")
    edad = int(input("Introduce tu edad: "))

print("Gracias, puedes pasar.")
print("Edad del usuario "+str(edad))
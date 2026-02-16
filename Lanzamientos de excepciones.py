#PILDORAS INFORMATICAS
#Python tutorizado. Excepciones IV. Vídeo 28

import math

def calculaRaizCuadrada(numero):

    if numero<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(numero)

numeroUsuario = int(input("Introduce un número: "))

try:
    print(calculaRaizCuadrada(numeroUsuario))
except ValueError:
    print("Error de número negativo.")
    
print("Y por acá continuaría el programa...")

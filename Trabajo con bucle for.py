#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Bucle For. Vídeo 20

# Primer bucle: recorre una lista de tres números
for i in [25,60,90]:
    print("Hola mundo.") # Imprime "Hola mundo." en cada iteración, sin usar el valor de i


# Segundo bucle: recorre una lista de nombres de meses
for meses_agno in ["enero","febrero","marzo","abril"]:
    print(meses_agno) # Imprime el nombre del mes actual


# Tercer bucle: recorre una secuencia de números del 0 al 18 (19 elementos)
for dias in range(0,19):

    # Imprime tres líneas por cada iteración del bucle
    print("Hola gente")
    print("Estoy estudiando los bucles")
    print("Esta es la última línea del bucle")

# Mensaje final fuera de los bucles
print("Hemos llegado al final del programa.")
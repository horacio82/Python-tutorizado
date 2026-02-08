#PILDORAS INFORMATICAS
#Python tutorizado. Explicación ejercicio diccionarios y listas
#SOLUCIÓN EJERCICIO 22

paises={}

pais=input("Introduce el país: ")

while pais !="salir":

    ciudad=input("Introduce ciudad: ")

    lista_ciudades=paises.setdefault(pais,[ciudad])

    if lista_ciudades!=[ciudad]:

        paises[pais].append(ciudad)

    pais = input("Intreoduce el país: ")

print(paises)

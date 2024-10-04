#Pildoras informáticas
#Python tutorizado. Explicación ejercicio diccionarios y listas(video 22)

paises={}

pais = input("Introduce el país: ")

while pais!="salir":
    
    ciudad = input("Introduce la ciudad: ")

    lista_ciudades=paises.setdefault(pais,[ciudad])

    if lista_ciudades!=[ciudad]:
        paises[pais].append(ciudad)

    pais = input("Introduce el país: ")

print(paises)        


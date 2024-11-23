#PILDORAS INFORMÁTICAS
#Python tutorizado. Listas. Vídeo 6

#Definición de la lista:
trabajadores = ["Ana","María","Antonio","Miguel"]

#append agrega un elemento a la lista:
trabajadores.append("Juan")

#Imprime la longitud de la lista:
print(len(trabajadores))
#La función len devuelve el número de elementos en la lista trabajadores. 
# Dado que se añadió "Juan", la longitud ahora es 5.

#Acá se está accediendo al elemento en el índice 2 de la lista trabajadores. 
# Recordando que los índices en Python empiezan en 0, el índice 2 corresponde 
# al tercer elemento de la lista, que es "Antonio":
print("El elemento del índice 2 es:",trabajadores[2])



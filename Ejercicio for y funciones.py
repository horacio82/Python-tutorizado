#PILDORAS INFORMATICAS
#Python tutorizado. Explicación ejercicio bucle For.


# Definimos una función que compara dos listas elemento por elemento
def comparaListas (lista1,lista2):

# Verificamos si las listas tienen diferente longitud:
    if(len(lista1)!=len(lista2)):

# Si no tienen la misma cantidad de elementos, no pueden ser iguales
        return False
    else:

# Recorremos ambas listas desde el segundo elemento (índice 1):
        for i in range(1,len(lista1)):
            # Comparamos los elementos en la misma posición


            if(lista1[i]!=lista2[i]):
                # Si encontramos una diferencia, las listas no son iguales

                return False
            # Si todas las comparaciones fueron iguales, devolvemos True

    return True

# Creamos dos listas con nombres de alumnos:
alumnosA=["Juan","Pedro","Ana"]
alumnosB=["Juan","Pedro","Ana"]

# Imprimimos el resultado de comparar ambas listas:
print(comparaListas(alumnosA,alumnosB))
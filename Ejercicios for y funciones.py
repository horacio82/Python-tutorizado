'''Pildoras informáticas - Python tutorizado. Ejercicio bucle For
Ejercicio bucles y condicionales.Comparar listas

Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas, devolviendo True si las listas son idénticas y False si no lo son.

'''

def compararListas (lista1,lista2):

    #si la longitud de la lista1 es distina de la lista2:
    if(len(lista1)!=len(lista2)):
        return False
    else:

        #Va desde 1 hasta la longitud de la lista:
        for i in range(1,len(lista1[i])):

            if(lista1[i]!=lista2[i]):
                return False
            
        
    return True    

alumnosA=["Juan","Pedro","Ana"]
alumnosB=["Juan","Pedro","Ana"]

print(compararListas(alumnosA,alumnosB))
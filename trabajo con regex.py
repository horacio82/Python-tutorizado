#PILDORAS INFORMATICAS
#Python tutorizado. Expresiones regulares I. Vídeo 85

import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"


busqueda = "Python"

#if re.search(busqueda, cadena) is not None: #si no encuentra nada devuelve None
    #print("He encontrado el texto",busqueda)
#else:
    #print("No he encontrado el texto",busqueda)    


texto_encontrado = re.search(busqueda, cadena) #devuelve un objeto

print(texto_encontrado.start()) #devuelve la posición de la primera letra de la palabra buscada

print(texto_encontrado.end()) #devuelve la posición de la última letra de la palabra buscada

print(texto_encontrado.span()) #devuelve una tupla con la posición de la primera y última letra de la palabra buscada

print(re.findall(busqueda, cadena)) #devuelve una lista con todas las veces que se repite la palabra buscada

print(len(re.findall(busqueda, cadena))) #devuelve el número de veces que se repite la palabra buscada
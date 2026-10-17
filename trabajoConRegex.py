#PILDORAS INFORMÁTICAS - Python tutorizado. Expresiones regulares I. Vídeo 85

import re

cadena = "Estoy trabajando con Python un sábado por la mañana. EL próximo sábado será un día de descanso."

busqueda = "sábado"

#busca si la palabra domingo está en la cadena
if re.search(busqueda, cadena) is not None: 
    print(f"Se ha encontrado la palabra {busqueda} en la cadena")

else:
    print(f"No se ha encontrado la palabra {busqueda} en la cadena")    

texto_encontrado = re.search(busqueda, cadena)  

print(texto_encontrado.start())#muestra la posición de inicio de la palabra encontrada

print(texto_encontrado.end())#muestra la posición de fin de la palabra encontrada

print(texto_encontrado.span())#muestra la posición de inicio y fin de la palabra encontrada

print(re.findall(busqueda, cadena))#muestra todas las coincidencias de la palabra encontrada en la cadena

print(len(re.findall(busqueda, cadena)))#muestra el número de coincidencias de la palabra encontrada en la cadena
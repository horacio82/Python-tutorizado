#PILDORAS INFORMÁTICAS
#Python tutorizado. Expresiones regulares III. Vídeo 87

import re

lista_terminos=["camión","Camion","niños","niñas","ejemplo"]

lista_otros_terminos=["Ma1","Se1","Ma2","Va1","Ba1","Se2","Ma3","Ma4","se3","seA","seB","va2","seC"]

#Bucle que recorre la lista de términos y busca aquellos que contienen letras entre la "p" y la "z"
for termino in lista_terminos:
    if re.findall("[p-z]", termino):
        print(termino)

print("---------------------------------------------------")

#Bucle que recorre la lista de términos y busca aquellos que comienzan con letras entre la "a" y la "f"
for termino in lista_terminos:
    if re.findall("^[A-F]", termino):
        print(termino)        

print("---------------------------------------------------")

#Bucle que recorre la lista de términos y busca aquellos que terminan con letras entre la "l" y la "p"
for termino in lista_terminos:
    if re.findall("[l-p]$", termino):
        print(termino)        

print("---------------------------------------------------")        


for termino in lista_otros_terminos:
    if re.findall("Se[0-2A-B]", termino):
        print(termino)
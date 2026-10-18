#PILDORAS INFORMATICAS - Python tutorizado. Expresiones regulares II. Vídeo 86

import re

lista_nombres=["Antonio Banderas","Salma Hayek","Tomás Cruceros","Antonio Resines","Friedrich Hayek"]

lista_terminos=["camión","camion","niños","niñas","ejemplo"]

#Bucle que recorre la lista de nombres y busca aquellos que comienzan con "Antonio"
for nombre in lista_nombres:
    if re.findall("^Antonio", nombre):
        print(nombre)

#Bucle que recorre la lista de nombres y busca aquellos que terminan con "Hayek"
for nombre in lista_nombres:
    if re.findall("Hayek$", nombre):
        print(nombre)        

#Bucle que recorre la lista de términos y busca aquellos que contienen "camión" o "camion"
for termino in lista_terminos:
    if re.findall("cami[óo]n", termino):
        print(termino)        
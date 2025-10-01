#PILDORAS INFORMATICAS
#Python tutorizado. Diccionarios. Vídeo 9

#Diccionario: {"Clave":"Valor"}
lasCapitales = {"España":"Madrid", "Francia":"Toulouse", "Reino Unido": "Londres"}

#Agregar un elemento al diccionario:
lasCapitales["Colombia"] = "Bogotá"

#Modificar valor:
lasCapitales["Francia"] = "Paris"

print(lasCapitales)

#Eliminar elemento:
del lasCapitales["Reino Unido"]

print(lasCapitales)


#--------------------------otro ejemplo de diccionario---------------------

datos = {"España":"Madrid", 23:"M. Jordan", "Mosqueteros":3}
print(datos)


#Tupla:
claveCapitales = ["España","Reino Unido","Colombia","Portugal"]

capitalesMundo = {claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Bogotá", claveCapitales[3]:"Lisboa"}

print(capitalesMundo)

#Imprime la clave de un valor:
print(capitalesMundo["Colombia"])

#Imprimw las claves del diccionario:
print(capitalesMundo.keys())

#Imprime los valores del diccionario:
print(capitalesMundo.values())

#Imprime la longitud del diccionario:
print(len(capitalesMundo))

#---------------------------otro ejemplo-----------------------------------

#Diccionario dentro de otro diccionario:
datosJordan = {23:"Jordan","Nombre":"Michael","Equipo":"C.Bulls","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(datosJordan.keys())
print(datosJordan["Anillos"])

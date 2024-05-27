#PILDORAS INFORMATICAS
#Python tutorizado. Diccionarios. Vídeo 9

#Creando un diccionario = {"clave":"valor"}:
lasCapitales={"España":"Madrid", "Francia":"Paris", "Reino Unido":"Londres"}
lasCapitales["Colombia"]="Bogotá" #agrega un nuevo valor
lasCapitales["Francia"]="París" #modifica un valor
print(lasCapitales)
del lasCapitales["Reino Unido"] #Borra un valor
print(lasCapitales)

#Nuevo diccionario (datos variados):
datos={"España":"Madrid", 23:"M. Jordan", "Mosqueteros":3}
print(datos)

#Creando una tupla:
claveCapitales=["España","Reino Unido","Colombia", "Portugal"]

#Creando un diccionario:
capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Bogotá", claveCapitales[3]:"Lisboa"}
print(capitalesMundo)

print(capitalesMundo.keys()) #Imprime el diccionario con sus claves
print(capitalesMundo.values()) #Imprime el diccionario con sus valores
print(len(capitalesMundo)) #Imprime la longitud del diccionario (número)

# Otro diccionario (agregando dentro otro diccionario y una lista):
datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(datosJordan)
print(datosJordan["Anillos"]) #Imprime la clave "Anillos"
print(datosJordan)
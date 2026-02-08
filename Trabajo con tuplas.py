#PILDORAS INFORMATICAS
#Python tutorizado. Tuplas. Vídeo 8

#Tupla:
misDatos = ("Horacio", 10,1,1982)
print(misDatos)

#Convierte la tupla en lista:(list)
misDatosLista=list(misDatos)
print(misDatosLista)

#Lista:
otrosDatos=["Molinari",43]

#Convierte la lista en tupla (tuple):
misDatosTupla=tuple(otrosDatos)
print(misDatosTupla)

#Busca dicho elemento en la tupla:
print(43 in misDatos)

#Para saber cuantas veces se encuentra dicho elemento:
print(misDatos.count("Horacio"))

#Para obtener la longitud de la tupla:
print(len(misDatos))

#Desempaquetar tupla:
nombre, dia, mes, agno=misDatos
print(mes)
#PILDORAS INFORMATICAS
#Python tutorizado. Tuplas. Vídeo 8

misDatos=("Horacio", 10, 1, 1982) #tupla
nombre, dia, mes, anio = misDatos #desempaquetar datos
print(anio)

misDatos1=["Horacio", 10, 1, 1982] #lista

misDatosLista=list(misDatos) #convierte la tupla en una lista.

misDatos1Tupla=tuple(misDatos1) #convierte la lista en una tupla.

print(misDatos1Tupla)
print("Horacio" in misDatos1Tupla) #buscar un dato (devuelve booleano)
print(misDatos1Tupla.count("Horacio")) #Para saber la cantidad de veces que está un dato
print(len(misDatos1Tupla)) #Para saber la longitud.




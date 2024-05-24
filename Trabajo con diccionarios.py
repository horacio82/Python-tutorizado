#PILDORAS INFORMATICAS
#Python tutorizado. Diccionarios. Vídeo 9

lasCapitales={"España":"Madrid", "Francia":"Paris", "Reino Unido":"Londres"}
lasCapitales["Colombia"]="Bogotá"
lasCapitales["Francia"]="París"
print(lasCapitales)
del lasCapitales["Reino Unido"]
print(lasCapitales)

datos={"España":"Madrid", 23:"M. Jordan", "Mosqueteros":3}
print(datos)

claveCapitales=["España","Reino Unido","Colombia", "Portugal"]
capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Bogotá", claveCapitales[3]:"Lisboa"}
print(capitalesMundo)
print(capitalesMundo.keys())
print(capitalesMundo.values())
print(len(capitalesMundo))


datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(datosJordan)
print(datosJordan["Anillos"])
print(datosJordan)
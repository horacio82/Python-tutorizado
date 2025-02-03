#PILDORAS INFORMATICAS-Python tutorizado. Archivos externos I. Vídeo 60

from io import open

#Creación de un archivo de texto
archivo_externo = open("primerArchivo.txt","w") #w es de escritura

archivo_externo.write("Hola, soy el primer archivo de texto creado desde Python\n") #Escribimos en el archivo

archivo_externo = open("primerArchivo.txt","a") #a es de añadir

archivo_externo.write("Hola, soy el segundo texto añadido al archivo\n") #Añadimos texto al archivo

archivo_externo = open("primerArchivo.txt","r") #r es de lectura

#informacion = archivo_externo.read() #Leemos el archivo

informacion_lineas = archivo_externo.readlines() #Leemos el archivo línea a línea

archivo_externo.close() #Cerramos el archivo

#print(informacion) #Mostramos el contenido del archivo

print(informacion_lineas) #Mostramos el contenido del archivo línea a línea


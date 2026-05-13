#PILDORAS INFORMATICAS
#Python tutorizado. Archivos externos I. Vídeo 60

'''Comenzamos a ver en este vídeo el acceso externo a ficheros desde Python. El acceso externo se utiliza para almacenar y leer información en archivos externos. La ventaja es que la información se puede almacenar de forma permanente'''

from io import open

archivo_externo = open("primerArchivo.txt", "r") #Abrimos el archivo externo en modo lectura

#archivo_externo.write("\nGuardamos información en el archivo externo de forma permanente") #Escribimos una línea en el archivo externo

informacion_lineas = archivo_externo.readlines()

archivo_externo.close() #Cerramos el archivo para que se guarden los cambios realizados

print(informacion_lineas[0]) #Mostramos el contenido del archivo externo
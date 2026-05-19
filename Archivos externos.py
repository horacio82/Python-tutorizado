#PILDORAS INFORMATICAS
#Python tutorizado. Archivos externos I, II. Vídeo 60, 61

'''Comenzamos a ver en este vídeo el acceso externo a ficheros desde Python. El acceso externo se utiliza para almacenar y leer información en archivos externos. La ventaja es que la información se puede almacenar de forma permanente'''

from io import open

archivo_externo = open("primerArchivo.txt", "r") #Abrimos el archivo externo en modo lectura

print(archivo_externo.read()) #Leemos el contenido del archivo externo

archivo_externo.seek(6) #Volvemos a colocar el cursor de lectura al principio del archivo

print(archivo_externo.read()) #Si intentamos leer el archivo externo de nuevo, no se muestra nada porque el cursor de lectura ya está al final del archivo
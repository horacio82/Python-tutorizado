#Pildoras informaticas
#Python tutorizado. Archivos externos IV. Vídeo 63

import os
import io

#os.makedirs("PracticaDirectorio2") # Creamos un directorio
os.chdir("PracticaDirectorio2") # Cambiamos de directorio

os.remove("ejemplo.docx") # Eliminamos un archivo

os.chdir("../") # Cambiamos de directorio

#os.rename("Ejemplo.txt","Archivo a eliminar.txt") # Renombramos un archivo
#os.remove("Archivo a eliminar.txt") # Eliminamos un archivo
os.rmdir("PracticaDirectorio2") # Eliminamos un directorio

#archivo_externo = open("ejemplo.docx", "w") # Creamos un archivo
#archivo_externo.write("Texto de ejemplo...") # Escribimos en el archivo
print(os.getcwd()) # Mostramos el directorio actual
print(os.listdir("./")) # Mostramos los archivos del directorio

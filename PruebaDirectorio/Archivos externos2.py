#PILDORAS INFORMATICAS
#Python tutorizado. Archivos externos III. Vídeo 62

import os #Importamos el módulo os para trabajar con archivos y directorios
import io #Importamos el módulo io para trabajar con archivos de texto

#os.makedirs("PruebaDirectorio") #Creamos un nuevo directorio llamado PruebaDirectorio

#os.chdir("PruebaDirectorio") #Cambiamos el directorio de trabajo actual a PruebaDirectorio

archivo_externo = open("ArchivoExterno.txt", "w") #Abrimos un archivo externo en modo escritura
archivo_externo.write("Hola, soy un archivo externo") #Escribimos una línea de texto en el archivo

print(os.getcwd()) #Imprimimos el directorio de trabajo actual

print(os.listdir("./")) #Imprimimos la lista de archivos en el directorio actual
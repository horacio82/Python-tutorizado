#PILDORAS INFORMATICAS
#Python tutorizado. Archivos externos I, II, III. Vídeo 60, 61, 62

'''Comenzamos a ver en este vídeo el acceso externo a ficheros desde Python. El acceso externo se utiliza para almacenar y leer información en archivos externos. La ventaja es que la información se puede almacenar de forma permanente'''

from io import open

archivo_externo = open("primerArchivo.txt", "r+") #Abrimos el archivo en modo lectura y escritura. Si el archivo no existe, se creará automáticamente

lista_archivo = archivo_externo.readlines() #Leemos el contenido del archivo y lo guardamos en una lista

lista_archivo[1] = "Esta línea ha sido modificada\n" #Modificamos el primer elemento de la lista

archivo_externo.seek(0) #Volvemos al principio del archivo para escribir desde el inicio

archivo_externo.writelines(lista_archivo) #Escribimos la lista modificada en el archivo

archivo_externo.close() #Cerramos el archivo para guardar los cambios

print(lista_archivo) #Mostramos el contenido del archivo
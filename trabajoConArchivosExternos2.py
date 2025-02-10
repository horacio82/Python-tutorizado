#PILDORAS INFORMATICAS-Python tutorizado. Archivos externos III. Vídeo 62

from io import open #importamos la librería io y la clase open

archivo_externo=open("primerArchivo.txt","r+") #abrimos el archivo en modo lectura y escritura

lista_archivo=archivo_externo.readlines() #leemos el archivo y lo guardamos en una lista

lista_archivo[1]="Hoy es lunes\n" #modificamos el segundo elemento de la lista

archivo_externo.seek(0) #nos posicionamos al principio del archivo

archivo_externo.writelines(lista_archivo) #escribimos la lista en el archivo

archivo_externo.close() #cerramos el archivo


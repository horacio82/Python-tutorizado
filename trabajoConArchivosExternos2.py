#PILDORAS INFORMATICAS-Python tutorizado. Archivos externos III. Vídeo 62

from io import open

archivo_externo=open("primerArchivo.txt","r")

lista_archivo=archivo_externo.readlines()

lista_archivo[1]="Hoy es lunes"

archivo_externo.seek(0)

archivo_externo.writelines(lista_archivo)

archivo_externo.close()


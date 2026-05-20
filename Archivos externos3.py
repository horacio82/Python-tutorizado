#PILDORAS INFORMATICAS
#Python tutorizado. Archivos externos IV. Vídeo 63

import os
import io

#os.makedirs("PtacticaDirectorio2")

os.chdir("PtacticaDirectorio2")

os.remove("Ejemplo.docx")

os.chdir("../")

os.rmdir("PtacticaDirectorio2")

print(os.getcwd())

print(os.listdir("./"))
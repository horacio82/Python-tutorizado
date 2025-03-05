#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO VI. Vídeo 83

from tkinter import *
import re

from resultados_pantalla import *


def pulsaciones_teclas(self, valor, mostrar):
    if mostrar:
        self.operacion+=str(valor) 
        mostrar_pantalla(self, valor) 
    elif not mostrar and valor=="=":
        self.operacion = re.sub(u"\u00D7", "*", self.operacion) #reemplazamos el símbolo de multiplicación por el asterisco
        borrar_pantalla(self)
        mostrar_pantalla(self, str(eval(self.operacion)))    
    else:
        pass   
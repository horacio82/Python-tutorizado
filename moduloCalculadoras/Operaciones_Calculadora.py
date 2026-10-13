#PILDORAS INFORMATICAS - CURSO DE PYTHON
#CALCULADORA POO VI - VIDEO 83

from tkinter import *
import re
from moduloCalculadoras.Resultados_Pantalla import *

def pulsaciones_teclas(self, valor, mostrar):
        if mostrar:
            self.operacion+=str(valor)
            mostrar_pantalla(self,valor)
        elif not mostrar and valor=="=":
            self.operacion=re.sub(u"\u00D7", "*", self.operacion)  # Reemplazar el símbolo de multiplicación "×" por "*"
            borrar_pantalla(self)
            mostrar_pantalla(self, str(eval(self.operacion)))    
        else:
            pass
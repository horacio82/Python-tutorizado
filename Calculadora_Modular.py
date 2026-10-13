#PILDORAS INFORMATICAS
#VIDEO 82 - CALCULADORA POO V

from tkinter import *
import re
from Botonera_Calculadora import *

raiz=Tk()

class Calculadora:

    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.title("Calculadora POO")
        self.operacion=""

        #agregar display-------------------------------------------
        self.display=Entry(ventana, font="Arial 15")

        #ubicar display--------------------------------------------
        self.display.grid(row=1, column=0, columnspan=4, padx=10)
        self.display.config(background="black", foreground="green", justify="right", width=25)

        #creación de botones fila 1 ---------------------------------------
        boton7=colocar_boton(self, 7)
        boton8=colocar_boton(self, 8)
        boton9=colocar_boton(self, 9)
        botonDiv=colocar_boton(self, "/")

        #fila 2------------------------------------------
        boton4=colocar_boton(self, 4)
        boton5=colocar_boton(self, 5)
        boton6=colocar_boton(self, 6)
        botonx=colocar_boton(self, u"\u00D7")  # Usar el símbolo de multiplicación "×" en lugar de "*"
        botonx.config(text="x")  # Cambiar el texto del botón de multiplicación a "x"

        #fila 3------------------------------------------
        boton1=colocar_boton(self, 1)
        boton2=colocar_boton(self, 2)
        boton3=colocar_boton(self, 3)
        botonResta=colocar_boton(self, "-")

        #fila 4------------------------------------------
        botonCero=colocar_boton(self, 0)
        botonComa=colocar_boton(self, ".")
        botonIgual=colocar_boton(self, "=", mostrar=False)
        botonMas=colocar_boton(self, "+")

        #----------------------------------------------------------

        botones=[boton7, boton8, boton9, botonDiv,boton4, boton5, boton6, botonx,boton1, boton2, boton3, botonResta,botonCero, botonComa, botonIgual, botonMas]

        construir_botones(self, botones, 4)
        
mi_calculadora=Calculadora(raiz)

raiz=mainloop() 
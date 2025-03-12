#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO V, VI, VII Vídeo 82, 83 y 84

from tkinter import *
import re

from moduloCalculadoras.botonera_calculadora import *


raiz = Tk() #creamos la ventana

class Calculadora:
    def __init__(self, ventana):#constructor

        self.ventana=ventana
        self.ventana.title("Calculadora POO")

        self.operacion=""

        #agregar display
        self.display=Entry(ventana, font="Arial 15")

        #ubicar display
        self.display.grid(row=1, column=0, columnspan=4)
        self.display.config(bg="black", fg="#00db00", justify="right")

        #---------------fila 1---------------------------------------
        boton7 = colocar_boton(self,7)
        boton8 = colocar_boton(self, 8)
        boton9 = colocar_boton(self, 9)
        boton_div = colocar_boton(self, '/')

        #---------------fila 2---------------------------------------
        boton4 = colocar_boton(self, 4)
        boton5 = colocar_boton(self, 5)
        boton6 = colocar_boton(self, 6)
        boton_mult = colocar_boton(self, u"\u00D7") #u"\u00D7" es el código unicode para el símbolo de multiplicación    
        #boton_mult.config(text="x")

        #---------------fila 3---------------------------------------
        boton1 = colocar_boton(self, 1)
        boton2 = colocar_boton(self, 2)
        boton3 = colocar_boton(self, 3)
        boton_rest = colocar_boton(self, '-')

        #---------------fila 4---------------------------------------
        boton0 = colocar_boton(self, 0)
        boton_coma = colocar_boton(self, '.')    
        boton_igual = colocar_boton(self, '=', mostrar=False)
        boton_sum = colocar_boton(self, '+')

#--------------------------------------------------------------------

        botones = [boton7, boton8, boton9, boton_div, boton4, boton5, boton6, boton_mult, boton1, boton2, boton3, boton_rest, boton0, boton_coma, boton_igual, boton_sum]


        construir_botones(self, botones, 4) #llamamos a la función que construye los botones


mi_alculadora = Calculadora(raiz) #instanciamos la clase


raiz.mainloop() #bucle infinito para mantener la ventana abierta
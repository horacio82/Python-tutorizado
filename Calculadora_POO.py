#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO, II, III, IV
#Vídeo 78, 79, 80, 81

from tkinter import *
import re


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

        #creación de botones---------------------------------------
        boton7=self.colocar_boton(7)
        boton8=self.colocar_boton(8)
        boton9=self.colocar_boton(9)
        botonDiv=self.colocar_boton("/")

        #----------------------------------------------------------
        boton4=self.colocar_boton(4)
        boton5=self.colocar_boton(5)
        boton6=self.colocar_boton(6)
        botonx=self.colocar_boton(u"\u00D7")  # Usar el símbolo de multiplicación "×" en lugar de "*"
        botonx.config(text="x")  # Cambiar el texto del botón de multiplicación a "x"

        #----------------------------------------------------------
        boton1=self.colocar_boton(1)
        boton2=self.colocar_boton(2)
        boton3=self.colocar_boton(3)
        botonResta=self.colocar_boton("-")

        #----------------------------------------------------------
        botonCero=self.colocar_boton(0)
        botonComa=self.colocar_boton(".")
        botonIgual=self.colocar_boton("=", mostrar=False)
        botonMas=self.colocar_boton("+")

        #----------------------------------------------------------

        botones=[boton7, boton8, boton9, botonDiv,boton4, boton5, boton6, botonx,boton1, boton2, boton3, botonResta,botonCero, botonComa, botonIgual, botonMas]
        

        contador=0

        for fila in range(2,6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1

    def colocar_boton(self, valor, mostrar=True, ancho=9, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Tahoma", 9), command=lambda:self.pulsaciones_teclas(valor, mostrar))
        
    def pulsaciones_teclas(self, valor, mostrar):
        if mostrar:
            self.operacion+=str(valor)
            self.mostrar_pantalla(valor)
        elif not mostrar and valor=="=":
            self.operacion=re.sub(u"\u00D7", "*", self.operacion)  # Reemplazar el símbolo de multiplicación "×" por "*"
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))    
        else:
            pass

    def mostrar_pantalla(self, valor):
        self.display.insert(END, valor)        

    def borrar_pantalla(self):
        self.display.delete(0, END)
        


mi_calculadora=Calculadora(raiz)

raiz=mainloop()        
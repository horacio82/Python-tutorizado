#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO, II
#Vídeo 78, 79

from tkinter import *

raiz=Tk()

class Calculadora:

    def __init__(self, ventana):

        self.ventana=ventana
        self.ventana.title("Calculadora POO")

        #agregar display-------------------------------------------
        self.display=Entry(ventana, font="Arial 15")

        #ubicar display--------------------------------------------
        self.display.grid(row=1, column=0, columnspan=4, padx=10)
        self.display.config(background="black", foreground="green", justify="right", width=25)

        #creación de botones---------------------------------------
        boton7=self.colocar_boton(7)
        boton8=self.colocar_boton(8)
        boton9=self.colocar_boton(9)
        botonDiv=self.colocar_boton("/", mostrar=False)

        #----------------------------------------------------------
        boton4=self.colocar_boton(4)
        boton5=self.colocar_boton(5)
        boton6=self.colocar_boton(6)
        botonx=self.colocar_boton("*", mostrar=False)

        #----------------------------------------------------------
        boton1=self.colocar_boton(1)
        boton2=self.colocar_boton(2)
        boton3=self.colocar_boton(3)
        botonResta=self.colocar_boton("-", mostrar=False)

        #----------------------------------------------------------
        botonCero=self.colocar_boton(0)
        botonComa=self.colocar_boton(".")
        botonIgual=self.colocar_boton("=", mostrar=False)
        botonMas=self.colocar_boton("+", mostrar=False)

        #----------------------------------------------------------

        botones=[boton7, boton8, boton9, botonDiv,boton4, boton5, boton6, botonx,boton1, boton2, boton3, botonResta,botonCero, botonComa, botonIgual, botonMas]
        

        contador=0

        for fila in range(2,6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1

    def colocar_boton(self, valor, mostrar=True, ancho=9, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Tahoma", 9))
        


mi_calculadora=Calculadora(raiz)

raiz.mainloop()
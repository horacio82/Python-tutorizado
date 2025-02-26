#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO. Vídeo 78

from tkinter import *

raiz = Tk() #creamos la ventana

class Calculadora:
    def __init__(self, ventana):#constructor

        self.ventana=ventana
        self.ventana.title("Calculadora POO")

        #agregar display
        self.display=Entry(ventana, font="Arial 15")

        #ubicar display
        self.display.grid(row=1, column=0, columnspan=4)
        self.display.config(bg="black", fg="#00db00", justify="right")

        #creamos los botones
        boton7 = self.colocar_boton(7)
        boton8 = self.colocar_boton(8)
        boton9 = self.colocar_boton(9)
        boton_div = self.colocar_boton('/')



mi_alculadora = Calculadora(raiz) #instanciamos la clase




raiz.mainloop() #bucle infinito para mantener la ventana abierta
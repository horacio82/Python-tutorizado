#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO, II, III. Vídeo 78, 79, 80

from tkinter import *

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

        #creamos los botones
        boton7 = self.colocar_boton(7)
        boton8 = self.colocar_boton(8)
        boton9 = self.colocar_boton(9)
        boton_div = self.colocar_boton('/')
        #------------------------------------------------------------
        boton4 = self.colocar_boton(4)
        boton5 = self.colocar_boton(5)
        boton6 = self.colocar_boton(6)
        boton_mult = self.colocar_boton('*')
        #------------------------------------------------------------
        boton1 = self.colocar_boton(1)
        boton2 = self.colocar_boton(2)
        boton3 = self.colocar_boton(3)
        boton_rest = self.colocar_boton('-')
        #------------------------------------------------------------
        boton0 = self.colocar_boton(0)
        boton_coma = self.colocar_boton('.')    
        boton_igual = self.colocar_boton('=', mostrar=False)
        boton_sum = self.colocar_boton('+')
        #------------------------------------------------------------

        botones = [boton7, boton8, boton9, boton_div, boton4, boton5, boton6, boton_mult, boton1, boton2, boton3, boton_rest, boton0, boton_coma, boton_igual, boton_sum]

        contador = 0

        for fila in range(2, 6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1


    def colocar_boton(self, valor, mostrar=True, ancho=9, alto=1):   
        return Button(self.ventana, text=valor, width=ancho, height=alto, font="Tahoma 15", command=lambda:self.pulsaciones_teclas(valor, mostrar))         

    def pulsaciones_teclas(self, valor, mostrar):
        if mostrar:
            self.operacion+=str(valor) 
            self.mostrar_pantalla(valor) 
        elif not mostrar and valor=="=":
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))    
        else:
            pass    

    def mostrar_pantalla(self, valor):
        self.display.insert(END, valor) #mostramos el valor en el display

    def borrar_pantalla(self):
        self.display.delete(0, END) #borramos el contenido del display



mi_alculadora = Calculadora(raiz) #instanciamos la clase




raiz.mainloop() #bucle infinito para mantener la ventana abierta
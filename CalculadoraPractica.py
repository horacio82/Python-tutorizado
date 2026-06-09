#PILDORAS INDORMATICAS
#Python tutorizado. Práctica guiada. Calculadora I, II, III. Vídeo 71, 72, 73

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()  

operacion="" #variable para almacenar la operación que se va a realizar

resultado=0 #variable para almacenar el resultado de la operación

digitoDisplay=StringVar() #variable para almacenar el número que se va a mostrar en el display


#----------------------pulsaciones numéricas----------------------

def pulsacionesNumericas(numeroPulsado):
    global operacion
    if operacion!="":
        digitoDisplay.set(numeroPulsado)
        operacion=""
    else:
        digitoDisplay.set(digitoDisplay.get() + numeroPulsado)


#----------------------función suma----------------------

def suma(num):
    global operacion, resultado

    resultado+=int(num)

    operacion="suma"

    digitoDisplay.set(resultado)


#----------------------función total----------------------

def total():

    global resultado

    digitoDisplay.set(resultado+int(digitoDisplay.get()))

    resultado=0





display=Entry(miFrame, textvariable=digitoDisplay) #creación del cuadro de texto para mostrar el número, se le asigna la variable digitoDisplay para que se actualice con el número que se va a mostrar
display.grid(row=1, column=1, columnspan=4, padx=3, pady=3)
display.config(bg="black", fg="#03f943", justify="right", width=15, font=("arial", 18, "bold")) #configuración del cuadro de texto: color de fondo, color de letra, justificación del texto, ancho y tipo de letra


#---------------------primer fila---------------------

boton7=Button(miFrame, text="7", width=4, command=lambda: pulsacionesNumericas("7")) 
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=4, command=lambda: pulsacionesNumericas("8")) 
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=4, command=lambda: pulsacionesNumericas("9"))
boton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=4)
botonDiv.grid(row=2, column=4)

#---------------------segunda fila---------------------

boton4=Button(miFrame, text="4", width=4, command=lambda: pulsacionesNumericas("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=4, command=lambda: pulsacionesNumericas("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=4, command=lambda: pulsacionesNumericas("6"))
boton6.grid(row=3, column=3)

botonMult=Button(miFrame, text="*", width=4)
botonMult.grid(row=3, column=4)

#---------------------tercera fila---------------------

boton1=Button(miFrame, text="1", width=4, command=lambda: pulsacionesNumericas("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=4, command=lambda: pulsacionesNumericas("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=4, command=lambda: pulsacionesNumericas("3"))
boton3.grid(row=4, column=3)

botonResta=Button(miFrame, text="-", width=4)
botonResta.grid(row=4, column=4)

#---------------------cuarta fila---------------------

boton0=Button(miFrame, text="0", width=4, command=lambda: pulsacionesNumericas("0"))
boton0.grid(row=5, column=1)

botonPunto=Button(miFrame, text=",", width=4, command=lambda: pulsacionesNumericas("."))
botonPunto.grid(row=5, column=2)

botonIgual=Button(miFrame, text="=", width=4, command=lambda: total())
botonIgual.grid(row=5, column=3)

botonSuma=Button(miFrame, text="+", width=4, command=lambda: suma(digitoDisplay.get()))
botonSuma.grid(row=5, column=4)












raiz.mainloop()











raiz.mainloop()
#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora I, II. Vídeo 71, 72

from tkinter import *


raiz=Tk() #ventana
miFrame = Frame(raiz) #frame
miFrame.pack() #empaquetamos el frame

digitoDisplay = StringVar() #variable para la pantalla

display=Entry(miFrame, textvariable=digitoDisplay, font="Tahoma 15") #pantalla
display.grid(row=1, column=1, columnspan=4, pady=10,) #ubicamos la pantalla en el frame    
display.config(bg="black", fg="#03f943", justify="right", width=15) #configuramos la pantalla

#pulsaciones números---------------------------------------
def pulsacionesTeclas(numPulsado):
    digitoDisplay.set(digitoDisplay.get() + numPulsado) #añadimos el número 7 a la pantalla

#botones de la primera fila-----------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:pulsacionesTeclas("7")) #creamos el botón 7
boton7.grid(row=2, column=1) #ubicamos el botón 7 en el frame   
boton8=Button(miFrame, text="8", width=3, command=lambda:pulsacionesTeclas("8")) #creamos el botón 8
boton8.grid(row=2, column=2) #ubicamos el botón 8 en el frame
boton9=Button(miFrame, text="9", width=3, command=lambda:pulsacionesTeclas("9")) #creamosel botón 9
boton9.grid(row=2, column=3) #ubicamos el botón 9 en el frame
botonDiv=Button(miFrame, text="/", width=3) #creamos el botón /
botonDiv.grid(row=2, column=4) #ubicamos el botón / en el frames

#botones de la segunda fila-----------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:pulsacionesTeclas("4")) #creamos el bot
boton4.grid(row=3, column=1) 
boton5=Button(miFrame, text="5", width=3, command=lambda:pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#botones de la tercera fila-----------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#botones de la cuarta fila-----------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:pulsacionesTeclas("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3)
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3)
botonSum.grid(row=5, column=4)


raiz.mainloop() #bucle infinito para que la ventana se mantenga abierta
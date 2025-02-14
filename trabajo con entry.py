#PILDORAS INFORMATICAS  
#Python tutorizado. Interfaces gráficas. Tkinter IV. Vídeo 67

from tkinter import *

raiz=Tk() #creamos la raiz

miFrame=Frame(raiz, width=1000, height=550) #creamos un frame
miFrame.pack() #empaquetamos el frame

#---------------------creamos cuadros de texto-----------------------------------
cuadroTextoNombre=Entry(miFrame) #creamos un cuadro de texto
cuadroTextoNombre.grid(row=0, column=1,) #posicionamos el cuadro de texto
cuadroTextoNombre.config(fg="red", justify="center") #configuramos el cuadro de texto

cuadroTextoApellido=Entry(miFrame) #creamos un cuadro de texto
cuadroTextoApellido.grid(row=1, column=1) #posicionamos el cuadro de texto

cuadroTextoDireccion=Entry(miFrame) #creamos un cuadro de texto
cuadroTextoDireccion.grid(row=2, column=1) #posicionamos el cuadro de texto

cuadroTextoMail=Entry(miFrame) #creamos un cuadro de texto
cuadroTextoMail.grid(row=3, column=1) #posicionamos el cuadro de texto


#----------------------creamos etiquetas-----------------------------------------
nombreLabelNombre=Label(miFrame, text="Nombre:") #creamos una etiqueta
nombreLabelNombre.grid(row=0, column=0, sticky="w") #posicionamos la etiqueta

nombreLabelApellido=Label(miFrame, text="Apellido:") #creamos una etiqueta
nombreLabelApellido.grid(row=1, column=0, sticky="w") #posicionamos la etiqueta

nombreLabelDireccion=Label(miFrame, text="Dirección:") #creamos una etiqueta
nombreLabelDireccion.grid(row=2, column=0, sticky="w") #posicionamos la etiqueta

nombreLabelMail=Label(miFrame, text="Mail:") #creamos una etiqueta
nombreLabelMail.grid(row=3, column=0, sticky="w") #posicionamos la etiqueta






raiz.mainloop() #bucle infinito para que se ejecute la ventana
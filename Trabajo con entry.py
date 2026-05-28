#PILDORAS INFORMATICAS
#Python tutorizado. Interfaces gráficas. Tkinter IV. Vídeo 67

'''En este vídeo comenzamos a ver los widgets Entry. Los Entry son los típicos cuadors de texto que permiten introducir información (texto) al usuario desde la interfaz gráfica.'''

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

cuadroTextoNombre=Entry(miFrame)
cuadroTextoNombre.grid(row=0, column=1) 
cuadroTextoNombre.config(fg="red", justify="center") #configuración del cuadro de texto: color de letra y justificación del texto

nombreLabelNombre=Label(miFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="w") #sticky="w" alinea el texto a la izquierda

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1)

apellidoLabelApellido=Label(miFrame, text="Apellido: ")
apellidoLabelApellido.grid(row=1, column=0, sticky="w")

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=2, column=1)

direccionLabelDireccion=Label(miFrame, text="Dirección: ")
direccionLabelDireccion.grid(row=2, column=0, sticky="w")

cuadroTextoMail=Entry(miFrame)
cuadroTextoMail.grid(row=3, column=1)

mailLabelMail=Label(miFrame, text="Mail personal: ")
mailLabelMail.grid(row=3, column=0, sticky="w")

raiz.mainloop()
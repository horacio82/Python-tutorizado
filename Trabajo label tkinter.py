#PILDORAS INFORMATICAS - CURSO PYTHON
#Python tutorizado. Interfaces gráficas. Tkinter III. Vídeo 66

from tkinter import * #Tkinter es una biblioteca de Python que permite crear interfaces gráficas de usuario (GUI). Es una de las bibliotecas más utilizadas para este propósito en Python.

raiz = Tk() #creamos la ventana raíz

miFrame = Frame(raiz, width=500, height=450) #creamos un frame, que es un contenedor para otros widgets

miFrame.pack() #empaquetamos el frame, esto es necesario para que se muestre en la ventana

#miLabel = Label(miFrame, text="Hoy es miercoles") #creamos un label, que es un widget que muestra texto o imágenes
#miLabel.place(x=120, y=125) #colocamos el label en el frame, el primer número es la coordenada x y el segundo número es la coordenada 

miLogo = PhotoImage(file="colores.png") #creamos un objeto PhotoImage, que es una imagen que se puede mostrar en un label, el archivo debe estar en el mismo directorio que el script o se debe especificar la ruta completa

Label(miFrame, image=miLogo).place(x=120, y=125) #creamos un label y lo colocamos en el frame en una sola línea



raiz.mainloop() #el mainloop es un bucle infinito que mantiene la ventana abierta, es necesario para que la ventana no se cierre inmediatamente después de abrirse.
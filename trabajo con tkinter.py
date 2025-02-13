#PILDORAS INFORMATICAS
#Python tutorizado. Interfaces gráficas. Tkinter I,II. Vídeo 64, 65

from tkinter import *

raiz=Tk() #creamos la raiz

raiz.title("Primera ventana") #titulo de la ventana

raiz.resizable(1,1) #ancho y alto de la ventana redimensionables
raiz.iconbitmap("ACOrigins_0.ico") #icono de la ventana

#raiz.geometry("650x350") #dimensiones de la ventana

raiz.config(bg="blue") #color de fondo de la ventana

miFrame=Frame() #creamos un frame

#miFrame.pack(side="right", anchor="n") #empaquetamos el frame en la raiz

miFrame.config(bg="red") #color de fondo del frame

miFrame.config(width="650", height="350") #dimensiones del frame

miFrame.pack(fill="x") #expandir el frame en el eje x

raiz.mainloop() #bucle infinito que mantiene la ventana abierta


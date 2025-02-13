#PILDORAS INFORMATICAS
#Python tutorizado. Interfaces gráficas. Tkinter I, I. Vídeo 64, 65

from tkinter import *

raiz=Tk() #creamos la raiz

raiz.title("Primera ventana") #titulo de la ventana

raiz.resizable(1,1) #ancho y alto de la ventana redimensionables
raiz.iconbitmap("ACOrigins_0.ico") #icono de la ventana

raiz.geometry("650x350") #dimensiones de la ventana

raiz.config(bg="blue") #color de fondo de la ventana

raiz.mainloop() #bucle infinito que mantiene la ventana abierta


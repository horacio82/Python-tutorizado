# PILDORAS INFORMATICAS - CURSO PYTHON
#Python tutorizado. Interfaces gráficas. Tkinter I. Vídeo 64

from tkinter import * #Tkinter es una biblioteca de Python que permite crear interfaces gráficas de usuario (GUI). Es una de las bibliotecas más utilizadas para este propósito en Python.

raiz = Tk() #creamos la ventana raíz

raiz.title("Primera ventana") #titulo de la ventana

raiz.resizable(1,1) #se puede redimensionar la ventana, el primer 1 es para el ancho y el segundo 1 para el alto

raiz.iconbitmap("pata_perro.ico") #icono de la ventana, el archivo debe estar en la misma carpeta que el script

raiz.geometry("400x300") #tamaño de la ventana, el primer número es el ancho y el segundo número es el alto

raiz.config(bg="blue") #color de fondo de la ventana

raiz.mainloop() #el mainloop es un bucle infinito que mantiene la ventana abierta, es necesario para que la ventana no se cierre inmediatamente después de abrirse.
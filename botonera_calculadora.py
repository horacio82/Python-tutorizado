#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO V. Víd

from tkinter import *
import re

from operaciones_calculadora import *

contador = 0


def construir_botones(self, botones, filas_botones):
    contador = 0
    for fila in range(2, filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row=fila, column=columna)
            contador += 1


def colocar_boton(self, valor, mostrar=True, ancho=9, alto=1):   
    return Button(self.ventana, text=valor, width=ancho, height=alto, font="Tahoma 15", command=lambda:pulsaciones_teclas(self, valor, mostrar))   


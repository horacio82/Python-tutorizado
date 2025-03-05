#PILDORAS INFORMATICAS
#Python tutorizado. Práctica guiada. Calculadora POO VI. Vídeo 83

from tkinter import *


def mostrar_pantalla(self, valor):
    self.display.insert(END, valor) #mostramos el valor en el display

def borrar_pantalla(self):
    self.display.delete(0, END) #borramos el contenido del display
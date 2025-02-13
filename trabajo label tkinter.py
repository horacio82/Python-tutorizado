#PILDORAS INFORMATICAS
#Python tutorizado. Interfaces gráficas. Tkinter III. Vídeo 66

from tkinter import *

root=Tk() #creamos la raiz

miFrame=Frame(root, width=500, height=450) #creamos un frame
miFrame.pack() #empaquetamos el frame   

#miLabel=Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)) #creamos un label

#miLabel.place(x=120, y=125) #colocamos el label en el frame


miLogo=PhotoImage(file="phoenix.png") #creamos un objeto de la clase PhotoImage

Label(miFrame, image=miLogo).place(x=120, y=125) #creamos un label)


root.mainloop() #bucle infinito para que se ejecute la ventana
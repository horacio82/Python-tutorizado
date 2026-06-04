#PILDORAS INFORMATICAS
#Python tutorizado. Interfaces gráficas. Tkinter IV, V, VI, VII. Vídeo 67, 68, 69, 70

'''En este vídeo comenzamos a ver los widgets Entry. Los Entry son los típicos cuadors de texto que permiten introducir información (texto) al usuario desde la interfaz gráfica.'''

from tkinter import *
from tkinter import messagebox as MessageBox

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

miVaraiable=StringVar()

cuadroTextoNombre=Entry(miFrame, textvariable=miVaraiable) #creación del widget Entry, con la opción textvariable para asociar una variable de tipo StringVar al cuadro de texto

cuadroTextoNombre.grid(row=0, column=1, padx=3, pady=3) #padx y pady añaden un espacio entre el cuadro de texto y los bordes del frame

cuadroTextoNombre.config(fg="red", justify="center") #configuración del cuadro de texto: color de letra y justificación del texto

nombreLabelNombre=Label(miFrame, text="Nombre: ")
nombreLabelNombre.grid(row=0, column=0, sticky="w") #sticky="w" alinea el texto a la izquierda

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1, padx=3, pady=3)

apellidoLabelApellido=Label(miFrame, text="Apellido: ")
apellidoLabelApellido.grid(row=1, column=0, sticky="w")

contraseñaLabelContraseña=Label(miFrame, text="Contraseña: ")
contraseñaLabelContraseña.grid(row=4, column=0, sticky="w")

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=2, column=1, padx=3, pady=3)

direccionLabelDireccion=Label(miFrame, text="Dirección: ")
direccionLabelDireccion.grid(row=2, column=0, sticky="w")

cuadroTextoMail=Entry(miFrame)
cuadroTextoMail.grid(row=3, column=1, padx=3, pady=3)

mailLabelMail=Label(miFrame, text="Mail personal: ")
mailLabelMail.grid(row=3, column=0, sticky="w")

cuadroContraseña=Entry(miFrame)
cuadroContraseña.grid(row=4, column=1, padx=3, pady=3)
cuadroContraseña.config(show="*") #configuración del cuadro de texto: mostrar asteriscos en lugar de texto

cuadroTextoComentarios=Text(miFrame, width=16, height=10) #widget Text para comentarios, con configuración de ancho y alto
cuadroTextoComentarios.grid(row=5, column=1, padx=3, pady=3)

comentariosLabelComentarios=Label(miFrame, text="Comentarios: ")
comentariosLabelComentarios.grid(row=5, column=0, sticky="w")

miScrollVertical=Scrollbar(miFrame, command=cuadroTextoComentarios.yview) #scrollbar vertical para el widget Text, con comando para que se mueva el cuadro de texto al hacer scroll

miScrollVertical.grid(row=5, column=2, sticky="nsew") #colocación del scrollbar al lado del widget Text

cuadroTextoComentarios.config(yscrollcommand=miScrollVertical.set) #configuración del widget Text para que se mueva el scrollbar al hacer scroll

def funcionBoton():
    
    cuadroTextoComentarios.insert(INSERT, "El nombre es: " + miVaraiable.get() + "\n") #método insert para insertar texto en el widget Text, con la opción INSERT para insertar el texto en la posición actual del cursor, y el método get para obtener el valor de la variable asociada al cuadro de texto

botonEnviar=Button(raiz, text="Enviar", command=funcionBoton)

botonEnviar.pack() #método pack para colocar el botón en la ventana

raiz.mainloop()
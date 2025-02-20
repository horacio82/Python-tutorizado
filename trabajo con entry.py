#PILDORAS INFORMATICAS  
#Python tutorizado. Interfaces gráficas. Tkinter IV, , VI Vídeo 67, 68, 69

from tkinter import *

from tkinter import messagebox as MessageBox


# Crear la ventana principal
raiz = Tk()

# Crear un frame
miFrame = Frame=Frame(raiz, width=1000, height=550)
miFrame.pack()

miVariable = StringVar() # Variable de control para los radiobuttons

# Cuadros de texto---------------------------------------
cuadroTextoNombre = Entry(miFrame, textvariable=miVariable)
cuadroTextoNombre.grid(row=0, column=1, padx=15, pady=15)
cuadroTextoNombre.config(fg="red", justify="center")

cuadroTextoApellido = Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1, padx=15, pady=15)

cuadroTextoContra = Entry(miFrame)
cuadroTextoContra.grid(row=2, column=1, padx=15, pady=15)
cuadroTextoContra.config(show="*")

cuadroTextoDireccion = Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1, padx=15, pady=15)

cuadroTextoMail = Entry(miFrame)
cuadroTextoMail.grid(row=4, column=1, padx=15, pady=15)

cuadroTextoOpiniones = Text(miFrame, width=15, height=10)
cuadroTextoOpiniones.grid(row=5, column=1, padx=15, pady=15)

# Scrollbar-----------------------------------------------
miScrollVertical = Scrollbar(miFrame, command=cuadroTextoOpiniones.yview)
miScrollVertical.grid(row=5, column=2, sticky="nsew")
cuadroTextoOpiniones.config(yscrollcommand=miScrollVertical.set) # Asociar el scroll con el cuadro de texto

# Etiquetas------------------------------------------------
nombreLabelNombre = Label(miFrame, text="Nombre:")
nombreLabelNombre.grid(row=0, column=0, sticky="w")

nombreLabelApellido = Label(miFrame, text="Apellido:")
nombreLabelApellido.grid(row=1, column=0, sticky="w")

nombreLabelContra = Label(miFrame, text="Contraseña:")
nombreLabelContra.grid(row=2, column=0, sticky="w")

nombreLabelDireccion = Label(miFrame, text="Dirección:")
nombreLabelDireccion.grid(row=3, column=0, sticky="w")

nombreLabelMail = Label(miFrame, text="Mail:")
nombreLabelMail.grid(row=4, column=0, sticky="w")

nombreLabelComentarios = Label(miFrame, text="Comentarios:")
nombreLabelComentarios.grid(row=5, column=0, sticky="w")


def funcionBoton():
    
    #MessageBox.showinfo("Saludo", "Hola desde Tkinter ")
    miVariable.set("Horacio")

# Botón---------------------------------------------------
botonEnviar = Button(raiz, text="Enviar", command=funcionBoton)
botonEnviar.pack()


# Iniciar el bucle principal de Tkinter
raiz.mainloop()

#PILDORAS INFORMATICAS
#Python tutorizado. BBDD. Aplicación gráfica CRUD I, II, III, IV. Vídeo 99, 100, 101, 102

from tkinter import * # Importamos la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox # Importamos la librería messagebox para mostrar mensajes emergentes
import sqlite3 # Importamos la librería sqlite3 para trabajar con bases de datos SQLite

root=Tk() # Creamos la ventana principal de la aplicación

barraMenu=Menu(root) # Creamos una barra de menú
root.config(menu=barraMenu, width=300, height=300) # Configuramos la ventana principal para que use la barra de menú

bbddMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para la base de datos
bbddMenu.add_command(label="Conectar", command=lambda:conectar()) # Añadimos una opción para conectar a la base de datos
bbddMenu.add_command(label="Salir", command=lambda:salir())

borrarMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para borrar datos
borrarMenu.add_command(label="Borrar", command=lambda:borrar()) # Añadimos una opción para borrar datos

crudMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para operaciones CRUD
crudMenu.add_command(label="Crear", command=lambda:crear()) # Añadimos una opción para crear datos
crudMenu.add_command(label="Leer", command=lambda:leer()) # Añadimos una opción para leer datos
crudMenu.add_command(label="Actualizar", command=lambda:actualizar()) # Añadimos una opción para actualizar datos
crudMenu.add_command(label="Eliminar", command=lambda:eliminar()) # Añadimos una opción para eliminar datos

ayudaMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para ayuda
ayudaMenu.add_command(label="Licencia", command=lambda:acercaDe()) # Añadimos una opción para mostrar información sobre la aplicación
ayudaMenu.add_command(label="Acerca de", command=lambda:acercaDe()) # Añadimos una opción para mostrar información sobre la aplicación

barraMenu.add_cascade(label="BBDD", menu=bbddMenu) # Añadimos el menú de base de datos a la barra de menú
barraMenu.add_cascade(label="Borrar", menu=borrarMenu) # Añadimos el menú de borrar a la barra de menú
barraMenu.add_cascade(label="CRUD", menu=crudMenu) # Añadimos el menú CRUD a la barra de menú
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu) # Añadimos el menú de ayuda a la barra de menú


#------------------------------contruccioón de campos grid------------------
# Creamos etiquetas y campos de entrada para los datos
miFrame=Frame(root) # Creamos un marco para organizar los widgets
miFrame.pack() # Añadimos el marco a la ventana principal

cuadroId=Entry(miFrame) # Creamos un campo de entrada para el ID
cuadroId.grid(row=0, column=1, padx=10, pady=10) # Colocamos el campo en la cuadrícula

cuadroNombre=Entry(miFrame) # Creamos un campo de entrada para el nombre
cuadroNombre.grid(row=1, column=1, padx=10, pady=10) # Colocamos el campo en la cuadrícula
cuadroNombre.config(fg="blue", justify="center") # Configuramos el color y la alineación del texto en el campo de entrada

cuadroPass=Entry(miFrame) # Creamos un campo de entrada para la contraseña
cuadroPass.grid(row=2, column=1, padx=10, pady=10) # Colocamos el campo en la cuadrícula
cuadroPass.config(show="*") # Configuramos el campo para ocultar la contraseña

cuadroApellidos=Entry(miFrame) # Creamos un campo de entrada para los apellidos
cuadroApellidos.grid(row=3, column=1, padx=10, pady=10) # Colocamos el campo en la cuadrícula

cuadroDireccion=Entry(miFrame) # Creamos un campo de entrada para la dirección
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10) # Colocamos el campo en la cuadrícula
textoComentarios=Text(miFrame, width=16, height=5) # Creamos un campo de texto para comentarios
textoComentarios.grid(row=5, column=1, padx=10, pady=10) # Colocamos el campo de texto en la cuadrícula
scrollVert=Scrollbar(miFrame, command=textoComentarios.yview) # Creamos una barra de desplazamiento vertical para el campo de texto
scrollVert.grid(row=5, column=2, sticky="nsew") # Colocamos la barra de desplazamiento en la cuadrícula
textoComentarios.config(yscrollcommand=scrollVert.set) # Configuramos la barra de desplazamiento para que funcione con el campo de texto



root.mainloop() # Iniciamos el bucle principal de la aplicación
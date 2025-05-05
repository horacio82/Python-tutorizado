# PILDORAS INFORMATICAS
# Python tutorizado. BBDD. Aplicación gráfica CRUD I, II, III, IV,V, VI. 
# Vídeo 99, 100, 101, 102, 103, 104

from tkinter import * # Importamos la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox # Importamos la librería messagebox para mostrar mensajes emergentes
import sqlite3 # Importamos la librería sqlite3 para trabajar con bases de datos SQLite

root=Tk() # Creamos la ventana principal de la aplicación

barraMenu=Menu(root) # Creamos una barra de menú en la ventana principal
root.config(menu=barraMenu, width=300, height=300) # Configuramos la ventana principal para que use la barra de menú

bbddMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para la base de datos
bbddMenu.add_command(label="Conectar") # Añadimos una opción al menú para conectar a la base de datos
bbddMenu.add_command(label="Salir") # Añadimos una opción al menú para desconectar de la base de datos

borrarMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para borrar registros
borrarMenu.add_command(label="Borrar") # Añadimos una opción al menú para borrar registros

crudMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para operaciones CRUD
crudMenu.add_command(label="Crear") # Añadimos una opción al menú para crear registros
crudMenu.add_command(label="Leer") # Añadimos una opción al menú para leer registros
crudMenu.add_command(label="Actualizar") # Añadimos una opción al menú para actualizar registros
crudMenu.add_command(label="Borrar") # Añadimos una opción al menú para eliminar registros
ayudaMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para ayuda
ayudaMenu.add_command(label="Licencia") # Añadimos una opción al menú para mostrar ayuda
ayudaMenu.add_command(label="Acerca de...") # Añadimos una opción al menú para mostrar información sobre la aplicación

barraMenu.add_cascade(label="BBDD", menu=bbddMenu) # Añadimos el menú de base de datos a la barra de menú
barraMenu.add_cascade(label="Borrar", menu=borrarMenu) # Añadimos el menú de borrar a la barra de menú
barraMenu.add_cascade(label="CRUD", menu=crudMenu) # Añadimos el menú CRUD a la barra de menú
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu) # Añadimos el menú de ayuda a la barra de menú


#-------------------------construccón de campos grid-------------------------

miFrame=Frame(root) # Creamos un marco (frame) para organizar los widgets
miFrame.pack() # Añadimos el marco a la ventana principal

cuadroId=Entry(miFrame) # Creamos un campo de entrada para el ID
cuadroId.grid(row=0, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula

cuadroNombre=Entry(miFrame) # Creamos un campo de entrada para el nombre
cuadroNombre.grid(row=1, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula
cuadroNombre.config(fg="blue", justify="right") # Configuramos el color y la alineación del texto en el campo de entrada

cuadroPass=Entry(miFrame) # Creamos un campo de entrada para la contraseña
cuadroPass.grid(row=2, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula
cuadroPass.config(show="*") # Configuramos el campo de entrada para ocultar la contraseña

cuadroApellido=Entry(miFrame) # Creamos un campo de entrada para el apellido
cuadroApellido.grid(row=3, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula

cuadroDireccion=Entry(miFrame) # Creamos un campo de entrada para la dirección
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula

textoComentario=Text(miFrame, width=16, height=5) # Creamos un campo de texto para comentarios
textoComentario.grid(row=5, column=1, padx=10, pady=10) # Colocamos el campo de texto en la cuadrícula
scrollVert=Scrollbar(miFrame, command=textoComentario.yview) # Creamos una barra de desplazamiento vertical para el campo de texto
scrollVert.grid(row=5, column=2, sticky="nsew") # Colocamos la barra de desplazamiento en la cuadrícula
textoComentario.config(yscrollcommand=scrollVert.set) # Configuramos el campo de texto para usar la barra de desplazamiento


#-------------------------construcción de etiquetas-------------------------

etiquetaId=Label(miFrame, text="Id:") # Creamos una etiqueta para el ID
etiquetaId.grid(row=0, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula

etiquetaNombre=Label(miFrame, text="Nombre:") # Creamos una etiqueta para el nombre
etiquetaNombre.grid(row=1, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula

etiquetaPass=Label(miFrame, text="Contraseña:") # Creamos una etiqueta para la contraseña
etiquetaPass.grid(row=2, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula

etiquetaApellido=Label(miFrame, text="Apellido:") # Creamos una etiqueta para el apellido
etiquetaApellido.grid(row=3, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula

etiquetaDireccion=Label(miFrame, text="Dirección:") # Creamos una etiqueta para la dirección
etiquetaApellido.grid(row=4, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula

etiquetaComentario=Label(miFrame, text="Comentarios:") # Creamos una etiqueta para los comentarios  
etiquetaComentario.grid(row=5, column=0, padx=10, pady=10) # Colocamos la etiqueta en la cuadrícula


#-------------------------construcción de botones-------------------------

miFrameBotones=Frame(root) # Creamos un marco (frame) para los botones
miFrameBotones.pack() # Añadimos el marco a la ventana principal

botonCrear=Button(miFrameBotones, text="Crear") # Creamos un botón para crear registros
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonLeer=Button(miFrameBotones, text="Leer") # Creamos un botón para leer registros
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonActualizar=Button(miFrameBotones, text="Actualizar") # Creamos un botón para actualizar registros
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonBorrar=Button(miFrameBotones, text="Borrar") # Creamos un botón para borrar registros
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula





root.mainloop() # Iniciamos el bucle principal de la aplicación
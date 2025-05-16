# PILDORAS INFORMATICAS
# Python tutorizado. BBDD. Aplicación gráfica CRUD I, II, III, IV,V, VI. 
# Vídeo 99, 100, 101, 102, 103, 104

from tkinter import * # Importamos la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox # Importamos la librería messagebox para mostrar mensajes emergentes
import sqlite3 # Importamos la librería sqlite3 para trabajar con bases de datos SQLite

root=Tk() # Creamos la ventana principal de la aplicación



#-------------------------conexión a la base de datos-------------------------

def conectarBBDD(): # Definimos la función para conectar a la base de datos

    miConexion=sqlite3.connect("Aplicacion BBDD/NegocioUsuarios") # Conectamos a la base de 
    
    miCursor=miConexion.cursor() # Creamos un cursor para ejecutar comandos SQL


    try: # Intentamos crear la tabla
        miCursor.execute('''
                     
            CREATE TABLE DATOSUSUARIOS(
                     
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(70),
                COMENTARIOS VARCHAR(120)
            )
                     
    ''')         

        messagebox.showinfo("BBDD", "Base de datos creada con éxito") # Mostramos un mensaje de éxito al crear la base de datos        
    except:
        messagebox.showwarning("BBDD", "La base de datos ya existe")

def salirAplicacion(): # Definimos la función para salir de la aplicación

    valor_salir=messagebox.askquestion("Salir", "¿Quieres salir de la aplicación?") # 
    if valor_salir=="yes":
        root.destroy() # Si el usuario confirma, cerramos la aplicación
   

def limpiarCampos(): # Definimos la función para limpiar los campos de entrada
    mi_Id.set("") # Limpiamos el campo de ID
    mi_Nombre.set("") # Limpiamos el campo de nombre
    mi_Apellido.set("") # Limpiamos el campo de apellido
    mi_Pass.set("") # Limpiamos el campo de contraseña
    mi_Direccion.set("") # Limpiamos el campo de dirección
    textoComentario.delete(1.0, END) # Limpiamos el campo de comentarios


def crear(): # Definimos la función para crear un nuevo registro
    mi_conexion=sqlite3.connect("Aplicacion BBDD/NegocioUsuarios") # Conectamos a la base de datos
    mi_cursor=mi_conexion.cursor() # Creamos un cursor para ejecutar comandos SQL
    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+mi_Nombre.get()+"','"+mi_Pass.get()+"','"+mi_Apellido.get()+"','"+mi_Direccion.get()+"','"+textoComentario.get("1.0", END)+"')") # Insertamos un nuevo registro en la tabla
    mi_conexion.commit() # Guardamos los cambios en la base de datos
    messagebox.showinfo("BBDD", "Registro insertado con éxito") # Mostramos un mensaje de éxito al insertar el registro

#---------------------------------------------------------------------

barraMenu=Menu(root) # Creamos una barra de menú en la ventana principal
root.config(menu=barraMenu, width=300, height=300) # Configuramos la ventana principal para que use la barra de menú


#-------------------------variables de control-------------------------

mi_Id =StringVar() # Creamos una variable de control para el ID
mi_Nombre =StringVar() # Creamos una variable de control para el nombre
mi_Apellido =StringVar() # Creamos una variable de control para el apellido
mi_Pass=StringVar() # Creamos una variable de control para la contraseña
mi_Direccion=StringVar() # Creamos una variable de control para la dirección


#----------------------------------------------------------------------

bbddMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para la base de datos
bbddMenu.add_command(label="Conectar", command=conectarBBDD) # Añadimos una opción al menú para conectar a la base de datos
bbddMenu.add_command(label="Salir", command=salirAplicacion) # Añadimos una opción al menú para desconectar de la base de datos

borrarMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para borrar registros
borrarMenu.add_command(label="Borrar", command=limpiarCampos) # Añadimos una opción al menú para borrar registros

crudMenu=Menu(barraMenu, tearoff=0) # Creamos un menú desplegable para operaciones CRUD
crudMenu.add_command(label="Crear", command=crear) # Añadimos una opción al menú para crear registros
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

cuadroId=Entry(miFrame, textvariable=mi_Id) # Creamos un campo de entrada para el ID
cuadroId.grid(row=0, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula

cuadroNombre=Entry(miFrame, textvariable=mi_Nombre) # Creamos un campo de entrada para el nombre
cuadroNombre.grid(row=1, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula
cuadroNombre.config(fg="blue", justify="right") # Configuramos el color y la alineación del texto en el campo de entrada

cuadroPass=Entry(miFrame, textvariable=mi_Pass) # Creamos un campo de entrada para la contraseña
cuadroPass.grid(row=2, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula
cuadroPass.config(show="*") # Configuramos el campo de entrada para ocultar la contraseña

cuadroApellido=Entry(miFrame, textvariable=mi_Apellido) # Creamos un campo de entrada para el apellido
cuadroApellido.grid(row=3, column=1, padx=10, pady=10) # Colocamos el campo de entrada en la cuadrícula

cuadroDireccion=Entry(miFrame, textvariable=mi_Direccion) # Creamos un campo de entrada para la dirección
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

botonCrear=Button(miFrameBotones, text="Crear", command=crear) # Creamos un botón para crear registros
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonLeer=Button(miFrameBotones, text="Leer") # Creamos un botón para leer registros
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonActualizar=Button(miFrameBotones, text="Actualizar") # Creamos un botón para actualizar registros
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula

botonBorrar=Button(miFrameBotones, text="Borrar") # Creamos un botón para borrar registros
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10) # Colocamos el botón en la cuadrícula





root.mainloop() # Iniciamos el bucle principal de la aplicación
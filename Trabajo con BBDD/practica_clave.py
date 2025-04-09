#  PILDORAS INFORMATICAS
#Python tutorizado. BBDD III. Vídeo 95

import sqlite3 # Importar la librería sqlite3 para trabajar con bases de datos SQLite

mi_conexion = sqlite3.connect("Trabajo con BBDD/GestionPedidos") # Conectar a la base de datos (se crea si no existe)

mi_cursor = mi_conexion.cursor() # Crear un cursor para ejecutar comandos SQL

# Crear una tabla con cuatro columnas: CODIGO_ARTICULO, NOMBRE_ARTICULO, PRECIO y SECCION:

#mi_cursor.execute(''' 
#CREATE TABLE PRODUCTOS (
    #CODIGO_ARTICULO VARCHAR (4) PRIMARY KEY,
    #NOMBRE_ARTICULO VARCHAR (40),
    #PRECIO INTEGER,
    #SECCION VARCHAR (20)
#)
#''')

misProductos = [
    ('P1', 'Camiseta', 25, 'Moda'), # Crear una lista de tuplas con varios registros
    ('P2', 'Pantalón', 20, 'Moda'),
    ('P3', 'Jersey', 30, 'Moda'),
    ('P4', 'Chaqueta', 50, 'Moda'),
    ('P5', 'Zapatos', 80, 'Calzado'),
    ('P6', 'Botas', 100, 'Calzado')
]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", misProductos) # Insertar varios registros a la vez

mi_conexion.commit() # Guardar los cambios en la base de datos

mi_cursor.close() # Cerrar el cursor

mi_conexion.close() # Cerrar la conexión a la base de datos
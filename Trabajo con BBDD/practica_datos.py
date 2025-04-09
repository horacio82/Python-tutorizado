#PILDORAS INFORMATICAS
#Python tutorizado. BBDD I,II. Vídeo 93,94

import sqlite3 # Importar la librería sqlite3 para trabajar con bases de datos SQLite

mi_conexion = sqlite3.connect("Trabajo con BBDD/miBBDD") # Conectar a la base de datos (se crea si no existe)

mi_cursor = mi_conexion.cursor() # Crear un cursor para ejecutar comandos SQL

#mi_cursor.execute("CREATE TABLE PRODUCTOS (ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR (20))") # Crear una tabla con tres columnas: ARTICULO, PRECIO y SECCION

#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES ('Camiseta', 25, 'Moda')") # Insertar un registro en la tabla

'''muchosProductos = [
    ('Pantalón', 20, 'Moda'), # Crear una lista de tuplas con varios registros
    ('Jersey', 30, 'Moda'),
    ('Chaqueta', 50, 'Moda'),
    ('Zapatos', 80, 'Calzado'),
    ('Botas', 100, 'Calzado')
]'''

#mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", muchosProductos) # Insertar varios registros a la vez

mi_cursor.execute("SELECT * FROM PRODUCTOS") # Seleccionar todos los registros de la tabla
muchosProductos = mi_cursor.fetchall() # Obtener todos los registros seleccionados

print(muchosProductos) # Imprimir los registros obtenidos

for p in muchosProductos: # Recorrer los registros obtenidos
    print("Artículo:", p[0]) # Imprimir el artículo
    print("Precio:", p[1]) # Imprimir el precio
    print("Sección:", p[2]) # Imprimir la sección
    print("-------------------") # Separador

#mi_conexion.commit() # Guardar los cambios en la base de datos

mi_cursor.close() # Cerrar el cursor

mi_conexion.close() # Cerrar la conexión a la base de datos
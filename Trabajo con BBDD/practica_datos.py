#PILDORAS INFORMATICAS
#Python tutorizado. BBDD I. Vídeo 93

import sqlite3 # Importar la librería sqlite3 para trabajar con bases de datos SQLite

mi_conexion = sqlite3.connect("Trabajo con BBDD/miBBDD") # Conectar a la base de datos (se crea si no existe)

mi_cursor = mi_conexion.cursor() # Crear un cursor para ejecutar comandos SQL

#mi_cursor.execute("CREATE TABLE PRODUCTOS (ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR (20))") # Crear una tabla con tres columnas: ARTICULO, PRECIO y SECCION

mi_cursor.execute("INSERT INTO PRODUCTOS VALUES ('Camiseta', 25, 'Moda')") # Insertar un registro en la tabla

mi_conexion.commit() # Guardar los cambios en la base de datos









mi_conexion.close() # Cerrar la conexión a la base de datos
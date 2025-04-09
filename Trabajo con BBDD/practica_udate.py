#  PILDORAS INFORMATICAS
#Python tutorizado. BBDD IV. Vídeo 96

import sqlite3 # Importar la librería sqlite3 para trabajar con bases de datos SQLite

mi_conexion = sqlite3.connect("Trabajo con BBDD/GestionPedidos") # Conectar a la base de datos (se crea si no existe)
mi_cursor = mi_conexion.cursor() # Crear un cursor para ejecutar comandos SQL

mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=1") 



mi_conexion.commit() # Guardar los cambios en la base de datos
mi_cursor.close() # Cerrar el cursor
mi_conexion.close() # Cerrar la conexión a la base de datos
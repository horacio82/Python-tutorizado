#PILDORAS INFORMATICAS
#Python tutorizado. BBDD V. Conectando con PostgreSQL. Vídeo 97

import psycopg2 # Importamos la librería psycopg2 para conectarnos a PostgreSQL

mi_conexion = psycopg2.connect( host="localhost", database="Personas", user="postgres", pasword="root") # Host de la base de datos

mi_cursos = mi_conexion.cursor() # Creamos un cursor para ejecutar las consultas SQL

mi_cursos.execute("INSERT INTO ALUMNOS VALUES ('Pepe','Martín')") # Insertamos un nuevo registro en la tabla ALUMNOS
mi_conexion.commit() # Confirmamos los cambios en la base de datos
mi_cursos.close() # Cerramos el cursor
mi_conexion.close() # Cerramos la conexión a la base de datos


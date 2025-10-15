#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Condicional If I. Vídeo 14

#Función:
def evaluarAlumno(nota):
    valoracion = "Aprobado"

    if nota<5:
        valoracion = "Suspenso"
    return valoracion

#Llamando a la función con parámetro(10)
print(evaluarAlumno(10))
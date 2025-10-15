#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Condicional If I, II - Vídeo 14, 15

#Función:
def evaluarAlumno(nota):
    valoracion = "desconocida"

    if nota<5:
        valoracion = "suspenso"
    elif nota>10:
        valoracion = "nota incorrecta" 
    else: 
        valoracion = "aprobado"
    return valoracion

notaAlumno = int(input("Introduce la nota: "))

#Llamando a la función:
print(evaluarAlumno(notaAlumno))
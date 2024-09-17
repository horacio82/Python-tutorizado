#Pildoras informaticas
#Estructuras de control de flujo If I y II 
# (video 14 y 15)

def evaluarAlumno(nota):
    valoracion="Desconocida"
    if nota<5:
        valoracion="Suspenso..."

    elif nota>10:
        valoracion="Nota incorrecta"    
    else:
        valoracion="Aprobado"    
    return valoracion

notaAlumno=int(input("Introduce la nota: "))
print(evaluarAlumno(notaAlumno))


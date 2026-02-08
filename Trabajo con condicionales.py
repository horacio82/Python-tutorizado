#PILDORAS INFORMATICAS
#Python tutorizado. Control de flujo. Condicional If I, II, III - Vídeo 14, 15, 16

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


#ESTRUCTURAS DE FLUJO if III - video 16---------------------

print("Verificación de acceso")

nota_alumno = int(input("Introduce tu nota: "))

if nota_alumno<5:
    print("Insuficiente")
elif nota_alumno<6:
    print("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else:
    print("Sobresaliente")


#-----------------------------------------------------------
print("Obtención carnet de conducir")

edad = int(input("Introduce tu edad: "))

if edad>=18 and edad<90:
    print("Puedes intentar obtener el carnet")
else:
    print("Lo siento, no cumples con la edad necesaria")

#-----------------------------------------------------------

print("Obtención de carnet de conducir.")

edad1=int(input("Introduce tu edad, por favor: "))

vision=input("¿Tienes la visión correcta?: ")

if edad1 >=18 and edad1<90 and vision=="si":
    print("Puedes obtener el carnet.")
else:
    print("Lo siento, no cumples con los requisitos...")


#BECA DE ESTUDIOS----------------------------------------

print("Obtención beca de estudios")

nota_media=int(input("Introduce tu nota media: "))

hermanos_en_centro=int(input("Introduce n° de hermanos: "))

distancia_al_centro=int(input("Introduce la distancia al centro de estudios: "))

renta_familiar=int(input("Introduce renta familiar: "))

if nota_media>8 or hermanos_en_centro>3 or distancia_al_centro>10 or renta_familiar<20000:
    print("¡Se te concede la beca!")
else:
    print("Lo siento, no cumples con los requisitos...")
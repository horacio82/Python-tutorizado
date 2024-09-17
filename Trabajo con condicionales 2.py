#Pildoras informaticas (video 16)
#Estructuras control flujo If III

'''print("Obtención de carnet de conducir.")

edad=int(input("Introduce tu edad, por favor: "))

vision=input("¿Tienes la visión correcta?: ")

if edad>18 and edad<90 and vision=="si":
    print("Puedes intentar obtener el carnet.")
else:
    print("Lo siento, no cumples con la edad necesaria.")'''


print("Obtención beca de estudios.")

nota_media=int(input("Introduce tu nota media: "))
hermanos_en_centro=int(input("Introduce n° de hermanos: "))
distancia_al_centro=int(input("Introduce distancia al centro: "))
renta_familiar=int(input("Introduce renta familiar: "))

if (nota_media>8 and hermanos_en_centro>3 and distancia_al_centro>10) or renta_familiar<20000:
    print("Se te concede la beca." )
else:
    print("Lo siento, no cumples con los requisitos.")


#PILDORAS INFORMATICAS
#Python tutorizado. Instrucciones pass, continue y else. Vídeo 21

nombre="Horacio Molinari"

contador=0

for i in nombre:

    if i==" ":
        continue
    contador+=1

print(contador)

#------------------------------------------------

class EjemploClase():

    pass

#--------------------------------------------------

email=input("Introduce tu email: ")

for i in email:

    if i=="@":

        arroba=True
        break

else:

    arroba=False

print(arroba)
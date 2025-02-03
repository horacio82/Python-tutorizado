#PILDORAS INFORMÁTICAS
#Python tutorizado. Explicación Ejercicio excepciones (VIDEO 29)

nombresPersonas = []

def agregar_a_lista(lista, nombreIntroducido): #Función que añade un nombre a la lista
    try:
        if nombreIntroducido in lista: 
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error. Este nombre ya se ha introducido.",nombreIntroducido)

introducidos=1

while introducidos<11:
    nombre=input("Introduce nombre: ")
    agregar_a_lista(nombresPersonas, nombre)
    introducidos+=1

print(nombresPersonas)    
#PILDORAS INFORMATICAS
#Python tutorizado. Conversiones de datos. Vídeo 13

a = "15"

b = "35"

#conversion, texto a entero:
print(int(a)+int(b))

#conversion, texto a flotante:
print(float(a)+float(b))


edad = 43

print("Mi edad es: " +str(edad) + " años")



empleados = ["Ana", "Oscar", "Pedro", "Juan"]

#Devuelve con string los elementos de la lista, con un separador:
print("-".join(empleados))


lista = "José, Walter, Matías"

#Convierte en una lista el string:
print(lista.split())
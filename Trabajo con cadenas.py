#PILDORAS INFORMÁTICAS
#Python tutorizado. Métodos útiles y especiales I. Vídeo 41

edad = input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("El valor introducido no es correcto")
    edad = input("Introduce tu edad: ")

if(int(edad)<18):
    print("No puedes pasar.")
else:
    print("Puedes pasar.")       
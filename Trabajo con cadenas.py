#PILDORAS INFORMATICAS
#Python tutorizado. Métodos útiles y especiales I. Vídeo 41

nUsuario=input("Introduce tu usuario: ")

print("El usuario introducido es: ",nUsuario.upper())


edad=input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("El valor introducido no es correcto.")
    edad=input("Introduce tu edad, por favor: ")

if(int(edad)<18):
    print("No puedes pasar.")
else:
    print("Puedes pasar.")        
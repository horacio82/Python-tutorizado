#Pildoras informáticas - Python tutorizado. Generadores I. Vídeo 23


#Finción tradicional:
def generarPares(limite):

    num=1

    numerosPares=[]

    while num<limite:
        numerosPares.append(num*2)
        num=num+1

    return numerosPares

print(generarPares(6))    


#Función con generador:
def generarPares1(limit):
    numero=1

    while numero<limit:
        yield numero*2
        numero=numero+1

sucesionPares=generarPares1(6)

for i in sucesionPares:
    print("->",i)
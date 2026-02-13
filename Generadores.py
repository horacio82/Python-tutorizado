#PILDORAS INFORMATICAS
#Generadores I,II Vídeo 23, 24

def generarPares(limite):
    num=1

    while num < limite:
        yield num*2

        num=num+1
    
sucesionPares = generarPares(6)    

print(next(sucesionPares))

print("Ahora va el siguiente valor: ")

print(next(sucesionPares))


#--------------------video 24---------------------------

def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letra_capital in capital:
            yield from capital
        

capitales_devueltas = capitales_mundo("Berlín","Roma","Bogotá","Buenos Aires")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
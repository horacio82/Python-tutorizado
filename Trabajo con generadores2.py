#Pildoras informáticas
#Python tutorizado. Generadores II. Vídeo 24

def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letra_capital in capital:
            yield from capital

capitales_devueltas = capitales_mundo("Berlín","Roma","Bogotá","Pekin","Hanoi")        

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
#PILDORAS INFORMATICAS
#Python tutorizado. Funciones lambda I, II. Vídeo 89, 90

def area_triangulo(base,altura): #Función normal
    return (base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)

print(triangulo1)
print(triangulo2)


print('---------------------------------------------')

area_triangulo = lambda base,altura:(base*altura)/2 #Función lambda

print(area_triangulo(5,7))
print(area_triangulo(9,6))


print('---------------------------------------------')

calculo_cubo = lambda base, exponente:base**exponente#Función lambda

print(calculo_cubo(5,6))
# Output:

print('---------------------------------------------')  

destacar_valor = lambda comision:'¡${}!'.format(comision)   #Función lambda
comision_Ana = 15585
print(destacar_valor(comision_Ana))

print('---------------------------------------------')  

mi_lista = [(11,5),(15,7),(2,4),(15,19),(8,4)]

mi_lista.sort(key=lambda t:t[0]+t[1]) #Ordena la lista por la suma de los elementos de las tuplas
print(mi_lista)

print('---------------------------------------------')

musicos = ['Soda Stereo','Charly Garcia','Chris Cornell','Fito Paez']

musicos.sort(key=lambda m:m.split()[1]) #Ordena la lista por el apellido
print(musicos)
#Pildoras informáticas - Python tutorizado. Generadores I. Vídeo 23


#Finción tradicional:
def generarPares(limite):

    num=1

    numerosPares=[]#Crea una lista vacía para guardar los pares.

    while num<limite:#Mientras que num sea menor que limite.
        numerosPares.append(num*2)#multiplica num por 2 y agrega el resultado a la lista numerosPares.
        num=num+1 #incrementa num en 1 en cada iteración.

    return numerosPares #devuelve la lista numerosPares al final del bucle.

print(generarPares(6))    


#Función con generador: Similar a la función anterior, pero en lugar de usar una lista para almacenar los resultados, 
# se utiliza yield para generar los valores uno a uno.
def generarPares1(limit):
    numero=1

    while numero<limit:
        yield numero*2 #produce un número par cada vez que la función es llamada, permitiendo ahorrar memoria 
        #ya que no se almacena toda la lista en memoria.
        numero=numero+1

sucesionPares=generarPares1(6) #Creación de un objeto generador

for i in sucesionPares: #Itera sobre los valores generados por generarPares1 e imprime cada uno.
    print("->",i)

#En resumen, ambos métodos tienen la misma finalidad de generar números pares hasta un límite dado. 
# La primera función utiliza una lista para almacenar y devolver todos los números a la vez, 
# mientras que la segunda utiliza un generador (yield), produciendo los números uno por uno bajo demanda, 
# lo que es más eficiente en términos de memoria.    
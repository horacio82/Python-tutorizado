#PILDORAS INFORMÁTICAS
#Python tutorizado. Excepciones III. Vídeo 27


def divide(): #Definición de la función (sin parámetros)
    try: #Este bloque intenta ejecutar las líneas dentro de él y maneja posibles excepciones.

#op1 y op2 son variables que almacenan los números ingresados por el usuario, convertidos a float.        
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundp número: ")))
        print("El resultado es: ",str(op1/op2)) #Luego se intenta dividir op1 por op2 y se imprime el resultado.
    except ZeroDivisionError: #Si se intenta dividir por cero, se captura esta excepción y se imprime un mensaje.
        print("No se puede dividir por 0.")
    except ValueError: #Si el usuario ingresa un valor que no puede ser convertido a float, 
        #se captura esta excepción y se imprime un mensaje indicando que el valor no es numérico.
        print("El valor introducido no es numérico.")

    finally: #Este bloque se ejecuta siempre, independientemente de si se lanzó una excepción o no.
        print("Se ha intentado ejecutar la función en su totalidad.")

        
divide() #Aquí se llama a la función divide para que se ejecute.

#Después de que la función divide ha terminado de ejecutarse, se imprime un mensaje final indicando
#  que el cálculo ha finalizado y el programa continúa.
print("Cálculo finalizado. Continuamos con el programa.")

'''Este código toma dos números como entrada del usuario y los divide, manejando posibles errores como división por cero
y valores no numéricos. El bloque finally asegura que se imprima un mensaje al final, independientemente de si hubo un error o no.'''
#PILDORAS INFORMATICAS
#Python tutorizado. Excepciones III. Vídeo 27

def divide():

    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el primer número: ")))
    
        print("El resultado es: "+str(op1/op2))

    except ZeroDivisionError:
        print("No se puede dividir por 0")

    except ValueError:
        print("EL valor introducido no es correcto")

    finally:
        print("Se ha intentado ejecutar la función en su totalidad...")

divide()

print("Cálculo finalizado. Continuamos con el programa.")
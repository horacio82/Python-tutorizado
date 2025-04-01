#PILDORAS INFORMATICAS
#Python tutorizado. Decoradores I, II. Vídeo 91, 92

def funcion_decoradora(funcion_parametro):# Decorador
    def funcion_interior(*args, **kwargs): # *args y **kwargs permiten pasar un número variable de argumentos
        print("A continuación voy a realizar un cálculo")
        funcion_parametro(*args, **kwargs)
        print("He terminado el cálculo")
    return funcion_interior

@funcion_decoradora # Decorador
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(5,7)
resta(20,5)        
potencia(base=5,exponente=3)
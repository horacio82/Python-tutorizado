#PILDORAS INFORMATICAS
#Python tutorizado. Decoradores I. Vídeo 91

def funcion_decoradora(funcion_parametro):# Decorador
    def funcion_interior():
        print("A continuación voy a realizar un cálculo")
        funcion_parametro()
        print("He terminado el cálculo")
    return funcion_interior

@funcion_decoradora # Decorador
def suma():
    print(25+30)
    
@funcion_decoradora
def resta():
    print(80-25)

suma()
resta()        
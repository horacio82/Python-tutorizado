#PILDORAS INFORMÁTICAS
#Python tutorizado. Métodos útiles y especiales II. Vídeo 42/43

class Persona(): #Definición de clase.

#Este es el constructor de la clase Persona, que se ejecuta cuando se crea una nueva instancia de la clase. 
#El parámetro **datos permite pasar un número variable de argumentos clave-valor:

    def __init__(self, **datos): #Método constructor.

        elementos = datos.items() #Obtiene los pares clave-valor del diccionario datos.

        for clave, valor in elementos: #Itera sobre cada par clave-valor en elementos.
            print(clave,"", valor) #Imprime cada clave y su correspondiente valor.

#Creación de una instancia de Persona:
#Aquí se crea una nueva instancia de Persona, pasando las claves y valores 
#Nombre, Apellido y Edad como argumentos.
p1 = Persona(Nombre="Horacio", Apellido="Molinari", Edad=42)

#Impresión de la instancia p1:
print(p1)
#Esta línea intenta imprimir la instancia p1. Sin embargo, como no se ha definido un método __str__ o __repr__ en la clase Persona, 
# esto imprimirá una representación por defecto del objeto p1, que generalmente será algo como <__main__.Persona object at 0x...> 
# indicando la ubicación en memoria del objeto.

#Esto indica que los argumentos se imprimen correctamente desde el constructor 
# y luego se imprime la representación por defecto del objeto p1.
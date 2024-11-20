#PILDORAS INFORMÁTICAS
#Python tutorizado. POO XII. Vídeo 40

#Definición de la clase Persona:
class Persona():
    #método hablar que devuelve la cadena "Hablo como una persona".:
    def hablar(self):
        return "Hablo como una personna"
    
#Definición de la clase Trabajador que hereda de Persona:    
class Trabajador(Persona):
#La clase Trabajador hereda de Persona, pero sobrescribe el método hablar para devolver 
# Hablo como un trabajador".
    def hablar(self):
        return "Hablo como un trabajador"    
    
class Director(Trabajador):#Definición de la clase Director que hereda de Trabajador.
#La clase Director hereda de Trabajador y también sobrescribe el método hablar para devolver 
# "Hablo como un director".
    def hablar(self):
        return "Hablo como un director"

#Creación de instancias de las 3 clases:
Antonio = Persona()
Maria = Trabajador()
Ana = Director()

#Definición de la función hazlesHablar:
def hazlesHablar(listaDeLasPersonas):
#Esta función toma una lista de objetos y llama al método hablar de cada objeto, 
#imprimiendo el resultado.
    for persona in listaDeLasPersonas:
        print(persona.hablar())

#Llamada a los métodos hablar de cada instancia:
print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())
print("--------------------------------------------------------")

#Creación de una lista de instancias y llamada a hazlesHablar:
listaPersonas = [Antonio, Ana, Maria] #listaPersonas que contiene las tres instancias y se pasa a la función hazlesHablar.
hazlesHablar(listaPersonas)

'''Este código muestra cómo el método hablar es sobrescrito en las clases derivadas y cómo se utiliza la herencia para manejar polimorfismo. Cada instancia usa su propia implementación del método hablar.'''
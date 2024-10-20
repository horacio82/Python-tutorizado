#PILDORAS INFORMÁTICAS
#Python tutorizado. POO XII. Vídeo 40

class Persona():

    def hablar(self):
        return "Hablo como una personna"
    
class Trabajador(Persona):

    def hablar(self):
        return "Hablo como un trabajador"    
    
class Director(Trabajador):

    def hablar(self):
        return "Hablo como un director"


Antonio = Persona()
Maria = Trabajador()
Ana = Director()


def hazlesHablar(listaDeLasPersonas):

    for persona in listaDeLasPersonas:
        print(persona.hablar())

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())
print("--------------------------------------------------------")

listaPersonas = [Antonio, Ana, Maria]
hazlesHablar(listaPersonas)


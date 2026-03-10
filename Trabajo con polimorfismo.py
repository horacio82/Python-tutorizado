#PILDORAS INFORMATICAS
#Python tutorizado. POO XII. Vídeo 40

class Persona():
    def hablar(self):
        return "Hablo como una persona"
    
class Trabajador():
    def hablar(self):
        return "Hablo como un trabajador"

class Director():
    def hablar(self):
        return "Hablo como un director"


def hazlesHablar(objeto):
    print(objeto.hablar())


Antonio=Persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("------------------------------------------------")

listaPersonas=[Antonio,Ana,Maria]

hazlesHablar(Ana)
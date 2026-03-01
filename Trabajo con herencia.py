#PILDORAS INFORMATICAS
#Python tutorizado. POO VIII. Vídeo 36

class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self):
        return "Nombre:",self.nombre,"Apellido:",self.apellido,"Edad:",self.edad


    def habla(self):
        return "Estoy hablando"

    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy caminando"

    def come(self):
        return "Estoy comiendo"    
    

class Estudiante(Persona):
    def estudia(self):
        return "Estoy estudiando"


persona1 = Persona("Ana","Gómez",35)

estudiante1 = Estudiante("Juan","Díaz",21)

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
#PILDORAS INFORMÁTICAS
#Python tutorizado. POO VIII. Vídeo 36/37

class Persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " edad: " +str(self.edad)    
    
    def habla(self):

        return "Estoy hablando"
    
    def piensa(self):

        return "Estoy pensando"
    
    def camina(self):

        return "Estoy caminando"
    
    def come(self):

        return "Estoy comiendo"
    

class Estudiante(Persona):    
    
    def __init__(self, nombre, apellido, edad, escuela):

        super().__init__(nombre, apellido, edad)

        self.escuela=escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " escuela: " + self.escuela    

    def estudia(self):
        return "Estoy estudiando"    
    

persona1=Persona("Horacio","Molinari",42)    

estudiante1=Estudiante("Juan","Diaz",35, "San Javier")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
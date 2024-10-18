#PILDORAS INFORMÁTICAS
#Python tutorizado. POO VIII. Vídeo 36/37
#---------------------------------------------------------------------------
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
    
#---------------------------------------------------------------------------
class Estudiante(Persona):    
    
    def __init__(self, nombre, apellido, edad, escuela):

        Persona.__init__(self, nombre, apellido, edad)

        self.escuela=escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " escuela: " + self.escuela    

    def estudia(self):
        return "Estoy estudiando"    
    
#---------------------------------------------------------------------------
class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):

        Persona.__init__(self, nombre, apellido, edad)

        self.empresa=empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Empresa: " + self.empresa    

    def trabaja(self):
        return "Estoy trabajando"    

#---------------------------------------------------------------------------
class Director(Estudiante, Trabajador):

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)

        self.bonus=bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Bonus: " + str(self.bonus)
    
    def dirige(self):
        return "Estoy dirigiendo"
        
#---------------------------------------------------------------------------



persona1=Persona("Horacio","Molinari",42)    

estudiante1=Estudiante("Juan","Diaz",35, "San Javier")

print("Persona 1 - " + persona1.getDatosPersonales())
print("Estudiante - " + estudiante1.getDatosPersonales())

print("-------------------------------------------------------------------")

trabajador1=Trabajador("Antonio", "López", 45, "Google")
print("Trabajador - " + trabajador1.getDatosPersonales())

director1=Director("Marcelo", "Péres", 48, "Microsoft", "San Juan", 90000)
print("Director - " + director1.getDatosPersonales())
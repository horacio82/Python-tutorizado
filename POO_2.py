#PILDORAS INFORMATICAS
#Python tutorizado. POO V. Vídeo 33

class Persona():
    nombre = ""
    apellido = ""
    edad = 0
    genero = "Sin definir"

    def __init__(self, nombre, apellido, edad, genero):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.genero=genero

    def habla(self):

        return "La persona que se llama",self.nombre,"está hablando."
    
    def camina(self):
        return "La persona que se llama",self.nombre,"está caminando."
    
    def getDatos(self):
        return "Nombre: ",self.nombre,"Apellido: ",self.apellido,"Edad: ",self.edad,"Género: ",self.genero
    
p1 = Persona("Horacio","Molinari",42,"masculino")
print(p1.getDatos())

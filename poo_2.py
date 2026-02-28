#PILDORAS INFORMATICAS
#Python tutorizado. POO V. Vídeo 33

class Persona():
    nombre = ""
    apellido = ""
    edad = 0
    genero = "Sin definir"

    #Constructor:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def hablar(self):
        return "La persona que se llama",self.nombre,"está hablando"
    
    def caminar(self):
        return "La persona que se llama",self.nombre,"está caminando"
    
    def getDatos(self):
        return "Nombre",self.nombre,"Apellido:",self.apellido + \
            " Edad:",self.edad," Género:",self.edad
    
p1 = Persona("Horacio","Molinari",44,"masculino")
print(p1.getDatos())

p2 = Persona("Ivan","Molinari",22,"masculino")
print(p2.getDatos())
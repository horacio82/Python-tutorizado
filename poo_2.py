#PILDORAS INFORMATICAS
#Python tutorizado. POO V, VI - Vídeo 33, 34

class Persona():
    __nombre = ""
    __apellido = ""
    __edad = 0
    __genero = "Sin definir"

    #método constructor:
    def __init__(self, nombre, apellido, genero):

        #Encapsulados:
        self.__nombre = nombre
        self.__apellido = apellido
        #self.__edad = edad
        self.__genero = genero

    def setEdad(self,laEdad):
        if laEdad<0 or laEdad>100:
            print("Error en la edad.")
        else:
            self.__edad = laEdad
            return self.__edad    

    def hablar(self):
        return "La persona que se llama",self.__nombre,"está hablando"
    
    def caminar(self):
        return "La persona que se llama",self.__nombre,"está caminando"
    
    def getDatos(self):
        return "Nombre",self.__nombre,"Apellido:",self.__apellido + \
            " Edad:",self.__edad," Género:",self.__genero
    

p1 = Persona("Horacio","Molinari","masculino")
p1.setEdad(-44)
print(p1.getDatos())


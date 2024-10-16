#PILDORAS INFORMATICAS
#Python tutorizado. POO V. Vídeo 33/34

class Persona():
    __nombre = ""
    __apellido = ""
    __edad = 0
    __genero = "Sin definir"

    def __init__(self, nombre, apellido, edad, genero):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
        self.__genero=genero

    def setEdad(self, laEdad):
        if laEdad<0 or laEdad>100:
            print("Error en la edad.")
        else:
            self.__edad=laEdad
            return self.__edad    

    def habla(self):

        return "La persona que se llama",self.__nombre,"está hablando."
    
    def camina(self):
        return "La persona que se llama",self.__nombre,"está caminando."
    
    def getDatos(self):
        return "Nombre: "+self.__nombre+" -Apellido: "+self.__apellido+" -Edad: "+str(self.__edad)+" -Género: "+self.__genero
    
p1 = Persona("Horacio","Molinari",42,"masculino")
p1.setEdad(-9)
print(p1.getDatos())

p1.nombre="Juan"
print(p1.getDatos())
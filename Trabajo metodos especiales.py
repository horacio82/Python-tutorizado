#PILDORAS INFORMATICAS
#Python tutorizado. Métodos útiles y especiales II. Vídeo 42

class Persona():

    almacen_datos=[]

    def __init__(self, *datos):
       
       for dato in datos:
           self.almacen_datos.append(dato)

       self.getDatos(self.almacen_datos)

    def getDatos(self, info):

        for dato in info:
            print(dato)

p1=Persona("Horacio","Molinari",44, 1.500, "Murata S.A.")
print(p1)         
#PILDORAS INFORMATICAS
#Python tutorizado. Métodos útiles y especiales II Y III. Vídeo 42, 43


import datetime
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

#------------------------video 43-----------------------------

hoy = datetime.date.today()
print(str(hoy))
print(repr(hoy))

#------------------------video 43---------------------------

class Agenda():

    def __init__(self):
        self.miAgenda={}

    def agregarPersonas(self, nombre, telefono):

        self.miAgenda[nombre]=telefono
    def __len__(self):
        return len(self.miAgenda)
    

agendaPersonal = Agenda()
agendaPersonal.agregarPersonas("Horacio","1133915281")
agendaPersonal.agregarPersonas("Natalia","1151791518")

print(len(agendaPersonal))

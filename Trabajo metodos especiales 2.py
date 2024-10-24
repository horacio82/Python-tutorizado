#PILDORAS INFORMÁTICAS
#Python tutorizado. Métodos útiles y especiales II. Vídeo 43

import datetime

hoy = datetime.date.today()
print(str(hoy))
print(repr(hoy))

print("---------------------------------------------------")


class Agenda():

    def __init__(self):
        self.miAgenda={}

    def agregarPersonas(self, nombre, telefono):
        self.miAgenda[nombre]=telefono

    def __len__(self):
        return len(self.miAgenda)    

agendaPersonal=Agenda()

agendaPersonal.agregarPersonas("Horacio", "1533915281")
agendaPersonal.agregarPersonas("Iván", "1125639874")

print(len(agendaPersonal))

#PILDORAS INFORMÁTICAS
#Python tutorizado. Métodos útiles y especiales II. Vídeo 43

import datetime #Importación del módulo datetime.
#Este módulo proporciona clases para manipular fechas y horas.

hoy = datetime.date.today() #Obtener fecha actual y almacena en la variable hoy.

print(str(hoy)) #Convierte la fecha a una cadena legible.

print(repr(hoy)) #Proporciona una representación más detallada y técnica de la fecha.

print("---------------------------------------------------")


class Agenda(): #Definiendo una clase.

    def __init__(self): #Constructor.
        self.miAgenda={} #Diccionario vacío para almacenar nombres y números de teléfono.

    #Este método toma un nombre y un tel y los añade al diccionario miAgenda:
    def agregarPersonas(self, nombre, telefono):
        self.miAgenda[nombre]=telefono 

    def __len__(self): #Este método devuelve el núm de entradas en miAgenda.
        return len(self.miAgenda)    

agendaPersonal=Agenda() #Se crea un objeto agendaPersonal de la clase Agenda.

#Se añaden dos entradas a la agenda con nombres y números de teléfono:
agendaPersonal.agregarPersonas("Horacio", "1533915281")
agendaPersonal.agregarPersonas("Iván", "1125639874")

#Se imprime el número de entradas en agendaPersonal, que será 2 en este caso.
print(len(agendaPersonal))

'''Así que, este código crea una agenda telefónica simple, añade un par de personas a ella 
y luego imprime la cantidad de personas en la agenda'''
#PILDORAS INFORMÁTICAS
#Python tutorizado. Métodos útiles y especiales II. Vídeo 42/43

class Persona():

   

    def __init__(self, **datos):

        elementos = datos.items()

        for clave, valor in elementos:
            print(clave,"", valor)

     

   



p1 = Persona(Nombre="Horacio", Apellido="Molinari", Edad=42)
print(p1)
      
        
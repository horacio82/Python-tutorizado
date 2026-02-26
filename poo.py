#PILDORAS INFORMATICAS
#Python tutorizado. POO III, IV Vídeo 31, 32

class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False

    #Método o comportamiento:
    def arrancar(self):
        self.arrancado = True

    def estadoCoche(self):
        if (self.arrancado):
            return "El coche está funcionando."
        else:
            return "EL coche está parado."

mazda = Coche()  #ejemplar de clase

renault = Coche()

print("Tu coche tiene",mazda.ruedas,"ruedas.")

#LLamando al método:
renault.arrancar()

print(mazda.estadoCoche())
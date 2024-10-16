#PILDORAS INFORMÁTICAS  
#Python tutorizado. POO III. Vídeo 31/32

class Coche():
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False

    def arrancar(self):
        self.arrancado=True

    def estadoCoche(self):
        if(self.arrancado==True):
            return "El coche está funcionando."
        else:
            return "El coche está parado"    

mazda = Coche()    #Ejemplar de clase
renault = Coche()

print("Tu coche tiene",mazda.ruedas,"ruedas")

renault.arrancar()

print(renault.estadoCoche())
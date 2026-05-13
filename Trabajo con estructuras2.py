#PILDORAS INFORMATICAS
#Python tutorizado. Estructuras de datos II. Vídeo 59

'''En este vídeo vemos las Queue (colas). Muy utilizadas en programación concurrente (multitarea) en Python. Abordaremos la multitarea más adelante.'''

import queue

miCola = queue.Queue(4)

miCola.put("Madrid")
miCola.put("Bogotá")
miCola.put("Mexico D.F.")
miCola.put("Lima")

while miCola.full():
    print(miCola.get())





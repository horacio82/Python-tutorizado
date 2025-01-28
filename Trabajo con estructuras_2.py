#PILDORAS INFORMÁTICAS - Python tutorizado. Estructuras de datos II. Vídeo 59

import queue #Módulo para trabajar con colas de prioridad

miCola = queue.PriorityQueue() #Cola de prioridad
#miCola = queue.Queue(4) #Cola normal

miCola.put((1,"Buenos Aires")) #Se añaden elementos a la cola de prioridad
miCola.put((2,"Córdoba"))
miCola.put((3,"Mendoza"))

print(miCola.get()) #Se extrae el elemento con mayor prioridad

print("A continuación se imprimen los elementos restantes en la cola")

for elemento in miCola.queue: #Se imprimen los elementos restantes en la cola
    print(elemento) #Se imprimen los elementos restantes en la cola
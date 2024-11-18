#PILDORAS INFORMÁTICAS - Python tutorizado. Estructuras de datos I. Vídeo 58

sistema_solar = "Mercurio Venus Tierra Marte Júpiter Saturno Urano Neptuno Urano Neptuno Plutón"

'''creando un conjunto vacío llamado planetas. Los conjuntos en Python son colecciones
desordenadas de elementos únicos, es decir, no permiten duplicados.'''
planetas = set()

'''Aquí estamos usando un bucle for para iterar sobre los nombres de los planetas. 
La función split(" ") divide la cadena sistema_solar en una lista de palabras, usando el espacio como separador. 
En cada iteración, agregamos el nombre del planeta al conjunto planetas usando el método add().'''
for planeta in sistema_solar.split(" "):
    planetas.add(planeta)

#Esta línea imprime el conjunto planetas, que contendrá todos los planetas, pero sin duplicados.
print(planetas)  

#Finalmente, esta línea imprime la cantidad de elementos únicos en el conjunto planetas usando la función len().
print(len(planetas))

'''Entonces, el código completo se encarga de eliminar los planetas duplicados
y contar cuántos planetas únicos hay en la lista original.'''
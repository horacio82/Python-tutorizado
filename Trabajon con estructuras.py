#PILDORAS INFORMATICAS
#Python tutorizado. Estructuras de datos I. Vídeo 58
# Un set es una colección de elementos únicos, sin orden específico. No permite elementos duplicados y no mantiene un orden fijo. Es útil para almacenar elementos únicos y realizar operaciones de conjunto como unión, intersección y diferencia.


sistema_solar = "Mercurio Venus Tierra Marte Júpiter Saturno Urano Neptuno Tierra Mercurio"

planetas=set()

for planeta in sistema_solar.split(" "):
    planetas.add(planeta)

print(planetas)    
print(len(planetas))
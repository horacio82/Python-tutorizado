#PILDORAS INFORMÁTICAS - Python tutorizado. Estructuras de datos I. Vídeo 58

sistema_solar = "Mercurio Venus Tierra Marte Júpiter Saturno Urano Neptuno Urano Neptuno Plutón"

planetas = set()

for planeta in sistema_solar.split(" "):
    planetas.add(planeta)

print(planetas)    
print(len(planetas))
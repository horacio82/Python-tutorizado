#Pildoras informáticas
#Python tutorizado. Bucles y diccionarios. Vídeo 22

capitales = {"China":"Pekin","India":"Nueva Delhi","Indonesia":"Yakarta","Japón":"Tokio","Bangladesh":"Dacca"}

for clave,valor in capitales.items():
    print(clave,"->",valor)   

    '''Este código define un diccionario llamado capitales que asocia países con sus capitales. 
    Luego, usa un bucle for para recorrer cada par clave-valor del diccionario. Dentro del bucle, 
    imprime cada país junto a su capital en el formato país -> capital.
    '''
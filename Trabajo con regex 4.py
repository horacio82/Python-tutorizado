#PILDORAS INFORMÁTICAS
#Python tutorizado. Expresiones regulares IV. Vídeo 88

import re

nombre1 = "Carmen López"
nombre2 = "Juan Díaz"
nombre3 = "Sandra Martín"
nombre4 = "Lara Gómez"
nombre5 = "Jara López"

codigo1 = "dsashkskdha255skjdajskhd"
codigo2 = "dsashkskdha133skjdajskhd"
codigo3 = "dsashkskdha255skjdajskhd"


#Bucle que recorre la lista de nombres y busca aquellos que comienzan con "Sandra"
if re.match("Sandra", nombre1,re.IGNORECASE):
    print("He encontrado a la persona")
else:
    print("No he encontrado a la persona")    

print("---------------------------------------------------")

if re.match(".ara", nombre4,re.IGNORECASE) or re.match(".ara", nombre5,re.IGNORECASE):    
    print("He encontrado a la persona")
else:
    print("No he encontrado a la persona")    

print("---------------------------------------------------")

if re.search("López", nombre1,re.IGNORECASE):    
    print("He encontrado a la persona")    
else:
    print("No he encontrado a la persona")    

print("---------------------------------------------------")

if re.search("255", codigo2,re.IGNORECASE):
    print("He encontrado el código")    
else:
    print("No he encontrado el código")    
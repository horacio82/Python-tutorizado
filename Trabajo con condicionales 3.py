#Pildoras informaticas (video 17) operadores IN y NOT

trabajadores = ["Paula", "Manuel", "Pedro", "Ana", "Sandra"]

#Busca la palabra Pedro en la lista:
if "Pedro" in trabajadores:
    print("Sí, Pedro está en la lista.")
else:
    print("Pedro no está en la lista.")    

#------------------------------------------------------------

lenguajes_Trim1 ="Java, Python, PHP, C#, HTML, JavaScript"

#Busca la palabra PHP en la cadena de texto:
if "PHP" in lenguajes_Trim1:
    print("PHP está.")
else:
    print("PHP no está.")    

#------------------------------------------------------------

#Si la palabra SQL no está en la cadena de texto:
if "SQL" not in lenguajes_Trim1:
    print("Falta SQL en la lista.")
else:
    print("SQL está en la lista.")


#Tambien se puede hacer de esta forma:
if not "SQL" in lenguajes_Trim1:
    print("Falta SQL en la lista.")
else:
    print("SQL está en la lista.")
#PILDORAS INFORMATICAS
#Python tutorizado. Expresiones regulares II, III, IV . Vídeo 86, 87, 88

import re

lista_nombres=['Sandra Gomez','Maria Martin','Sandra Lopez', 'Ana Martin', 'Sandra Fernandez']

for nombre in lista_nombres:
    if re.findall('^Sandra',nombre): #^ indica que empieza por Sandra
        print(nombre)

print('---------------------------------------------')

for nombre in lista_nombres:
    if re.findall('Martin$',nombre): #$ indica que termina por Martin
        print(nombre)        

print('---------------------------------------------')

lista_paginas = ['http://www.pildorasinformaticas.es', 'ftp://www.pildorasinformaticas.es', 'http://www.pildorasinformaticas.com', 'ftp://www.pildorasinformaticas.com']

for pagina in lista_paginas:
    if re.findall('.es$',pagina): #Busca las que terminan por .es
        print(pagina)


print('---------------------------------------------')

lista_terminos = ['camion','camión','niños','niñas','ejemplo']

for termino in lista_terminos:
    if re.findall('cami[oó]n',termino): #Busca camion o camión
        print(termino)

print('---------------------------------------------')

for termino in lista_terminos:
    if re.findall('[p-z]',termino): #Busca palabras que contengan letras entre p y z
        print(termino)        

print('---------------------------------------------')

for termino in lista_terminos:
    if re.findall("^[a-f]",termino): #Busca palabras que empiecen por letras entre a y f
        print(termino)

print('---------------------------------------------')

for termino in lista_terminos:
    if re.findall("[l-p]$",termino): #Busca palabras que contengan letras entre l y p o terminen por p
        print(termino)

print('---------------------------------------------')

lista_codigos = ['Ma:1','Se1','Ma2','Ba1','Ma.3','Va1','Va2','Ma4','MaA','Ma5','MaB','MaC']   

for codigo in lista_codigos:
    if re.findall('Ma[0-3]',codigo): #Busca Ma0, Ma1, Ma2 o Ma3
        print(codigo)

print('---------------------------------------------')

for codigo in lista_codigos:
    if re.findall('Ma[^1-3]',codigo): #Busca Ma que no contenga 1, 2 o 3
        print(codigo)

print('---------------------------------------------')

for codigo in lista_codigos:
    if re.findall('Ma[0-3A-B]',codigo): #Busca Ma0, Ma1, Ma2, Ma3, MaA o MaB
        print(codigo)

print('---------------------------------------------')

for codigo in lista_codigos:
    if re.findall('Ma[.:]',codigo): #Busca Ma. o Ma:
        print(codigo)

print('---------------------------------------------')

nombre = 'Jara Lopez'
nombre2 = 'Antonio Gomez'
nombre3 = 'Lara Lopez'

if re.match('.ara',nombre, re.IGNORECASE): #Busca palabras que empiecen por cualquier letra y terminen por ara
    print("He encontrado a la persona",nombre)
else:
    print("No he encontrado a la persona",nombre)    

print('---------------------------------------------')

codigo1 = 'Ma1'
codigo2 = 'Se1'
codigo3 = 'Ma2'

if re.search('Ma1',codigo1): #Busca Ma1
    print("He encontrado el código",codigo1)
else:
    print("No he encontrado el código",codigo1)    
#PILDORAS INFORMATICAS
#Python tutorizado. Expresiones regulares II, III. Vídeo 86, 87

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
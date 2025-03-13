#PILDORAS INFORMATICAS
#Python tutorizado. Expresiones regulares II. Vídeo 86

import re

lista_nombres=['Sandra Gomez','Maria Martin','Sandra Lopez', 'Ana Martin', 'Sandra Fernandez']

for nombre in lista_nombres:
    if re.findall('^Sandra',nombre): #^ indica que empieza por Sandra
        print(nombre)

#------------------------------------------------------

for nombre in lista_nombres:
    if re.findall('Martin$',nombre): #$ indica que termina por Martin
        print(nombre)        

#------------------------------------------------------

lista_paginas = ['http://www.pildorasinformaticas.es', 'ftp://www.pildorasinformaticas.es', 'http://www.pildorasinformaticas.com', 'ftp://www.pildorasinformaticas.com']

for pagina in lista_paginas:
    if re.findall('.es$',pagina): #Busca las que terminan por .es
        print(pagina)


#------------------------------------------------------

lista_terminos = ['camion','camión','niños','niñas','ejemplo']

for termino in lista_terminos:
    if re.findall('cami[oó]n',termino): #Busca camion o camión
        print(termino)
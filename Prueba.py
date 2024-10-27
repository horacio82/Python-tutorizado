#PILDORAS INFORMÁTICAS - Python tutorizado. Ejemplo de uso módulos. Vídeo 48

import csv
with open('Ejemplo.csv', newline='') as csvfile:
    miCsv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in miCsv:
        print('- '.join(row))
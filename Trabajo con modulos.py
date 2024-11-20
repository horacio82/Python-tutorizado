#PILDORAS INFORMÁTICAS
#Python tutorizado. Módulos II. Vídeo 45
#Python tutorizado. Paquetes I. Vídeo 46

#import Funciones_matematicas

#Importación de módulos y funciones
from moduloMatematico.calculosBasicos.Funciones_matematicas import *
from moduloMatematico.otrosCalculos.PotenciaYredondeo import *
'''Estas líneas importan todas las funciones definidas en los módulos Funciones_matematicas y PotenciaYredondeo, 
ubicados en los directorios calculosBasicos y otrosCalculos respectivamente. La sintaxis import * indica que todas las 
funciones disponibles en esos módulos serán importadas.'''

#Uso de las funciones importadas:
sumar(20,15)
restar(20,10)
multiplicar(8,6)
potencia(5,3)
redondear(2.78)

'''Para que este código funcione correctamente, necesitas tener definidos y disponibles esos módulos (moduloMatematico.calculosBasicos.Funciones_matematicas y moduloMatematico.otrosCalculos.PotenciaYredondeo) en tu entorno de Python.'''
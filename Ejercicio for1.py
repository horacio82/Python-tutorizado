#Pildoras informáticas 
'''
Crea un programa de Python que pida 2 números por consola. El programa debe imprimir todos
los números primos comprendidos entre los 2 números introducidos por consola.
Los números primos son aquellos que solo son divisibles por 1 y por ellos mismos.
Por ejemplo, si introducimos como primer número el 1 y como segundo número el 10, el
programa imprimirá en consola todos los números primos comprendidos entre 1 y 10, esto es:
1
2
3
5
7
Si por el contrario, introducimos como primer número el 10 y como segundo número el 20, el
programa imprimirá en consola todos los números primos comprendidos entre 10 y 20, esto es:
11
13
17
19
Solución en la siguiente página

'''

# Solicita dos números enteros al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Define la función que verifica si un número es primo
def es_primo(numero):
    # Recorre los números desde 2 hasta uno menos del número dado
    for i in range(max(num1, 2), num2 + 1):
        if es_primo(i):
            print(str(i), "es primo")
            return False
    # Si no encuentra ningún divisor, el número es primo
    print(str(numero), "es primo")
    return True

# Recorre los números entre num1 y num2
for i in range(num1, num2):
    es_primo(i)       
import numpy as np

# Crear dos matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Sumar las matrices
matrix_sum = np.add(matrix_a, matrix_b)

# Multiplicar las matrices elemento por elemento (producto Hadamard)
matrix_product = np.multiply(matrix_a, matrix_b)

# Multiplicar las matrices (producto de matriz)
matrix_dot_product = np.dot(matrix_a, matrix_b)

# Imprimir resultados
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Suma de las matrices:\n", matrix_sum)
print("Producto Hadamard de las matrices:\n", matrix_product)
print("Producto de matriz de las matrices:\n", matrix_dot_product)
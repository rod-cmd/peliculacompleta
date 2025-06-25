# 1. Crear la matriz de 3x3 llamada "teclado"
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)

# 3. Mostrar valores específicos usando índices
print("\nNúmero en el centro:", teclado[1][1])            # El 5
print("Número en la esquina inferior derecha:", teclado[2][2])  # El 9

# 4. Modificar el número en la esquina superior izquierda
teclado[0][0] = 0

# 5. Imprimir la matriz de nuevo para ver el cambio
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)
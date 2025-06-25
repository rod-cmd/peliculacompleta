# Matriz teclado
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Inicialización
num_filas = len(teclado)
num_columnas = len(teclado[0])
sumas_por_columna = [0] * num_columnas  # Lista con 3 ceros: [0, 0, 0]

# 2. Iteración anidada con índices
for i in range(num_filas):
    for j in range(num_columnas):
        # 3. Acumulación por índice
        sumas_por_columna[j] += teclado[i][j]

# 4. Resultado final
print("Suma de cada columna:", sumas_por_columna)
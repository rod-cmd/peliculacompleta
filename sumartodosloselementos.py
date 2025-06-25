# Matriz teclado
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Inicialización
acumulador_total = 0

# 2. Iteración anidada
for fila in teclado:
    for elemento in fila:
        # 4. Acumulación
        acumulador_total += elemento

# 5. Resultado
print("La suma total de los elementos es:", acumulador_total)
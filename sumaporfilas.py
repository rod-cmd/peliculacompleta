# Matriz teclado
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Inicialización
sumas_por_fila = []

# 2. Iteración exterior (por fila)
for fila in teclado:
    # 3a. Inicializar acumulador para la fila
    acumulador_fila = 0
    
    # 3b. Iteración interior (por elemento en la fila)
    for elemento in fila:
        # 3c. Sumar al acumulador
        acumulador_fila += elemento
    
    # 4. Guardar resultado de la fila
    sumas_por_fila.append(acumulador_fila)

# 5. Resultado final
print("Suma de cada fila:", sumas_por_fila)
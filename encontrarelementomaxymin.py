# Matriz teclado
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Suposición inicial (manejo de matriz vacía)
if len(teclado) == 0 or len(teclado[0]) == 0:
    print("La matriz está vacía.")
else:
    maximo = teclado[0][0]
    minimo = teclado[0][0]

    # 2. Iteración anidada
    for fila in teclado:
        for elemento in fila:
            # 3. Comparación y actualización
            if elemento > maximo:
                maximo = elemento
            if elemento < minimo:
                minimo = elemento

    # 4. Resultado
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
# Matriz teclado ya modificada
teclado = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer la matriz e imprimirla como cuadrícula
print("Teclado como cuadrícula:")
for fila in teclado:
    for elemento in fila:
        print(elemento, end="\t")  # Imprime con tabulación en la misma línea
    print()  # Salto de línea al terminar cada fila
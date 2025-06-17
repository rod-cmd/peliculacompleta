
def encontrar_maximo(ingresa_los_numeros):
    if len(ingresa_los_numeros) == 0:
        return None  # Mejor explicito

    maximo = ingresa_los_numeros[0]
    for numero in ingresa_los_numeros:
        if numero > maximo:
            maximo = numero
    return maximo  # Fuera del bucle

print("\nProbando encontrar_maximo")
assert encontrar_maximo([1, 9, 2, 8, 3, 7]) == 9
print("Prueba 1 pasada = 9")
assert encontrar_maximo([-1, -9, -2, -8]) == -1
print("Prueba 2 pasada = -1")
assert encontrar_maximo([42, 42, 42]) == 42
print("Prueba 3 pasada = 42")

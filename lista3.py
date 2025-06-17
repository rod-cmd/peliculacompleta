
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero
    return acumulador_suma

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
resultado = sumar_elementos(mi_lista)

print (f"La suma de los elementos de la lista es: {resultado}")

print("(-Con assert-)")

def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero
    return acumulador_suma
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
print("Prueba 1 pasada = 15")
assert sumar_elementos([10, 20, 30, 40, 50]) == 150
print("Prueba 2 pasada = 150")
assert sumar_elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 70
print("Prueba 3 pasada = 70")
assert sumar_elementos([10, -2, 5]) == 13
print("Prueba 4 pasada = 13")
assert sumar_elementos([]) == 0
print("Prueba 5 pasada = 0")
assert sumar_elementos([100]) == 100
print("Prueba 6 pasada = 100")
print (" Todas las pruebas pasaron.")




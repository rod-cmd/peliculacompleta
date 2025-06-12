cantidad_notas = int (input("¿cuantas notas vas a ingresar? "))
suma = 0
for i in range(cantidad_notas):
    nota = float (input(f"ingrese la nota # {i + 1}: "))
    suma += nota
    promedio = suma / cantidad_notas
    print(f"\nSuma total de notas: {suma}")
    print(f"Promedio: {promedio}")

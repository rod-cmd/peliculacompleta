num_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"--- Tabla del {num_tabla} ---")
for i in range(1, 11):
    resultado = num_tabla * i # i tomará valores de 1 a 10     resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")

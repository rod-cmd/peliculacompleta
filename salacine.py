# 1. Crear la sala
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

# 2. Mostrar la sala de forma visual
def mostrar_sala(sala):
    print("\nSala de Cine (L = Libre, O = Ocupado):\n")
    print("   " + " ".join(f"{i}" for i in range(len(sala[0]))))  # Encabezado de columnas
    for idx, fila in enumerate(sala):
        print(f"{idx:2} " + " ".join(fila))
    print()

# 3. Ocupar un asiento
def ocupar_asiento(sala, fila, columna):
    if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]):
        if sala[fila][columna] == 'L':
            sala[fila][columna] = 'O'
            return True
        else:
            print("⛔ Ese asiento ya está ocupado.")
            return False
    else:
        print("❌ Coordenadas fuera de rango.")
        return False

# 4. Contar asientos libres
def contar_asientos_libres(sala):
    return sum(fila.count('L') for fila in sala)

# Programa principal
def main():
    filas = 5
    columnas = 8
    sala = crear_sala(filas, columnas)

    while True:
        mostrar_sala(sala)
        print(f"Asientos libres: {contar_asientos_libres(sala)}")
        print("\nMENÚ:")
        print("1. Ocupar asiento")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                fila = int(input("Ingresa número de fila: "))
                columna = int(input("Ingresa número de columna: "))
                exito = ocupar_asiento(sala, fila, columna)
                if exito:
                    print("✅ Asiento reservado con éxito.")
            except ValueError:
                print("⚠️ Por favor, ingresa números válidos.")
        elif opcion == '0':
            print("¡Gracias por usar el sistema de cine!")
            break
        else:
            print("❗ Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
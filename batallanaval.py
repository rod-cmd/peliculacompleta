import json
import random
import os

# Constantes
TAM = 5
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_PARTIDAS = "partidas_guardadas.json"

# ---------- UTILIDADES ----------

def crear_tablero():
    return [['~' for _ in range(TAM)] for _ in range(TAM)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(map(str, range(TAM))))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join('~' if ocultar_barcos and c == 'B' else c for c in fila))

def posicion_aleatoria():
    return random.randint(0, TAM - 1), random.randint(0, TAM - 1)

def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, 'r') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f)

def cargar_partidas():
    if os.path.exists(ARCHIVO_PARTIDAS):
        with open(ARCHIVO_PARTIDAS, 'r') as f:
            return json.load(f)
    return {}

def guardar_partidas(partidas):
    with open(ARCHIVO_PARTIDAS, 'w') as f:
        json.dump(partidas, f)

# ---------- JUEGO ----------

def registrar_usuario():
    usuarios = cargar_usuarios()
    username = input("Nombre de usuario: ")
    if username in usuarios:
        print("⚠️ Usuario ya registrado.")
    else:
        password = input("Contraseña: ")
        usuarios[username] = password
        guardar_usuarios(usuarios)
        print("✅ Usuario registrado.")
    return username

def iniciar_sesion():
    usuarios = cargar_usuarios()
    username = input("Nombre de usuario: ")
    if username in usuarios:
        password = input("Contraseña: ")
        if password == usuarios[username]:
            print("✅ Sesión iniciada.")
            return username
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")
    return None

def colocar_barco(tablero):
    while True:
        fila, col = posicion_aleatoria()
        if tablero[fila][col] == '~':
            tablero[fila][col] = 'B'
            break

def disparar(tablero, visible, fila, col):
    if tablero[fila][col] == 'B':
        visible[fila][col] = 'X'
        print("🎯 ¡Tocado!")
        return True
    elif visible[fila][col] == '~':
        visible[fila][col] = 'O'
        print("💧 Agua.")
        return False
    else:
        print("⚠️ Ya disparaste aquí.")
        return False

def partida_terminada(tablero_visible):
    for fila in tablero_visible:
        if 'X' in fila:
            return True
    return False

def jugar_turno(jugador, tablero_enemigo, visible_enemigo, is_cpu=False):
    print(f"\nTurno de {jugador}")
    mostrar_tablero(visible_enemigo, ocultar_barcos=False if is_cpu else True)
    if is_cpu:
        fila, col = posicion_aleatoria()
    else:
        try:
            fila = int(input("Fila: "))
            col = int(input("Columna: "))
        except:
            print("❌ Entrada inválida.")
            return False
    if 0 <= fila < TAM and 0 <= col < TAM:
        return disparar(tablero_enemigo, visible_enemigo, fila, col)
    else:
        print("❌ Coordenadas fuera de rango.")
        return False

# ---------- JUGAR Y GUARDAR ----------

def guardar_estado_partida(usuario, datos_partida):
    partidas = cargar_partidas()
    partidas[usuario] = datos_partida
    guardar_partidas(partidas)
    print("💾 Partida guardada.")

def jugar(usuario, contra_cpu=True, cargada=None):
    if cargada:
        datos = cargada
    else:
        datos = {
            "turno": 1,
            "jugador1_tablero": crear_tablero(),
            "jugador1_visible": crear_tablero(),
            "jugador2_tablero": crear_tablero(),
            "jugador2_visible": crear_tablero(),
            "contra_cpu": contra_cpu
        }
        colocar_barco(datos["jugador1_tablero"])
        colocar_barco(datos["jugador2_tablero"])

    while True:
        print("\n" + "-"*30)
        print(f"🎮 TURNO {datos['turno']} (Escribe 'guardar' para guardar y salir)")

        # Turno jugador
        mostrar_tablero(datos["jugador2_visible"], ocultar_barcos=True)
        entrada = input("Fila (o 'guardar'): ")
        if entrada.lower() == "guardar":
            guardar_estado_partida(usuario, datos)
            break
        try:
            fila = int(entrada)
            col = int(input("Columna: "))
        except:
            print("❌ Entrada inválida.")
            continue
        if 0 <= fila < TAM and 0 <= col < TAM:
            disparar(datos["jugador2_tablero"], datos["jugador2_visible"], fila, col)
            if partida_terminada(datos["jugador2_visible"]):
                print(f"\n🏆 {usuario} ganó la partida!")
                break
        else:
            print("❌ Coordenadas fuera de rango.")
            continue

        # Turno CPU o jugador 2
        if datos["contra_cpu"]:
            fila, col = posicion_aleatoria()
            print(f"\n💻 CPU dispara a ({fila}, {col})")
            disparar(datos["jugador1_tablero"], datos["jugador1_visible"], fila, col)
            if partida_terminada(datos["jugador1_visible"]):
                print("\n💻 La CPU ganó la partida!")
                break
        else:
            mostrar_tablero(datos["jugador1_visible"], ocultar_barcos=True)
            print("Turno Jugador 2")
            try:
                fila = int(input("Fila: "))
                col = int(input("Columna: "))
            except:
                print("❌ Entrada inválida.")
                continue
            if 0 <= fila < TAM and 0 <= col < TAM:
                disparar(datos["jugador1_tablero"], datos["jugador1_visible"], fila, col)
                if partida_terminada(datos["jugador1_visible"]):
                    print("\n🏆 Jugador 2 ganó la partida!")
                    break
            else:
                print("❌ Coordenadas fuera de rango.")
                continue

        datos["turno"] += 1

# ---------- MENÚ ----------

def main():
    print("=== 🚢 Batalla Naval 5x5 ===")
    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("0. Salir")
        op = input("Opción: ")
        if op == '1':
            registrar_usuario()
        elif op == '2':
            usuario = iniciar_sesion()
            if usuario:
                while True:
                    print("\n1. Nueva partida vs CPU")
                    print("2. Nueva partida vs Jugador 2")
                    print("3. Continuar partida guardada")
                    print("0. Cerrar sesión")
                    op2 = input("Elige opción: ")
                    if op2 == '1':
                        jugar(usuario, contra_cpu=True)
                    elif op2 == '2':
                        jugar(usuario, contra_cpu=False)
                    elif op2 == '3':
                        partidas = cargar_partidas()
                        if usuario in partidas:
                            jugar(usuario, cargada=partidas[usuario])
                        else:
                            print("⚠️ No hay partida guardada.")
                    elif op2 == '0':
                        break
                    else:
                        print("❌ Opción inválida.")
        elif op == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
    



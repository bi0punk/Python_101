import random


def jugar():
    POSICIONES = 6
    posiciones = [0] * POSICIONES
    bala = random.randint(0, POSICIONES - 1)
    posiciones[bala] = 1

    print("=== RULETA RUSA ===")
    print(f"Tienes {POSICIONES} intentos. ¡Suerte!")

    for intento in range(1, POSICIONES + 1):
        try:
            eleccion = int(input(f"Intento {intento}/{POSICIONES} - Elige posición (0-5): "))
        except ValueError:
            print("Número inválido")
            continue
        if eleccion < 0 or eleccion >= POSICIONES:
            print(f"Elige entre 0 y {POSICIONES - 1}")
            continue
        if posiciones[eleccion] == 1:
            print("¡BANG! Has perdido.")
            return
        print("Sigues vivo.")
    print("¡Ganaste! Sobreviviste a todos los intentos.")


if __name__ == "__main__":
    jugar()

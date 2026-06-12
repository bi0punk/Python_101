from tqdm import tqdm
import random


def obtener_color():
    print("Ingrese colores para apostar")
    print("1) Rojo")
    print("2) Negro")
    while True:
        try:
            col_apuesta = int(input())
            if col_apuesta == 1:
                return 'Rojo'
            elif col_apuesta == 2:
                return 'Negro'
            else:
                print("Ingrese una opción válida")
        except ValueError:
            print("Ingrese una opción válida")


def obtener_numero():
    while True:
        try:
            num_rul_jug = int(input("Ingrese un número entre 0 y 36: "))
            if num_rul_jug >= 0 and num_rul_jug <= 36:
                return num_rul_jug
            else:
                print("Ingrese un número dentro del rango")
        except ValueError:
            print("Ingrese un número válido")


def lanzar_ruleta(veces_a_lanzar):
    lista = []
    lista_choice = []

    for _ in tqdm(range(veces_a_lanzar)):
        nr = random.randint(0, 36)
        cr = random.choice(["Rojo", "Negro"])
        lista.append(nr)
        lista_choice.append(cr)

    return lista, lista_choice


def resumen_apuesta(mon_apuesta, color, num_rul_jug):
    print("Resumen Apuesta")
    print("Monto:", mon_apuesta)
    print("Color:", color)
    print("Número:", num_rul_jug)


def resultado_ruleta(nr, cr):
    print("Resultado Ruleta")
    print("Color:", cr)
    print("Número:", nr)


def calcular_ganancia(mon_apuesta, nr, color, cr, num_rul_jug):
    if nr != num_rul_jug and color == cr:
        ganancia = mon_apuesta * 0.2
        print("Usted ha ganado:", ganancia)
    elif nr == num_rul_jug and color != cr:
        ganancia = mon_apuesta * 2
        print("Usted ha ganado:", ganancia)
    elif nr == num_rul_jug and color == cr:
        ganancia = mon_apuesta * 4
        print("Usted ha ganado:", ganancia)
    else:
        print("Mala suerte, no ganó nada")


if __name__ == "__main__":
    print("#####################")
    print("# RULETA MONTECARLO #")
    print("#####################")

    try:
        mon_apuesta = int(input("Ingrese el monto a apostar: "))
    except ValueError:
        print("Monto inválido")
        exit(1)

    color = obtener_color()
    num_rul_jug = obtener_numero()

    resumen_apuesta(mon_apuesta, color, num_rul_jug)

    op_rul = input("Presione Enter para lanzar Ruleta: ")

    if op_rul == "":
        try:
            veces_a_lanzar = int(input("Veces a lanzar: "))
        except ValueError:
            print("Número inválido")
            exit(1)

        numeros, colores = lanzar_ruleta(veces_a_lanzar)
        for nr, cr in zip(numeros, colores):
            resultado_ruleta(nr, cr)
            calcular_ganancia(mon_apuesta, nr, color, cr, num_rul_jug)

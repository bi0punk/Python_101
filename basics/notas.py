def ingresar_notas():
    notas = []
    print("Ingrese las notas una por una (Enter sin valor para terminar):")
    while True:
        entrada = input(f"Nota {len(notas) + 1}: ").strip()
        if entrada == "":
            break
        try:
            nota = float(entrada)
            if nota < 1.0 or nota > 7.0:
                print("Nota fuera de rango (1.0 - 7.0)")
            else:
                notas.append(nota)
        except ValueError:
            print("Nota inválida")
    return notas


def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)


if __name__ == "__main__":
    print("=== CALCULADORA DE PROMEDIO ===")
    notas = ingresar_notas()
    if notas:
        prom = calcular_promedio(notas)
        print(f"\nNotas: {notas}")
        print(f"Promedio: {prom:.2f}")
        if prom >= 4.0:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")
    else:
        print("No se ingresaron notas")

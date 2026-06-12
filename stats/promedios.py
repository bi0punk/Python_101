def calcular_promedio():
    notas = []
    print("Ingrese notas (presione Enter sin valor para terminar):")
    while True:
        entrada = input("Nota: ").strip()
        if entrada == "":
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Nota inválida, intente de nuevo")
    if not notas:
        print("No se ingresaron notas")
        return
    promedio = sum(notas) / len(notas)
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")


if __name__ == "__main__":
    calcular_promedio()

def fibonacci_iterativo(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


if __name__ == "__main__":
    try:
        n = int(input("Cantidad de términos Fibonacci: "))
        print(f"Serie: {fibonacci_iterativo(n)}")
        print(f"Término {n} (recursivo): {fibonacci_recursivo(n)}")
    except ValueError:
        print("Número inválido")

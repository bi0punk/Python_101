import numpy as np


def es_cuadrada(matriz):
    return len(matriz[0]) == len(matriz)


def tipo_simetria(matriz):
    if not es_cuadrada(matriz):
        return None
    es_simetrica = True
    es_antisimetrica = True
    for x in range(len(matriz)):
        for y in range(x, len(matriz)):
            if matriz[x][y] != matriz[y][x]:
                es_simetrica = False
            if matriz[x][y] != -(matriz[y][x]):
                es_antisimetrica = False
    if es_antisimetrica:
        return "antisimétrica"
    if es_simetrica:
        return "simétrica"
    return "ninguno"


a = np.array([[1, 2, 3, 4, 5], [1, -1, 1, -1, 1], [3, 3, 3, 3, 3], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]])
b = np.array([[1, 2, 3, 4, 5], [2, 1, 2, 1, 2], [3, 2, 3, 2, 3], [4, 1, 2, 1, 4], [5, 2, 3, 4, 2]])
c = np.array([[0, 2, 3, 4, 5], [-2, 0, 2, 1, 2], [-3, -2, 0, 2, 3], [-4, -1, -2, 0, 4], [-5, -2, -3, -4, 0]])

for nombre, m in [("a", a), ("b", b), ("c", c)]:
    if es_cuadrada(m):
        print(f"La matriz {nombre} es {tipo_simetria(m)}")
    else:
        print(f"La matriz {nombre} no es cuadrada")

rut = "12345678-9"
ultimos_3_digitos = rut[-3:]
matriz_rut = np.array([
    [int(d) * 2 for d in ultimos_3_digitos],
    [int(d) * 3 for d in ultimos_3_digitos],
    [int(d) * 4 for d in ultimos_3_digitos]
])
print(f"\nMatriz desde últimos 3 dígitos del RUT {rut}:")
print(matriz_rut)

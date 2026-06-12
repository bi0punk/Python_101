import sys
import re
from itertools import cycle


def validar_rut(rut):
    rut = re.sub("[^0-9kK]", "", rut)
    if len(rut) < 2:
        return False
    aux = rut[:-1]
    dv = rut[-1].upper()
    factores = cycle([2, 3, 4, 5, 6, 7])
    s = sum(int(d) * next(factores) for d in reversed(aux))
    res = (11 - (s % 11)) % 11
    dv_calculado = str(res) if res < 10 else "K"
    return dv_calculado == dv


def main():
    if len(sys.argv) < 2:
        print("Uso: python valida_rut.py <rut>")
        print("Ejemplo: python valida_rut.py 12345678-9")
        return
    if validar_rut(sys.argv[1]):
        print("RUT válido")
    else:
        print("RUT inválido")


if __name__ == "__main__":
    main()

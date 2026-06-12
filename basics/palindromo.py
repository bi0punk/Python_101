import re


def es_palindromo(texto):
    limpio = re.sub(r"[^a-zA-Z0-9]", "", texto).lower()
    return limpio == limpio[::-1]


if __name__ == "__main__":
    texto = input("Ingrese una palabra o frase: ")
    if es_palindromo(texto):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

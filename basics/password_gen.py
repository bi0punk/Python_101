import random
import string


def generar_password(longitud=12, mayus=True, minus=True, digitos=True, simbolos=True):
    chars = ""
    if minus:
        chars += string.ascii_lowercase
    if mayus:
        chars += string.ascii_uppercase
    if digitos:
        chars += string.digits
    if simbolos:
        chars += string.punctuation
    if not chars:
        return "Error: selecciona al menos un tipo de carácter"
    return "".join(random.choice(chars) for _ in range(longitud))


if __name__ == "__main__":
    try:
        largos = {
            8: "Débil",
            12: "Media",
            16: "Fuerte",
            24: "Muy fuerte",
        }
        while True:
            try:
                n = int(input("Largo de la contraseña (0 para salir): "))
                if n == 0:
                    break
                pw = generar_password(longitud=n)
                nivel = "Personalizada"
                for k in sorted(largos):
                    if n >= k:
                        nivel = largos[k]
                print(f"Contraseña ({nivel}): {pw}")
            except ValueError:
                print("Número inválido")
    except KeyboardInterrupt:
        print("\nAdiós")

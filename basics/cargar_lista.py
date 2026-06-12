def cargar_alumnos():
    nombres = []
    print("Ingrese nombres de alumnos (escriba 'stop' para terminar):")
    while True:
        nombre = input("> ").strip()
        if not nombre:
            continue
        if nombre.lower() == "stop":
            break
        nombres.append(nombre)
    return nombres

if __name__ == "__main__":
    alumnos = cargar_alumnos()
    print(f"\nAlumnos registrados: {len(alumnos)}")
    for i, a in enumerate(alumnos, 1):
        print(f"  {i}. {a}")

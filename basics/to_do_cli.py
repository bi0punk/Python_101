import json
import os

TASKS_FILE = "tareas.json"


def cargar():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def guardar(tareas):
    with open(TASKS_FILE, "w") as f:
        json.dump(tareas, f, indent=2)


def mostrar(tareas):
    if not tareas:
        print("  No hay tareas")
        return
    for i, t in enumerate(tareas, 1):
        estado = "[x]" if t.get("done") else "[ ]"
        print(f"  {i}. {estado} {t['texto']}")


def agregar(tareas, texto):
    tareas.append({"texto": texto, "done": False})
    guardar(tareas)
    print(f"  Tarea agregada: {texto}")


def completar(tareas, idx):
    if 0 <= idx < len(tareas):
        tareas[idx]["done"] = True
        guardar(tareas)
        print(f"  Tarea {idx + 1} completada")
    else:
        print("  Índice inválido")


def eliminar(tareas, idx):
    if 0 <= idx < len(tareas):
        t = tareas.pop(idx)
        guardar(tareas)
        print(f"  Tarea eliminada: {t['texto']}")
    else:
        print("  Índice inválido")


def main():
    tareas = cargar()
    print("=== TO-DO CLI ===")
    print("Comandos: list, add <texto>, done <n>, del <n>, salir")
    while True:
        try:
            cmd = input("> ").strip().split(maxsplit=1)
            if not cmd:
                continue
            accion = cmd[0].lower()
            if accion == "salir":
                break
            elif accion == "list":
                mostrar(tareas)
            elif accion == "add" and len(cmd) > 1:
                agregar(tareas, cmd[1])
            elif accion == "done" and len(cmd) > 1:
                completar(tareas, int(cmd[1]) - 1)
            elif accion == "del" and len(cmd) > 1:
                eliminar(tareas, int(cmd[1]) - 1)
            else:
                print("Comandos: list, add <texto>, done <n>, del <n>, salir")
        except (ValueError, IndexError):
            print("Comando inválido")
        except KeyboardInterrupt:
            print("\nAdiós")
            break


if __name__ == "__main__":
    main()

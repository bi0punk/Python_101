import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
import os

DATA_FILE = "Login.txt"


def _hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def _leer_usuarios():
    if not os.path.exists(DATA_FILE):
        return {}
    d = {}
    with open(DATA_FILE, "r") as f:
        for linea in f:
            linea = linea.strip()
            if ":" in linea:
                user, pw = linea.split(":", 1)
                d[user] = pw
    return d


def _guardar_usuario(user, pw_hash):
    with open(DATA_FILE, "a") as f:
        f.write(f"{user}:{pw_hash}\n")


def check(uname, pwd, cpwd, status):
    a, b, c = uname.get(), pwd.get(), cpwd.get()
    usuarios = _leer_usuarios()
    if b != c:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return
    if a not in usuarios:
        messagebox.showerror("Error", "Usuario no encontrado")
        return
    if usuarios[a] != _hash(b):
        messagebox.showerror("Error", "Contraseña incorrecta")
        return
    messagebox.showinfo("Welcome", f"Hello {a}, login exitoso")


def save(uname, pwd, cpwd, status):
    a, b, c = uname.get(), pwd.get(), cpwd.get()
    if not a or not b or not c:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    usuarios = _leer_usuarios()
    if a in usuarios:
        messagebox.showerror("Error", "El usuario ya existe")
        return
    if b != c:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return
    _guardar_user(a, _hash(b))
    messagebox.showinfo("Success", "Cuenta creada exitosamente")
    uname.set("")
    pwd.set("")
    cpwd.set("")


def main():
    root = tk.Tk()
    root.title("Login")
    root.geometry("450x400")
    root.resizable(False, False)

    uname = tk.StringVar()
    pwd = tk.StringVar()
    cpwd = tk.StringVar()

    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text="Iniciar Sesión", font=("Segoe UI", 18, "bold")).pack(pady=(0, 20))

    ttk.Label(frame, text="Usuario", font=("Segoe UI", 12)).pack(anchor="w")
    ttk.Entry(frame, textvariable=uname, font=("Segoe UI", 12)).pack(fill="x", pady=(0, 10))

    ttk.Label(frame, text="Contraseña", font=("Segoe UI", 12)).pack(anchor="w")
    ttk.Entry(frame, textvariable=pwd, show="*", font=("Segoe UI", 12)).pack(fill="x", pady=(0, 10))

    ttk.Label(frame, text="Confirmar Contraseña", font=("Segoe UI", 12)).pack(anchor="w")
    ttk.Entry(frame, textvariable=cpwd, show="*", font=("Segoe UI", 12)).pack(fill="x", pady=(0, 20))

    btn_frame = ttk.Frame(frame)
    btn_frame.pack()

    ttk.Button(btn_frame, text="Login", command=lambda: check(uname, pwd, cpwd, None)).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Registrarse", command=lambda: save(uname, pwd, cpwd, None)).pack(side="left", padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import itertools
import math

def factorial(n):
    return math.factorial(n)

def calcular_permutaciones(n, r, con_repeticion):
    if con_repeticion:
        return list(itertools.product(range(n), repeat=r))
    else:
        return list(itertools.permutations(range(n), r))

def calcular_combinaciones(n, r, con_repeticion):
    if con_repeticion:
        return list(itertools.combinations_with_replacement(range(n), r))
    else:
        return list(itertools.combinations(range(n), r))

def calcular():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        if tipo_var.get() == "Permutaciones":
            if repeticion_var.get() == "Con Repetición":
                resultado = calcular_permutaciones(n, r, True)
                messagebox.showinfo("Resultado", f"Permutaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}")
            else:
                if r > n:
                    raise ValueError("Para permutaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_permutaciones(n, r, False)
                cantidad = factorial(n) // factorial(n - r)
                messagebox.showinfo("Resultado", f"Cantidad de permutaciones: {cantidad}\nResultados:\n{resultado}")
        
        else:  # Combinaciones
            if repeticion_var.get() == "Con Repetición":
                resultado = calcular_combinaciones(n, r, True)
                messagebox.showinfo("Resultado", f"Combinaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}")
            else:
                if r > n:
                    raise ValueError("Para combinaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_combinaciones(n, r, False)
                cantidad = factorial(n) // (factorial(r) * factorial(n - r))
                messagebox.showinfo("Resultado", f"Cantidad de combinaciones: {cantidad}\nResultados:\n{resultado}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Combinaciones y Permutaciones")
root.geometry("400x400")
root.configure(bg="#e6f7ff")
fuente = tkfont.Font(family="Arial", size=12)

# Título de la aplicación
tk.Label(root, text="Permutaciones y Combinaciones", font=tkfont.Font(family="Arial", size=16, weight="bold"), bg="#e6f7ff").pack(pady=10)

# Entrada para n
tk.Label(root, text="Ingresa el valor de n:", font=fuente, bg="#e6f7ff").pack(pady=5)
entry_n = tk.Entry(root, font=fuente, width=20)
entry_n.pack(pady=5)

# Entrada para r
tk.Label(root, text="Ingresa el valor de r:", font=fuente, bg="#e6f7ff").pack(pady=5)
entry_r = tk.Entry(root, font=fuente, width=20)
entry_r.pack(pady=5)

# Variables para menús desplegables
tipo_var = tk.StringVar(value="Permutaciones")
repeticion_var = tk.StringVar(value="Con Repetición")

# Menú para tipo (Permutaciones / Combinaciones)
tipo_menu = tk.OptionMenu(root, tipo_var, "Permutaciones", "Combinaciones")
tk.Label(root, text="Selecciona tipo:", font=fuente, bg="#e6f7ff").pack(pady=5)
tipo_menu.pack(pady=5)

# Menú para repetición (Con / Sin Repetición)
repeticion_menu = tk.OptionMenu(root, repeticion_var, "Con Repetición", "Sin Repetición")
tk.Label(root, text="Selecciona repetición:", font=fuente, bg="#e6f7ff").pack(pady=5)
repeticion_menu.pack(pady=5)

# Botón para calcular
tk.Button(root, text="Calcular", command=calcular, font=fuente).pack(pady=20)

# Iniciar el bucle de la aplicación
root.mainloop()





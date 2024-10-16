import tkinter as tk
from tkinter import messagebox
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

def calcular_permutaciones_con_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        resultado = calcular_permutaciones(n, r, True)
        messagebox.showinfo("Resultado", f"Permutaciones con repetición:\nCantidad: {len(resultado)}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_permutaciones_sin_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        if r > n:
            raise ValueError("Para permutaciones sin repetición, r no puede ser mayor que n.")
        
        cantidad = factorial(n) // factorial(n - r)
        messagebox.showinfo("Resultado", f"Cantidad de permutaciones: {cantidad}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_combinaciones_con_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        resultado = calcular_combinaciones(n, r, True)
        messagebox.showinfo("Resultado", f"Combinaciones con repetición:\nCantidad: {len(resultado)}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_combinaciones_sin_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        if r > n:
            raise ValueError("Para combinaciones sin repetición, r no puede ser mayor que n.")
        
        cantidad = factorial(n) // (factorial(r) * factorial(n - r))
        messagebox.showinfo("Resultado", f"Cantidad de combinaciones: {cantidad}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Combinaciones y Permutaciones")

# Entrada para n
tk.Label(root, text="Ingresa el valor de n:").pack(pady=5)
entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Entrada para r
tk.Label(root, text="Ingresa el valor de r:").pack(pady=5)
entry_r = tk.Entry(root)
entry_r.pack(pady=5)

# Botones para calcular
tk.Button(root, text="Permutaciones con Repetición", command=calcular_permutaciones_con_repeticion).pack(pady=5)
tk.Button(root, text="Permutaciones sin Repetición", command=calcular_permutaciones_sin_repeticion).pack(pady=5)
tk.Button(root, text="Combinaciones con Repetición", command=calcular_combinaciones_con_repeticion).pack(pady=5)
tk.Button(root, text="Combinaciones sin Repetición", command=calcular_combinaciones_sin_repeticion).pack(pady=5)

# Iniciar el bucle de la aplicación
root.mainloop()

  
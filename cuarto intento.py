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
                messagebox.showinfo("Resultado", f"Permutaciones con repetición:\nCantidad: {len(resultado)}", icon='info')
            else:
                if r > n:
                    raise ValueError("Para permutaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_permutaciones(n, r, False)
                cantidad = factorial(n) // factorial(n - r)
                messagebox.showinfo("Resultado", f"Cantidad de permutaciones: {cantidad}", icon='info')

        else:  
            if repeticion_var.get() == "Con Repetición":
                resultado = calcular_combinaciones(n, r, True)
                messagebox.showinfo("Resultado", f"Combinaciones con repetición:\nCantidad: {len(resultado)}", icon='info')
            else:
                if r > n:
                    raise ValueError("Para combinaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_combinaciones(n, r, False)
                cantidad = factorial(n) // (factorial(r) * factorial(n - r))
                messagebox.showinfo("Resultado", f"Cantidad de combinaciones: {cantidad}", icon='info')

        # Clear input fields after calculation
        entry_n.delete(0, tk.END)
        entry_r.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Combinaciones y Permutaciones")
root.geometry("400x400")
root.configure(bg="#FF7F50")
fuente = tkfont.Font(family="Arial", size=12)

tk.Label(root, text="Permutaciones y Combinaciones", font=tkfont.Font(family="Arial", size=16, weight="bold"), bg="#E6E6FA").pack(pady=10)

tk.Label(root, text="Ingresa el valor de n:", font=fuente, bg="#F08080").pack(pady=5)
entry_n = tk.Entry(root, font=fuente, width=20)
entry_n.pack(pady=5)

tk.Label(root, text="Ingresa el valor de r:", font=fuente, bg="#F08080").pack(pady=5)
entry_r = tk.Entry(root, font=fuente, width=20)
entry_r.pack(pady=5)

tipo_var = tk.StringVar(value="Permutaciones")
repeticion_var = tk.StringVar(value="Con Repetición")

tipo_menu = tk.OptionMenu(root, tipo_var, "Permutaciones", "Combinaciones")
tk.Label(root, text="Selecciona tipo:", font=fuente, bg="#F08080").pack(pady=5)
tipo_menu.pack(pady=5)

repeticion_menu = tk.OptionMenu(root, repeticion_var, "Con Repetición", "Sin Repetición")
tk.Label(root, text="Selecciona repetición:", font=fuente, bg="#F08080").pack(pady=5)
repeticion_menu.pack(pady=5)


calcular_btn = tk.Button(root, text="Calcular", command=calcular, font=fuente, bg="#1E90FF", fg="white")
calcular_btn.pack(pady=20)

root.mainloop()

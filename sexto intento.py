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
                messagebox.showinfo("Resultado", f"Permutaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}",
                                    icon='info')
            else:
                if r > n:
                    raise ValueError("Para permutaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_permutaciones(n, r, False)
                cantidad = factorial(n) // factorial(n - r)
                messagebox.showinfo("Resultado", f"Cantidad de permutaciones: {cantidad}\nResultados:\n{resultado}",
                                    icon='info')
        
        else:  
            if repeticion_var.get() == "Con Repetición":
                resultado = calcular_combinaciones(n, r, True)
                messagebox.showinfo("Resultado", f"Combinaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}",
                                    icon='info')
            else:
                if r > n:
                    raise ValueError("Para combinaciones sin repetición, r no puede ser mayor que n.")
                resultado = calcular_combinaciones(n, r, False)
                cantidad = factorial(n) // (factorial(r) * factorial(n - r))
                messagebox.showinfo("Resultado", f"Cantidad de combinaciones: {cantidad}\nResultados:\n{resultado}",
                                    icon='info')

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def set_tipo(tipo):
    tipo_var.set(tipo)
    tipo_btn1.config(bg="#FFB6C1" if tipo == "Permutaciones" else "#FF7F50")
    tipo_btn2.config(bg="#FFB6C1" if tipo == "Combinaciones" else "#FF7F50")

def set_repeticion(repeticion):
    repeticion_var.set(repeticion)
    repeticion_btn1.config(bg="#FFB6C1" if repeticion == "Con Repetición" else "#FF7F50")
    repeticion_btn2.config(bg="#FFB6C1" if repeticion == "Sin Repetición" else "#FF7F50")

root = tk.Tk()
root.title("Combinaciones y Permutaciones")
root.geometry("400x400")
root.configure(bg="#E6E6FA")
fuente = tkfont.Font(family="Arial", size=12)

tk.Label(root, text="Permutaciones y Combinaciones", font=tkfont.Font(family="Arial", size=16, weight="bold"), bg="#FF7F50").pack(pady=10)

tk.Label(root, text="Ingresa el valor de n:", font=fuente, bg="#FF7F50").pack(pady=5)
entry_n = tk.Entry(root, font=fuente, width=20)
entry_n.pack(pady=5)

tk.Label(root, text="Ingresa el valor de r:", font=fuente, bg="#FF7F50").pack(pady=5)
entry_r = tk.Entry(root, font=fuente, width=20)
entry_r.pack(pady=5)

tipo_var = tk.StringVar(value="Permutaciones")
repeticion_var = tk.StringVar(value="Con Repetición")


tipo_btn1 = tk.Button(root, text="Permutaciones", command=lambda: set_tipo("Permutaciones"), font=fuente, bg="#FF7F50", fg="black")
tipo_btn1.pack(pady=5)

tipo_btn2 = tk.Button(root, text="Combinaciones", command=lambda: set_tipo("Combinaciones"), font=fuente, bg="#FF7F50", fg="black")
tipo_btn2.pack(pady=5)

tk.Label(root, text="Selecciona repetición:", font=fuente, bg="#FF7F50").pack(pady=5)


repeticion_btn1 = tk.Button(root, text="Con Repetición", command=lambda: set_repeticion("Con Repetición"), font=fuente, bg="#FF7F50", fg="black")
repeticion_btn1.pack(pady=5)

repeticion_btn2 = tk.Button(root, text="Sin Repetición", command=lambda: set_repeticion("Sin Repetición"), font=fuente, bg="#FF7F50", fg="black")
repeticion_btn2.pack(pady=5)

calcular_btn = tk.Button(root, text="Calcular", command=calcular, font=fuente, bg="#F08080", fg="black")
calcular_btn.pack(pady=20)

root.mainloop()

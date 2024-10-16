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

def calcular_permutaciones_con_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        resultado = calcular_permutaciones(n, r, True)
        messagebox.showinfo("Resultado", f"Permutaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}") 

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
        
        resultado = calcular_permutaciones(n, r, False)
        cantidad = factorial(n) // factorial(n - r)
        messagebox.showinfo("Resultado", f"Cantidad de permutaciones: {cantidad}\nResultados:\n{resultado}")  

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_combinaciones_con_repeticion():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if n < 0 or r < 0:
            raise ValueError("Los valores deben ser no negativos.")
        
        resultado = calcular_combinaciones(n, r, True)
        messagebox.showinfo("Resultado", f"Combinaciones con repetición:\nCantidad: {len(resultado)}\nResultados:\n{resultado}")  

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
        
        resultado = calcular_combinaciones(n, r, False)
        cantidad = factorial(n) // (factorial(r) * factorial(n - r))
        messagebox.showinfo("Resultado", f"Cantidad de combinaciones: {cantidad}\nResultados:\n{resultado}")  

    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Combinaciones y Permutaciones")


root.geometry("400x400")  


root.configure(bg="#e6f7ff")  


fuente = tkfont.Font(family="Arial ", size=12)


tk.Label(root, text="Ingresa el valor de n:", font=fuente, bg="#e6f7ff").pack(pady=5)
entry_n = tk.Entry(root, font=fuente, width=20)  
entry_n.pack(pady=5)


tk.Label(root, text="Ingresa el valor de r:", font=fuente, bg="#e6f7ff").pack(pady=5)
entry_r = tk.Entry(root, font=fuente, width=20)  
entry_r.pack(pady=5)


tk.Button(root, text="Permutaciones con Repetición", command=calcular_permutaciones_con_repeticion, font=fuente).pack(pady=5)
tk.Button(root, text="Permutaciones sin Repetición", command=calcular_permutaciones_sin_repeticion, font=fuente).pack(pady=5)
tk.Button(root, text="Combinaciones con Repetición", command=calcular_combinaciones_con_repeticion, font=fuente).pack(pady=5)
tk.Button(root, text="Combinaciones sin Repetición", command=calcular_combinaciones_sin_repeticion, font=fuente).pack(pady=5)


root.mainloop()
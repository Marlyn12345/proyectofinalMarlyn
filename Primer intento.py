import tkinter as tk
from tkinter import messagebox
from math import factorial

def permutaciones_sin_repeticion(n, r):
    return factorial(n) // factorial(n - r)

def combinaciones_sin_repeticion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutaciones_con_repeticion(n, r):
    return n ** r

def combinaciones_con_repeticion(n, r):
    return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))

def calcular():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        
        if r > n:
            messagebox.showerror("Error", "r no puede ser mayor que n para permutaciones y combinaciones sin repetición.")
            return

        result_permutaciones_sin = permutaciones_sin_repeticion(n, r)
        result_combinaciones_sin = combinaciones_sin_repeticion(n, r)
        result_permutaciones_con = permutaciones_con_repeticion(n, r)
        result_combinaciones_con = combinaciones_con_repeticion(n, r)

        messagebox.showinfo("Resultados", f"""
        Permutaciones sin repetición: {result_permutaciones_sin}
        Combinaciones sin repetición: {result_combinaciones_sin}
        Permutaciones con repetición: {result_permutaciones_con}
        Combinaciones con repetición: {result_combinaciones_con}
        """)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números enteros válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Permutaciones y Combinaciones")

# Crear los elementos de la interfaz
label_n = tk.Label(root, text="Ingresa n:")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()

label_r = tk.Label(root, text="Ingresa r:")
label_r.pack()
entry_r = tk.Entry(root)
entry_r.pack()

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

root.mainloop()





import tkinter as tk

# 1. CREAR LA VENTANA
ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("325x400")

# 2. CREAR LA PANTALLA (Entry)
pantalla = tk.Entry(ventana, font=("Arial", 20), justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # Ocupa 4 columnas

# 3. CREAR LAS FUNCIONES (El cerebro de la calculadora)
def agregar(valor):
    pantalla.insert(tk.END, valor)
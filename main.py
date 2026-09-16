import tkinter as tk

# 1. CREAR LA VENTANA
ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("325x400")

# 2. CREAR LA PANTALLA (Entry)
pantalla = tk.Entry(ventana, font=("Arial", 15), justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # Ocupa 4 columnas

# 3. CREAR LAS FUNCIONES (El cerebro de la calculadora)
def agregar(valor):
    pantalla.insert(tk.END, valor)

def borrar():
    pantalla.delete(0, tk.END)

def calcular():
    pass

# Botón que limpia(borrar) la pantalla
# Fila 0
btn_c = tk.Button(ventana, text="C", width=5, height=2, command=borrar)
btn_c.grid(row=2, column=0)

# 4. CREAR Y COLOCAR LOS BOTONES (Grid)
# Fila 1
btn_7 = tk.Button(ventana, text="7", width=5, height=2, command=lambda: agregar("7"))
btn_7.grid(row=3, column=0, pady=7)

btn_8 = tk.Button(ventana, text="8", width=5, height=2, command=lambda: agregar("8"))
btn_8.grid(row=3, column=1, pady=7)

btn_9 = tk.Button(ventana, text="9", width=5, height=2, command=lambda: agregar("9"))
btn_9.grid(row=3, column=2, pady=7)

btn_multi = tk.Button(ventana, text="*", width=5, height=2, command=lambda: agregar("*"))
btn_multi.grid(row=3, column=3, pady=7)

# Fila 2
btn_4 = tk.Button(ventana, text="4", width=5, height=2, command=lambda: agregar("4"))
btn_4.grid(row=4, column=0, pady=7)

btn_5 = tk.Button(ventana, text="5", width=5, height=2, command=lambda: agregar("5"))
btn_5.grid(row=4, column=1, pady=7)

btn_6 = tk.Button(ventana, text="6", width=5, height=2, command=lambda: agregar("6"))
btn_6.grid(row=4, column=2, pady=7)

btn_res = tk.Button(ventana, text="-", width=5, height=2, command=lambda: agregar("-"))
btn_res.grid(row=4, column=3, pady=7)

# Fila 3
btn_1 = tk.Button(ventana, text="1", width=5, height=2, command=lambda: agregar("1"))
btn_1.grid(row=5, column=0, pady=7)

btn_2 = tk.Button(ventana, text="2", width=5, height=2, command=lambda: agregar("2"))
btn_2.grid(row=5, column=1, pady=7)

btn_3 = tk.Button(ventana, text="3", width=5, height=2, command=lambda: agregar("3"))
btn_3.grid(row=5, column=2, pady=7)

btn_sum = tk.Button(ventana, text="+", width=5, height=2, command=lambda: agregar("+"))
btn_sum.grid(row=5, column=3, pady=7)

# 5. MANTENER LA VENTANA ABIERTA
ventana.mainloop()
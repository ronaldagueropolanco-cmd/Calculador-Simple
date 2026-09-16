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

def borrar():
    pantalla.delete(0, tk.END)

def calcular():
    # Código para resolver la operación con eval()
    pass

# 4. CREAR Y COLOCAR LOS BOTONES (Grid)
# Aquí creas tus botones uno a uno o usando un bucle, por ejemplo:
btn_7 = tk.Button(ventana, text="7", width=5, height=2, command=lambda: agregar("7"))
btn_7.grid(row=3, column=0, pady=7)

# Botón que limpia(borrar) la pantalla
btn_c = tk.Button(ventana, text="C", width=5, height=2, command=borrar)
btn_c.grid(row=2, column=0)

# ... (así con el resto de botones: 8, 9, +, etc.)

# 5. MANTENER LA VENTANA ABIERTA
ventana.mainloop()
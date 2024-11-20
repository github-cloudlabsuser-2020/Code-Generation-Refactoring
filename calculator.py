import tkinter as tk
from tkinter import messagebox

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        return ""

def on_button_click(char):
    current_text = entry.get()
    new_text = current_text + str(char)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Básica")

# Crear el campo de entrada
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Crear los botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x) if x != '=' else on_equal()
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botón de limpiar
tk.Button(root, text='C', width=5, height=2, command=on_clear).grid(row=row_val, column=col_val)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
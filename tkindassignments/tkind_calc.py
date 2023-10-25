import tkinter as tk

def update_expression(value):
    current_expression = expression.get()
    expression.set(current_expression + str(value))


def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Error")

def clear():
    expression.set("")


root = tk.Tk()
root.title("Simple Calculator")


expression = tk.StringVar()


entry = tk.Entry(root, textvariable=expression, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda btn=button: update_expression(btn) if btn != '=' and btn != 'C' else calculate() if btn == '=' else clear()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


root.mainloop()

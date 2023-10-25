# Try to configure Label widget with various options 
#     like background red and font   with Times New Roman 18 size.

import tkinter as tk
root = tk.Tk()
root.title("Label Configuration")
label = tk.Label(root, text="Hello, tkinter!", bg="red", font=("Times New Roman", 18))
label.pack(padx=20, pady=20)  
root.mainloop()

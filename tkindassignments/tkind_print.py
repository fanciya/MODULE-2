
# Try to configure GUI, that should define a simple function which will 
# print the data entered by the user in the text-area, upon clicking on a button.

import tkinter as tk

# Function to print data entered by the user
def print_data():
    user_input = entry.get()  # Get text from the entry field
    text_area.insert(tk.END, user_input + "\n")  # Insert the text into the text area
    entry.delete(0, tk.END)  # Clear the entry field after printing

# Create the main window
root = tk.Tk()
root.title("Data Printer")

# Entry widget for user input
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=20)

# Button to print data
print_button = tk.Button(root, text="Print Data", command=print_data, font=("Arial", 14))
print_button.pack()

# Text area to display printed data
text_area = tk.Text(root, width=40, height=10, font=("Arial", 12))
text_area.pack(pady=20)

# Run the main loop
root.mainloop()

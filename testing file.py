import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = combo.get()
    print(f"Selected: {selected_value}")

# Create the main window
root = tk.Tk()
root.title("Dropdown Example")

# Create a label
label = ttk.Label(root, text="Select an option:")
label.pack(pady=10)

# Create a dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(root, values=options)
combo.pack(pady=10)

# Bind the selection event
combo.bind("<<ComboboxSelected>>", on_select)

# Start the Tkinter event loop
root.mainloop()
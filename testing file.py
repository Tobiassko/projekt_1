import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = tk.Tk()
root.title("Tkinter Window")

# Set the window size
root.geometry("400x300")


# Create a sample plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4,5], [10, 20, 25, 30,20])
ax.set_title('Mney.com')

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the application
root.mainloop()
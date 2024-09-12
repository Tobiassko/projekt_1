import blocks as bl
from blocks import block_catagorys


import tkinter as tk
from tkinter import ttk
current_color_index = 0
def block_color():
    global current_color_index
    button_color.set(block_catagorys[current_color_index].replace("_", " ").title())
    current_color_index +=1
    if current_color_index == 16:
        current_color_index = 0
    
    

#window
window = tk.Tk()
window.title()
window.geometry("500x500")


#input frame
input_frame = tk.Frame(master=window)
button_color = tk.StringVar()
button_switch = ttk.Button(master=input_frame, textvariable=button_color, text="testing", command=block_color)


#packs
input_frame.pack()
button_switch.pack()

#run
window.mainloop()

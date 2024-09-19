import blocks as bl
from blocks import blocks
from blocks import block_catagorys
import random as rand


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
window.title("Minecraft assistance program")
window.geometry("500x500")


#input frame
input_frame = tk.Frame(master=window)
button_color = tk.StringVar()
rand_selection = tk.StringVar()
#call block color to update
block_color()


# select and define the random block
def random_block():
    global rand_selection
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    ran_block = rand.choice(current_blocks)
    rand_selection.set(f"Block:{ran_block}\n value: {round((len(ran_block)*2)**0.5)}")
    print(ran_block)
random_block()

#define label and button for block chatagory switching and redo button
color_chatagory_switch_label = ttk.Label(master=input_frame, text="Block color:", font="system 15 bold")
button_switch = ttk.Button(master=input_frame, textvariable=button_color, text="testing", command=block_color)

redo_button = ttk.Button(master=input_frame, text="Block", command=random_block)
current_block_selection = ttk.Label(master=window, textvariable=rand_selection, font="system 25 bold")





#debug lable
Debug_lable = ttk.Label(master=window, )

#packs

#input packs
input_frame.pack()
color_chatagory_switch_label.pack(side="left")
button_switch.pack(side="left")
redo_button.pack(side="left")
current_block_selection.pack()

#debug
Debug_lable.pack()




#run
window.mainloop()

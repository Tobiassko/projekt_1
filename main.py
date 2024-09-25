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
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    if current_color_index == 16:
        current_color_index = 0
    if 'block_box' in globals():
        block_box['values'] = list(current_blocks.keys())
        block_box.set('Select a block')



#window
window = tk.Tk()
window.title("Minecraft assistance program")
window.geometry("960x540")



#input frame
input_frame = tk.Frame(master=window)
use_diamonds = tk.BooleanVar(master=input_frame, value=False)
button_color = tk.StringVar()
rand_selection = tk.StringVar()

#call block color to update
block_color()
#------------------------------------------------ definitions ------------------------------------------------
# select and define the random block
def random_block():
    # Declare global variables to be used in the function
    global rand_selection,value, ran_block, current_blocks
    # Get the current block category based on the current color index
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    # Select a random block from the current block category
    ran_block = rand.choice(list(current_blocks.keys()))
    # Get the value of the selected block
    value = current_blocks[ran_block]
    # Check if the diamond switch is off
    if use_diamonds.get() == False:
        # Set the random selection string with the block details
        rand_selection.set(f"Block: {ran_block}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")
    else:
        # If the diamond switch is on, adjust the value accordingly
        value = value / 1500
        # Set the random selection string with the adjusted block details
        rand_selection.set(f"Block: {ran_block}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")
    
    # Print the selected block and its value for debugging purposes
    print(ran_block)
    print(f"value: {value}")

# Call the random_block function to initialize the random block selection
random_block()


def diamond_switch():
    global value
    value = (current_blocks[ran_block])
    if use_diamonds.get() == True:
        value = round(value/1500, 2)
        rand_selection.set(f"Block: {ran_block}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")
    else:
        rand_selection.set(f"Block: {ran_block}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")

def on_select(event):
    print(f"Selected: {block_box.get()}")
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    print(f"Value: {current_blocks[block_box.get()]}")
    value = current_blocks[block_box.get()]
    if use_diamonds.get() == True:
        value = value/1500
        value = round(value, 2)
        rand_selection.set(f"Block: {block_box.get()}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")
    else:
        rand_selection.set(f"Block: {block_box.get()}\nValue: {value}\nStack: {value*64:,.0f}\nChest: {value*1728:,.0f}\nDouble Chest: {value*3456:,.0f}\nChunk: {value*98304:,.0f}")    
#------------------------------------------------ input frame ------------------------------------------------

#define label and button for block chatagory switching and redo button
# Label for block color category
color_chatagory_switch_label = ttk.Label(master=input_frame, text="Block color:", font="system 15 bold")

# Button to switch block color category
button_switch = ttk.Button(master=input_frame, textvariable=button_color, text="testing", command=block_color)

# Checkbox to toggle the use of diamonds
diamond_button = ttk.Checkbutton(master=input_frame, text="Use Diamonds Instead", variable=use_diamonds, command=diamond_switch)

# Button to select a new random block
redo_button = ttk.Button(master=input_frame, text="Random Block", command=random_block)

# Label to display the current block selection
current_block_selection = ttk.Label(master=window, textvariable=rand_selection, font="system 25 bold")


# Combobox for selecting a specific block within the selected category
block_box_list = list(current_blocks.keys())
block_box = ttk.Combobox(master=input_frame, values=block_box_list, state="readonly")
block_box.set('Select a block')
block_box.bind("<<ComboboxSelected>>", on_select)



#debug lable
Debug_lable = ttk.Label(master=window, text=" asd", font="system 15 bold")


#------------------------------------------------ pack ------------------------------------------------
#input packs
input_frame.pack()
color_chatagory_switch_label.pack(side="left")
button_switch.pack(side="left")
redo_button.pack(side="left")
block_box.pack(side="left")
diamond_button.pack(side="left")
current_block_selection.pack()

#debug
Debug_lable.pack()




#run
window.mainloop()
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
global value, ran_block, current_blocks
current_blocks = getattr(bl, block_catagorys[current_color_index-1])
def diamond_switch():
    # Get the current block category based on the current color index
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    # Call the on_select function to update the selection
    on_select(1)

def on_select(event):
    global value
    # Print the selected block for debugging purposes
    print(f"Selected: {block_box.get()}")
    # Get the current block category based on the current color index
    current_blocks = getattr(bl, block_catagorys[current_color_index-1])
    # Print the value of the selected block for debugging purposes
    print(f"Value: {current_blocks[block_box.get()]}")
    # Get the value of the selected block
    value = current_blocks[block_box.get()]
    # Check if the diamond switch is on
    update_entry_title()
    if use_diamonds.get() == True:
        # Adjust the value accordingly
        value = value *119000000000
        value = round(value, 2)
        update_entry_title()
        # Set the random selection string with the adjusted block details
        rand_selection.set(f"Block: {block_box.get()}\nValue: {value/64:,.0f}\nStack: {value:,.0f}\nChest: {value*1728/64:,.0f}\nDouble Chest: {value*3456/64:,.0f}\nChunk: {value*98304/64:,.0f}")
    else:
        # Set the random selection string with the block details
        rand_selection.set(f"Block: {block_box.get()}\nValue: {value/64}\nStack: {value:,.0f}\nChest: {value*1728/64:,.0f}\nDouble Chest: {value*3456/64:,.0f}\nChunk: {value*98304/64:,.0f}")

# Function to update the entry title based on the value entered
def update_entry_title(*args):
    # Set the entry title string to the current value of the entry widget
    try:
        # Try to convert the entry value to a float
        float_value = int(value_entry.get())
        if use_diamonds.get() == True:
            entry_title_str.set(f"Value of {float(value_entry.get())} {block_box.get()} is:{int(value_entry.get())*value/64}")
        else:
            entry_title_str.set(f"Value of {float(value_entry.get())} {block_box.get()} is:{int(value_entry.get())*value/64}")
    except ValueError:
        # If conversion fails, set an error message
        entry_title_str.set("Enter a valid number")

#------------------------------------------------ input frame ------------------------------------------------

#define label and button for block chatagory switching and redo button
# Label for block color category
color_chatagory_switch_label = ttk.Label(master=input_frame, text="Block color:", font="system 15 bold")

# Button to switch block color category
button_switch = ttk.Button(master=input_frame, textvariable=button_color, text="testing", command=block_color)

# Checkbox to toggle the use of diamonds
diamond_button = ttk.Checkbutton(master=input_frame, text="Use kr Instead", variable=use_diamonds, command=diamond_switch)

# Label to display the current block selection
current_block_selection = ttk.Label(master=window, textvariable=rand_selection, font="system 25 bold")


# Combobox for selecting a specific block within the selected category
block_box_list = list(current_blocks.keys())
block_box = ttk.Combobox(master=input_frame, values=block_box_list, state="readonly")
block_box.set('Select a block')
block_box.bind("<<ComboboxSelected>>", on_select)



value_entry = tk.Entry(master=window)
value_entry.bind("<KeyRelease>", update_entry_title)

entry_title_str = tk.StringVar()
entry_title = tk.Label(master=window, textvariable=entry_title_str, font="system 15 bold")

#debug label
Debug_lable = ttk.Label(master=window, text="Debug", font="system 15 bold")


#------------------------------------------------ pack ------------------------------------------------
#input packs

input_frame.pack()
color_chatagory_switch_label.pack(side="left")
button_switch.pack(side="left")
block_box.pack(side="left")
diamond_button.pack(side="left")
current_block_selection.pack()
value_entry.pack()
entry_title.pack()

#debug


#run
window.mainloop()
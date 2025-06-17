import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.title("What the button!")
window.geometry('300x300')
window.resizable(False, False)

# buttons
def button_func():
    print('button clicked')

button_string = ttk.StringVar(value="Button 1")

button = ttk.Button(master=window, text="Button 1", command=button_func)
button.pack(padx=5, pady=5)

# Checkbutton
check_var = ttk.BooleanVar()
check = ttk.Checkbutton(
    master=window,
    text="Checkbutton",
    command= lambda: print(check_var.get()),
    variable=check_var,
    onvalue=True, offvalue=False)
check.pack(padx=5, pady=5)

# radiobuttons
# note value can be anything from string to int.
radio_var = ttk.StringVar()

radio1 = ttk.Radiobutton(
    master=window,
    text="Radiobutton 1",
    value=1,
    variable=radio_var,
    command= lambda: print(radio_var.get()),
)
radio2 = ttk.Radiobutton(
    master=window,
    text="Radiobutton 2",
    value=2,
    variable=radio_var,
    command= lambda: print(radio_var.get())
)
radio1.pack(padx=5, pady=5)
radio2.pack(padx=5, pady=5)

window.mainloop()
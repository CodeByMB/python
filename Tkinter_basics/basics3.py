import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.title('Basics 3')
window.resizable(False, False)
window.geometry('300x300')

string_var = ttk.StringVar()
option_var = ttk.StringVar()
radioButtons = ttk.StringVar()

label = ttk.Label(master=window, text='Label 1', textvariable= string_var)
label.pack(padx=5, pady=5)


radiobutton1 = ttk.Radiobutton(master=window, text='Option 1', variable=option_var, value='Option 1')
radiobutton2 = ttk.Radiobutton(master=window, text='Option 2', variable=option_var, value='Option 2')
radiobutton1.pack(padx=5, pady=5)
radiobutton2.pack(padx=5, pady=5)

checkbox1 = ttk.Checkbutton(master=window, text='Checkbox 1', style='Squaretoggle.Toolbutton')
checkbox2 = ttk.Checkbutton(master=window, text='Checkbox 2', style='Roundtoggle.Toolbutton')
checkbox1.pack(padx=5, pady=5)
checkbox2.pack(padx=5, pady=5)

button2 = ttk.Button(master=window, text='Submit', style='info.TButton')
button2.pack(padx=5, pady=5)

entry = ttk.Entry(master=window, textvariable= string_var)
entry.pack(padx=5, pady=5)

window.mainloop()
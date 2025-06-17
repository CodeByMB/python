import tkinter as tk
import ttkbootstrap as ttk

def button_func(entry_string):
    print("A button was pressed")
    print(entry_string.get())

window = ttk.Window(themename = 'superhero')
window.title("What the button 2!")
window.geometry('300x300')
window.resizable(False, False)

entry_string = ttk.StringVar(value="Test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='Button', command= lambda: button_func(entry_string))
button.pack()

window.mainloop()
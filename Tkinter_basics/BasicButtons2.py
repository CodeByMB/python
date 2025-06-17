import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.title("What the button 2!")
window.geometry('300x300')
window.resizable(False, False)

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='Button')
button.pack()

window.mainloop()
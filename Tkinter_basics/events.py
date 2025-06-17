import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename = 'superhero')
window.title("Events")
window.geometry('600x500')
window.resizable(False, False)

text = ttk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text='Button')
btn.pack()

window.bind('<Alt-KeyPress-a>', lambda event: print("An event"))

window.mainloop()
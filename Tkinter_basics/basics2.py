import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    entry_text = entry.get()
    label.configure(text = entry_text)
    entry['state'] = 'disabled'

def button_func2():
    label.configure(text='Some text')
    entry['state'] = 'enabled'

# window
window = ttk.Window(themename = 'superhero')
window.title('Basics 2')
window.geometry('300x300')
window.resizable(False, False)

# widgets
label = ttk.Label(master=window, text="Hello World")
label.pack(padx=5, pady=5)

entry = ttk.Entry(master=window)
entry.pack(padx=5, pady=5)

button = ttk.Button(master=window, text="OK", command= button_func)
button.pack(padx=5, pady=5)

button2 = ttk.Button(master=window, text="Enable", command=button_func2)
button2.pack(padx=5, pady=5)
# run
window.mainloop()
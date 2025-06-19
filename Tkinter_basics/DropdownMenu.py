import tkinter as tk
from tkinter import ttk

from main_course import value

window = tk.Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Combo and Spin")

#combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string, values=items)
#combo['values'] = items
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text=f'Selected value: {food_string.get()}'))
combo_label = ttk.Label(window, text='A label', textvariable=food_string)
combo_label.pack()

# Spinbox
spin = ttk.Spinbox(window, from_=0, to=100, command=lambda:print('A arrow was pressed'))
spin.pack()

window.mainloop()
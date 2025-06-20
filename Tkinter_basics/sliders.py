import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'superhero')
window.title("Sliders")
window.resizable(False, False)
window.geometry("600x400")

scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(
    window,
    command= lambda value: print(value),
    from_ = 0,
    to = 25,
    length = 300,
    orient = tk.VERTICAL,
    variable = scale_int,)
scale.pack(padx=5, pady=5)

window.mainloop()

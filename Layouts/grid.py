import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grid")
window.geometry("600x400")

# setup grid:
colums = (1,2,3,4,5)
rows = (1,2,3)
window.columnconfigure(colums, weight=1, uniform='a')
window.rowconfigure(rows, weight=1, uniform='a')

label1 = tk.Label(window, text="Label 1", background="red")
label2 = tk.Label(window, text="Label 2", background="blue")
label3 = tk.Label(window, text="Label 3", background="green")
label4 = tk.Label(window, text="Label 4", background="yellow")
label5 = tk.Label(window, text="Label 5", background="purple")

label1.grid(row=1, column=1, sticky="nsew", columnspan=len(colums))
label2.grid(row=2, column=1, sticky="ns", columnspan=2)
label3.grid(row=3, column=3, sticky="nsew", columnspan=2)
label4.grid(row=2, column=4, sticky="nsew")
label5.grid(row=2, column=5, sticky="nsew", rowspan=2)



window.mainloop()

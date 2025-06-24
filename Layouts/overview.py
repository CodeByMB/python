import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Overview')
window.geometry('600x400')

label1 = tk.Label(window, text='Label 1', background='red')
label2 = tk.Label(window, text='Label 2', background='yellow')
label3 = tk.Label(window, text='Label 3', background='green')
label4 = tk.Label(window, text='Label 4', background='blue')

# pack ------------
# label1.pack(side='left', expand=True, fill='y')
# label2.pack(side='left', expand=True, fill='both')

# grid -------------
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)
# window.rowconfigure(3, weight=1)
#
# label1.grid(row=0, column=0, sticky='nsew', rowspan=4)
# label2.grid(row=1, column=1,columnspan=1, sticky='nsew')
# label3.grid(row=2, column=1,columnspan=1, sticky='nsew')
# label4.grid(row=0, column=2, sticky='nsew', rowspan=4)

# grid -------------
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

label1.grid(row=0, column=0, sticky='nsew', rowspan=4)
label2.grid(row=0, column=1,columnspan=1, sticky='nsew')
label3.grid(row=1, column=1,columnspan=1,rowspan=4,  sticky='nsew')

# place ------------
# If using place use the relx and rely then it follows the with and hight and stays on screen.
# label1.place(x = 200, y = 200, width = 200, height = 100)
# label2.place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = 'center')

window.mainloop()
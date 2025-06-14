import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print('The button has been pressed!')

def button2_func():
    print('Hellloooo!')

# window
window = ttk.Window(themename = 'superhero')
window.title('Tkinter Basics')
window.geometry('800x800')

# ttk Label
label = ttk.Label(
    master=window, 
    text='This is a test')
label.pack()

# ttk text
text = ttk.Text(
    master=window)
text.pack(pady=20)

#ttk entry
entry = ttk.Entry(
    master=window, )
entry.pack()

label1 = ttk.Label(
    master=window, 
    text='my label')
label1.pack()

button = ttk.Button(
    master=window, 
    text = 'A button', 
    command= button_func)
button.pack()

button1 = ttk.Button(
    master=window, 
    text='Hello?', 
    command=button2_func, 
    bootstyle='danger')
button1.pack()
# run
window.mainloop()
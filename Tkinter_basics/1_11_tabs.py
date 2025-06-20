import tkinter as tk
import ttkbootstrap as ttk
 
window = ttk.Window(themename = 'superhero')
window.geometry('600x400')
window.title("Tab Widget")

# Notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Text in tab 1')
label1.pack(padx = 10, pady = 10)
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack(padx = 10, pady = 10)

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Text in tab 2')
label2.pack(padx = 10, pady = 10)
entry2 = ttk.Entry(tab2)
entry2.pack(padx = 10, pady = 10)

notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.pack(padx = 10, pady = 10)

# exercise
# add another tab with 2 buttons and one label inside 

tab_exercise = ttk.Frame(notebook)
button_exercise_1 = ttk.Button(tab_exercise, text = 'button 1')
button_exercise_1.pack(padx = 10, pady = 10)

button_exercise_2 = ttk.Button(tab_exercise, text = 'button 2')
button_exercise_2.pack(padx = 10, pady = 10)

label_exercise_2 = ttk.Label(tab_exercise, text = 'Label')
label_exercise_2.pack(padx = 10, pady = 10)

notebook.add(tab_exercise, text = 'Tab exercise')

# run 
window.mainloop()  
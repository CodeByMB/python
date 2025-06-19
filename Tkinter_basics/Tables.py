import tkinter as tk
import ttkbootstrap as ttk
from random import choice

window = ttk.Window()
window.title("Excel/Treeview")
window.resizable(False, False)
window.geometry('600x400')

#data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(window, columns=('first','last','email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)
# insert value
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}.{last}@email.com'
    data = (first, last, email)
    table.insert('', 0, values=data)

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

window.mainloop()
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, size):
		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0], size[1])

		self.menu = Menu(self)

		self.mainloop()

class Menu(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		ttk.Label(self, background='blue').pack(expand=True, fill= 'both')
		self.pack(expand=True, fill='both')

App('Class based app', (600,600))
from tkinter import *
from tkinter import ttk

tela = Tk()
tela.iconbitmap('icone.ico')
tela.title('Calculadora')
b = ttk.Label(text=(0)).place(x=0, y=1)

tela.mainloop()
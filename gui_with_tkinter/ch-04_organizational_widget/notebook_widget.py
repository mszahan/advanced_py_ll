from tkinter import *
from tkinter import ttk


root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

ttk.Button(frame1, text='click here').pack()

frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='three')

## you can forget the frames here too

root.mainloop()
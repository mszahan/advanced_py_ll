from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()

## can print after entry
print(entry.get())

## it will delete the character in index manner
entry.delete(0, 2)

## it will delete first to last character
entry.delete(0, END)

## you can enter text from specific index
entry.insert(0, 'Enter your text here')

## you can hide text with show='*'
entry.config(show='*')

## you can disable the entry widget
entry.state(['disabled'])

## you can make it readonly
entry.state(['readonly'])

## you can enable the entry widget
entry.state(['!disabled'])




root.mainloop()
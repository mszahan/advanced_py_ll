from tkinter import *
from tkinter import ttk

root = Tk()

## combobox---------------------

month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', "Oct", "Nov", 'Dec'])


## Spinbox ----------------
year = StringVar()
Spinbox(root, from_=1990, to=2025, textvariable=year).pack()


root.mainloop()
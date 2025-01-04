from tkinter import *
from tkinter import ttk


root = Tk()

frame = ttk.Frame(root)
frame.pack()

frame.config(height=100, width=200)

## relief is used for border
frame.config(relief='ridge')

## now add and widget to the frame
## the width and height will now collapse to the widget only
ttk.Button(frame, text='click here').grid()

## you can add padding
frame.config(padding=(30, 15))


##label frame-------------
ttk.LabelFrame(root, height=100, width=200, text='label frame').pack()

root.mainloop()
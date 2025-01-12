from tkinter import *
from tkinter import ttk

root = Tk()

pannedwindow = ttk.Panedwindow(root, orient='horizontal')
pannedwindow.pack(fill='both', expand=True)

frame1 = ttk.Frame(pannedwindow, width=100, height=300, relief='sunken')
frame2 = ttk.Frame(pannedwindow, width=400, height=400, relief='sunken')
frame3 = ttk.Frame(pannedwindow, width=50, height=400, relief='sunken')

## you need to add frames in the panned window
pannedwindow.add(frame1, weight=1)
pannedwindow.add(frame2, weight=4)

## you can insert frame to specific index
pannedwindow.insert(1, frame3)

## you can stop using the window with forget with index
## it doesn't destroy the window
pannedwindow.forget(1)
root.mainloop()
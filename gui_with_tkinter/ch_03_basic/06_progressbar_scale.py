from tkinter import *
from tkinter import ttk

root = Tk()


progressbar = ttk.Progressbar(root, orient='horizontal', length=200)
progressbar.pack()

## progressbar in indterminate mode (don't how long or steps left)
progressbar.config(mode='indeterminate')
## to start the progressbar - it will keep moving back and forth
progressbar.start()
## to stop - it will remain in the lef
progressbar.stop()

## determinate progressbar
progressbar.config(mode='determinate', maximum=11.0, value=4.2)
progressbar.config(value=8)

## step will increase one step
progressbar.step()
## it will increase 5 step, if complete will startover
progressbar.step(5)

## you can create variable with value and assign it to progressbar
pvalue = DoubleVar()
progressbar.config(variable=pvalue)


##scale------------------
scale = ttk.Scale(root, orient='horizontal', length=400, variable= pvalue, 
                  from_=0.0, to=11.0)
scale.pack()

## you can set and get value
scale.set(4.2)
print(scale.get())


root.mainloop()
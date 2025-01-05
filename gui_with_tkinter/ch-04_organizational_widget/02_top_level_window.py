from tkinter import *

root = Tk()

window = Toplevel(root)
window.title('new window')


## you can lower the window with lower
# window.lower()

## you can lift the window with lift
# window.lift(root)

## you maximize the window
# window.state('zoomed')

## you can hide the window 
# window.state('withdrawn')

## you can minimize and reverse with iconify
# window.iconify()
# window.deiconify()

##window.geometry(width X height + x + y)
window.geometry('640x480+50+100')

## we can prevent user from resizing the window in x and y direction
window.resizable(False, False)

## you can limit how long can they resize in x and y direction
window.maxsize(640, 480)
window.minsize(200, 200)

## you can destroy any widget
# window.destroy()

root.mainloop()
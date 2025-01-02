from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text="Click Me")
button.pack()

def callback():
    print("Clicked!")

button.config(command=callback)

## you can simulate the click button
button.invoke()

## this will set the state of the button to disabled
button.state(['disabled'])

## chcking button state
print(button.instate(['disabled']))

## activate the button again
button.state(['!disabled'])

## adding image to the button
logo = PhotoImage(file='py.gif')
small_logo = logo.subsample(5, 5)
button.config(image=small_logo, compound='left')


root.mainloop()
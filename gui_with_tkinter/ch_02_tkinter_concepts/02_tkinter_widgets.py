from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text='Click here')
button.pack()

## you can access the button properties like this
print(button['text'])
## change the properties
button['text'] = 'Press here'
## here is another way to access the button properties
button.config(text='Press me')

## you can get all the properties of the button
print(button.config())  # returns a dictionary

## you can ge the name of the widget
print(str(button))

## add another label to the root
label = ttk.Label(root, text='Hello, World!').pack()

## if you need the file to work you need the line
root.mainloop()

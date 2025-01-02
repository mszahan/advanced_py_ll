from tkinter import *
from tkinter import ttk


root = Tk()

label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()

## Change the text of the label
label.config(text='Howdy, World')

## Change the text of the label
label.config(text='Hello world, I am a label with a very long text')

## you can wrap text in pixel
label.config(wraplength=150)

## you can justify the text
label.config(justify=CENTER)

## you can change the forground color (text color) and background color
label.config(foreground='blue', background='yellow')

## you can change the font of the text
label.config(font=('Courier', 18, 'bold'))




## displaying image ------------------
label.config(text='Hello, python')

logo = PhotoImage(file='py.gif')

## it will replace the text with the image
label.config(image=logo)

## it will keep the text only
label.config(compound='text')

## it will display the text on the center
label.config(compound='center')

## this will display the image left to the text
label.config(compound='left')

### if you just reference to image through a variable it will
### display until the variable is alive (scope),
### once scope is gone like in function and class, image will not be displayed
### so to keep the image alive, you can assign it to label

label.img = logo
label.config(image=label.img)

root.mainloop()
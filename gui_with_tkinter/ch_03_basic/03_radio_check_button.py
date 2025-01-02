from tkinter import *
from tkinter import ttk

root = Tk()

checkbutton = ttk.Checkbutton(root, text='SPAM?')
checkbutton.pack()

## you can add different variable as options but
## you need the builtins to be able to use them

spam = StringVar()
spam.set('Spam!')
print(spam.get())

checkbutton.config(variable=spam, onvalue='Spam please', offvalue='Boo spam')

## create function to printvar
def printvar():
    print(spam.get())

checkbutton.config(command=printvar)


### Radio buttons--------------------

breakfast = StringVar()

ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()


## we can change the value of the checkbox based on the radio button
checkbutton.config(textvariable=breakfast)

root.mainloop()

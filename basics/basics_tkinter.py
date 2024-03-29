""" Miscellaneous tkinter exercises """

from tkinter import *

window = Tk()
e1_value = StringVar()

def km_to_miles():
    """ Convert kilometeres to miles """
    miles = float(e1_value.get())*1.6
    t1.delete("1.0", END)
    t1.insert(END, miles)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()

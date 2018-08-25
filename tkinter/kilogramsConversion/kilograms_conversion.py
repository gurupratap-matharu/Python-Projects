from tkinter import *

window = Tk()


def kgConversion():
    query = float(e1_value.get())
    grams = query * 1000
    pounds = query * 2.20462
    ounces = query * 35.274

    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


b1 = Button(window, text="Convert", command=kgConversion)
b1.grid(row=0, column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=3)


window.mainloop()

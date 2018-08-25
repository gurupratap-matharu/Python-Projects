"""This script is just for practicing tkinter. Nada mas"""

from tkinter import *

window = Tk()
window.wm_title("Matharu Family")

l1 = Label(window, text="Santokh Singh Matharu")
l1.grid(row=0, column=2)

l2 = Label(window, text="Jasbir Kaur Matharu")
l2.grid(row=0, column=3)

l3 = Label(window, text="Jaspal Singh Matharu")
l3.grid(row=30, column=0)

l4 = Label(window, text="Jasvinder Kaur Matharu")
l4.grid(row=30, column=1)

l5 = Label(window, text="Inderpal Singh Matharu")
l5.grid(row=30, column=2)

l6 = Label(window, text="Harjinder Kaur Matharu")
l6.grid(row=30, column=3)


l7 = Label(window, text="Satpal Singh Matharu")
l7.grid(row=30, column=4)

l8 = Label(window, text="Jatinder Kaur Matharu")
l8.grid(row=30, column=5)


window.mainloop()

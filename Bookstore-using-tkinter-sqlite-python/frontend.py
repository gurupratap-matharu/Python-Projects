"""
A program that stores this book information:
Titlee, Author
Year, ISBN

User can:

View all records
Search an entry
Update entry
Delete entry
Close entry
"""
from tkinter import *
from backend import Database

database = Database("books.db")


class Command():
    """Base class for actions of commands issued on the frontend"""

    def __init__(self):
        pass

    def get_selected_row(self, event):
        try:
            index = list1.curselection()[0]
            self.selected_tuple = list1.get(index)
            e1.delete(0, END)
            e1.insert(END, self.selected_tuple[1])
            e2.delete(0, END)
            e2.insert(END, self.selected_tuple[2])
            e3.delete(0, END)
            e3.insert(END, self.selected_tuple[3])
            e4.delete(0, END)
            e4.insert(END, self.selected_tuple[4])

        except IndexError:
            pass

    def view(self):
        """Populates the list box with the view function from backend"""
        list1.delete(0, END)
        for row in database.view():
            list1.insert(END, row)

    def add(self):
        """Adds entry to the backend database with the string populated in the entry boxes."""
        database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.delete(0, END)
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

    def delete(self):
        """Deletes the selected item from the list widget from the backend database"""
        database.delete(self.selected_tuple[0])

    def update(self):
        """Fetches new data from the entry widgets and updates them in the database"""
        database.update(self.selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

    def search(self):
        """Populates the list widget with the search matches between the entry widgets and the backend database."""
        row = database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.delete(0, END)
        list1.insert(END, row)


command = Command()

window = Tk()

window.wm_title("Book Store")
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', command.get_selected_row)


b1 = Button(window, text="View all", width=12, command=command.view)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=command.search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=command.add)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=command.update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=command.delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()

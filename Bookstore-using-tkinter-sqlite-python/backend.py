""" We import the sql library to create an sqlite database. """
import sqlite3


class Database:

    def __init__(self, db):
        """Object initialization for the Database class."""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        """Allows to add a new entry to the table with the arguments passed"""
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        """Simply returns all the entries of the database as a list of tuples"""
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        """Searches the database for a particular entry based on the arguments passed. Arguments are optional or Kwargs"""
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        """Deletes a particular row from the database referring to the id passed"""
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        """Updates the table entry with the arguments passed"""
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        """Destroys the instance of the class when the script is closed"""
        self.conn.close()

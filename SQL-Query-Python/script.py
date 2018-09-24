import sqlite3


def create_table():
    """Creates the basic sqlite table and ignores if already exists."""
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert_table(item, quantity, price):
    """Inserts merchandise into the sql table"""
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view_table():
    """Pulls up all the rows of the table as a list of tuples."""
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_table(item):
    """deletes the passed item from the table"""
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update_table(item, quantity, price):
    """Updates the Quantity and Price within the table for a particular item."""
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# insert_table("Wine Cup", 10, 40)
# insert_table("Coffee Cup", 5, 40)
# insert_table("Diamond Cup", 10, 400)
# insert_table("Football Cup", 10, 40)
# delete_table("Wine Cup")
update_table("Coffee Cup", 15, 20
    )
print(view_table())

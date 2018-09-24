import sqlite3


def create_table():
    """Creates the basic sqlite table. Ignores if already exists"""
    conn = sqlite3.connect("outofindia.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS outofindia (Articulo TEXT, Cantidad INTEGER, Precio REAL)")
    conn.commit()
    conn.close()


def insert_table(Articulo, Cantidad, Precio):
    """Inserts merchandise into the table"""
    conn = sqlite3.connect("outofindia.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO outofindia VALUES(?, ?, ?)", (Articulo, Cantidad, Precio))
    conn.commit()
    conn.close()


def view_table():
    """Views all the rows of the table. Returns a list of tuples."""
    conn = sqlite3.connect("outofindia.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM outofindia")
    rows = cur.fetchall()
    conn.close()
    return rows


create_table()

insert_table("Lamparas", 1, 200)
insert_table("Aceite", 1, 35)
insert_table("Corre de Mesa", 3, 210)
insert_table("Cubrecama 1 Plaza", 150, 200)
insert_table("Cubrecama 2 Plaza", 100, 300)
insert_table("Bolsas", 30, 250)

merchandise = view_table()
for i in merchandise:
    print(i)

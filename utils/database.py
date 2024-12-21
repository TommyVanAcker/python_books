import sqlite3


def create_book_table():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
        connection.commit()

def add_book(name, author):
   with sqlite3.connect('data.db') as connection:
       cursor = connection.cursor()
       cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
       connection.commit()


def get_all_books():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books') #creates a list with tuples
        #turn into dictionary with list comprehension
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books



def mark_as_read(name):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        #the parameter of the execute must be a tuple
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))
        connection.commit()


def delete_book(name):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))
        connection.commit()
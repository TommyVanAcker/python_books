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


def _save_all_books(books):
    with open(book_file, 'w') as file:
        json.dump(books, file)

def mark_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
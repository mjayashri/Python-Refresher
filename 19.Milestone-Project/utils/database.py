"""
Concerned with storing and retrieving from csv file
name,author,read\n
"""
from .database_connection import DatabaseConnection

books_file = 'books.txt'


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  books(name text primary key, author text, read integer)')


def add_book(author, book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (book_name, author))


def list_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT *  FROM  books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # [(name,author,read)]
        return books


def mark_books_as_read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_name,))


def delete_the_book(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (book_name,))

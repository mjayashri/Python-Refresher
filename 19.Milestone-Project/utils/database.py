"""
Concerned with storing and retrieving from csv file
name,author,read\n
"""
from typing import List, Dict, Union

from .database_connection import DatabaseConnection

Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  books(name text primary key, author text, read integer)')


def add_book(author: str, book_name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (book_name, author))


def list_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT *  FROM  books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in
                 cursor.fetchall()]  # [(name,author,read)]
        return books


def mark_books_as_read(book_name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_name,))


def delete_the_book(book_name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (book_name,))
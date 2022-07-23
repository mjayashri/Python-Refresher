from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to make the book as read
- 'd' to delete a book
- 'q' to quit
Your choice:
"""


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("unknown command,Please try again")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    author = input("Enter the author name: ")
    book_name = input("Enter the book name: ")
    database.add_book(author, book_name)


def list_books():
    all_books = database.list_books()
    for book in all_books:
        read = 'Yes' if book['read']  else "No"
        print(f"{book['name']} by {book['author']}, read:{read}")


def prompt_read_book():
    book_name = input("Enter the book name that you finished reading")
    database.mark_books_as_read(book_name)


def prompt_delete_book():
    book_name = input("Enter the book name")
    database.delete_the_book(book_name)


menu()

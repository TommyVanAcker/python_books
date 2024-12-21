from utils import database


USER_CHOICE = """
Enter:
-'a' to add a book
-'r' to mark a book as read
-'l' to list book all books
-'d' to delete book
-'q' to quit

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'l':
            prompt_list_books()
        elif user_input == 'd':
            prompt_remove_book()
        user_input = input(USER_CHOICE)
    
def prompt_add_book():
    name = input('provide the title of the book: ')
    author = input('provide the author of the book: ')
    database.add_book(name, author)

def prompt_list_books():
    books = database.get_all_books()
    for book in books:
        read = 'yes' if book['read'] else 'no'
        print(f"{book['name']} written by {book['author']} has been read: {read} ")

def prompt_read_book():
    name = input("What is the book title you read?: ")
    database.mark_as_read(name=name)

def prompt_remove_book():
    name = input("What book would you like to remove: ")
    database.delete_book(name=name)


menu()
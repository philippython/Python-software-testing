
class Library:

    def __init__(self):
        self.shelf = {}

    def add_book(self, book_name, book_rating):
        
        if book_name not in self.shelf.keys():
            book = {}
            book[book_name] = book_rating
            self.shelf[book_name] = book
        else:
            return f"Book {book_name} already in the library with rating {self.shelf.get(book_name)}"

    def get_book(self, book_name):
        if book_name not in self.shelf.keys():
            return f"Book {book_name} does not exist in the library"
        else:
            return self.shelf.get(book_name)

    def get_all_books(self):
        return self.shelf

book_library = Library()
book_library.add_book('Journey of philip', 8.9)
book_library.add_book('Rise', 9.9)
print(book_library.get_all_books())
print(book_library.get_book('Rise'))
print(book_library.get_book('rise'))

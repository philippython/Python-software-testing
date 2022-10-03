
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

    def get_book_by_name(self, book_name):
        if book_name not in self.shelf.keys():
            return f"Book {book_name} does not exist in the library"
        else:
            return self.shelf.get(book_name)

    def get_books_by_ratings(self, book_ratings):
        books = self.shelf.values()
        book_same_rating = {}
        for book in books:
            if book_ratings in book.values() :
                book_same_rating.update(book)
        print('No book has the rating of %s' % (book_ratings)) if book_same_rating == {} else print(book_same_rating)

    def change_book_rating(self, book_name, new_rating):
        if book_name not in self.shelf.keys():
            return f"Book {book_name} does not exist in the library"
        else:
            book = self.shelf.get(book_name)
            book[book_name] = new_rating
            return f"Book rating updated to {new_rating}"

    def delete_book(self, book_name):
        if book_name in self.shelf.keys():
            self.shelf.pop(book_name)
            #  or del self.shelf[bookname]
            print("%s has been removed from library" % (book_name))
        else:
            print("Book doesn't exist in library")
    
    def get_all_books(self):
        return self.shelf

# book_library = Library()
# book_library.add_book('Journey of philip', 8.9)
# book_library.add_book('Rise', 9.9)
# book_library.add_book('Cinderalla', 9.9)
# book_library.add_book('25-21', 8.9)
# book_library.add_book('Alchemy of souls', 8.0)
# print(book_library.get_all_books())
# print(book_library.get_book_by_name('Rise'))
# book_library.get_books_by_ratings(9.0)
# book_library.change_book_rating('Rise', 4.5)
# book_library.change_book_rating('rise', 4.5)
# print(book_library.get_all_books())
def main():

    library = Library()
    choice = input('What operation would you like to perform \n 1. Add a new book \n 2. Get all books in library 3. Get all books with \ same ratings \n 4. Delete a book \n 5. Update book rating 6. Get a single book')

    if choice == '1' :
        book_name = 
        library.add_book()
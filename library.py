
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
def terminator():
    quit =input('Would you like to perform more operations (Y/N)').lower()
    if quit == 'y': 
        main()
    else: 
        return

def main():

    library = Library()
    library.add_book('Journey of philip', 8.9)
    library.add_book('Rise', 9.9)
    library.add_book('Cinderalla', 9.9)
    library.add_book('25-21', 8.9)
    library.add_book('Alchemy of souls', 8.0)
    library.add_book('Toy store', 6.0)

    choice = input('What operation would you like to perform \n 1. Add a new book \n 2. Get all books in library \n 3. Get all books with same ratings \n 4. Delete a book \n 5. Update book rating 6. Get a single book')

    if choice == '1' :
        book_name = input('What is the name of the book you want to add')
        book_rating = input('What is the rating of the book')
        library.add_book(book_name, book_rating)

        terminator()
        

    elif choice == '2' :
        library.get_all_books()

        terminator()


    elif choice == '3' :
        book_rating = input('What is the rating of the books you need')
        library.get_books_by_ratings(book_rating)

        terminator()

    elif choice == '4' :
        book_name = input('What is the name of the book you want to delete')
        library.delete_book(book_name)

        terminator()

    elif choice == '5' :
        book_name = input("What is the name of the book you want to change its ratings")
        new_rating = input('What is the new rating of the book')
        library.change_book_rating(book_name, new_rating)
    
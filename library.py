class Library:

    def __init__(self):
        self.shelf = {}

    def add_book(self, book_name, book_rating):
        
        if book_name not in self.shelf.keys():
            book = {}
            book[book_name] = book_rating
            self.shelf[book_name] = book
        else:
           print( f"Book {book_name} already in the library with rating {self.shelf.get(book_name)}")

    def get_book_by_name(self, book_name):
        print(self.shelf.get(book_name, f"Book {book_name} does not exist in the library"))

    def get_books_by_ratings(self, book_ratings):
        books = self.shelf.values()
        book_same_rating = {}
        for book in books:
            if book_ratings in book.values() :
                book_same_rating.update(book)
        print('No book has the rating of %s' % (book_ratings)) if book_same_rating == {} else print(book_same_rating)

    def change_book_rating(self, book_name, new_rating):
        if book_name not in self.shelf.keys():
           print(f"Book {book_name} does not exist in the library")
        else:
            book = self.shelf.get(book_name)
            book[book_name] = new_rating
            print( f"Book rating updated to {new_rating}" )

    def delete_book(self, book_name):
        if book_name in self.shelf.keys():
            self.shelf.pop(book_name)
            # del self.shelf[book_name]
            print("%s has been removed from library" % (book_name))
        else:
            print("Book doesn't exist in library")
    
    def get_all_books(self):
       print(self.shelf)

expected_output = {'Journey of philip': {'Journey of philip': 8.9}, 
                    'Rise': {'Rise': 9.9}, 
                    'Cinderalla': {'Cinderalla': 9.9}, 
                    '25-21': {'25-21': 8.9},
                    'Alchemy of souls': {'Alchemy of souls': 8.0}
                   }



library = Library()
library.add_book('Journey of philip', 8.9)
library.add_book('Rise', 9.9)
library.add_book('Cinderalla', 9.9)
library.add_book('25-21', 8.9)
library.add_book('Alchemy of souls', 8.0)
# print(library.get_all_books())
# print(library.get_book_by_name('Rise'))
# library.get_books_by_ratings(9.0)
# library.change_book_rating('Rise', 4.5)
# library.change_book_rating('rise', 4.5)
print(library.get_all_books())

